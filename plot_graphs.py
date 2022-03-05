import datetime
import pandas as pd
import pathlib
import plotly
import plotly.graph_objects as go


class FigurePlotter:
    def __init__(self):
        self.fig = {}
        self.average_wattage = {}
        self.average_wattage["software_name"] = []
        self.average_wattage["average_wattage"] = []

    def plot_graphs(
        self, software_name, csv_folder, iteration_count, line_color, thick_line_color, metric_name, metric_figure_path
    ):
        for i in range(iteration_count):
            df = pd.read_csv(str(csv_folder) + str(i) + ".csv")
            df["Time"] = pd.to_datetime(df["Time"])
            df["Time"] = (df["Time"] - df["Time"][0]).dt.seconds
            if metric_figure_path in self.fig:
                figure = self.fig[metric_figure_path]
            else:
                self.fig[metric_figure_path] = go.Figure()
            figure = self.fig[metric_figure_path]
            figure.add_trace(
                go.Scatter(
                    x=df["Time"],
                    y=df[metric_name],
                    name=software_name + " Sample {}".format(i),
                    line_color=line_color,
                    line_dash="dot",
                    line_width=2,
                )
            )

        # Average series
        df_concat = pd.read_csv(str(csv_folder) + "0" + ".csv")
        df_concat["Time"] = pd.to_datetime(df_concat["Time"])
        df_concat["Time"] = (df_concat["Time"] - df_concat["Time"][0]).dt.seconds
        for i in range(1, iteration_count):
            df1 = pd.read_csv(str(csv_folder) + str(i) + ".csv")
            df1["Time"] = pd.to_datetime(df1["Time"])
            df1["Time"] = (df1["Time"] - df1["Time"][0]).dt.seconds
            df_concat = pd.concat((df_concat, df1))

        df_concat = df_concat.groupby(level=0).mean()
        figure.add_trace(
            go.Scatter(
                x=df_concat["Time"],
                y=df_concat[metric_name],
                name=software_name + " Average Performance",
                line=dict(color=thick_line_color, width=6),
            )
        )

        wattage_sum = 0.0
        for i in range(0, iteration_count):
            df_sum = pd.read_csv(str(csv_folder) + str(i) + ".csv")
            wattage_sum = wattage_sum + df_sum["Watts"].mean()

        self.average_wattage["software_name"].append(software_name)
        self.average_wattage["average_wattage"].append(wattage_sum / iteration_count)

        figure.update_layout(
            title=metric_name + " Performance",
            xaxis_title="Seconds elapsed",
            yaxis_title=metric_name,
            font=dict(family="Courier New, monospace", size=18, color="RebeccaPurple"),
        )
        self.fig[metric_figure_path] = figure

    def plot_bars(self):
        print(self.average_wattage)
        plotly.offline.plot(
            {
                "data": [
                    plotly.graph_objs.Bar(
                        x=self.average_wattage["software_name"],
                        y=self.average_wattage["average_wattage"],
                    )
                ]
            }
        )

    def save_figure(self):
        for path,figure in self.fig.items():
            plotly.offline.plot(figure, filename=path)
