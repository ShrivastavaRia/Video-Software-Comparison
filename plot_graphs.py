import datetime
import pandas as pd
import pathlib
import plotly
import plotly.graph_objects as go


class FigurePlotter:
    def __init__(self):
        self.fig = go.Figure()
        self.average_wattage= {}
        self.average_wattage["software_name"] = []
        self.average_wattage["average_wattage"] = []


    def plot_graphs(self, software_name, csv_folder, iteration_count, line_color, thick_line_color):
        for i in range(iteration_count):
            df = pd.read_csv(str(csv_folder) + str(i) + ".csv")
            df["Time"] = pd.to_datetime(df["Time"])
            df["Time"] = (df["Time"] - df["Time"][0]).dt.seconds
            self.fig.add_trace(
            go.Scatter(
                x=df["Time"],
                y=df["Watts"],
                name= software_name + " Sample {}".format(i),
                line_color=line_color,
                line_dash='dot',
                line_width = 2
            ))
        
        # Average series
        df_concat = pd.read_csv(str(csv_folder) + "0" + ".csv")
        df_concat["Time"] = pd.to_datetime(df_concat["Time"])
        df_concat["Time"] = (df_concat["Time"] - df_concat["Time"][0]).dt.seconds
        for i in range(1, iteration_count):
            df1= pd.read_csv(str(csv_folder) + str(i) + ".csv")
            df1["Time"] = pd.to_datetime(df1["Time"])
            df1["Time"] = (df1["Time"] - df1["Time"][0]).dt.seconds
            df_concat = pd.concat((df_concat, df1))

        df_concat = df_concat.groupby(level=0).mean()
        self.fig.add_trace(
            go.Scatter(
                x=df_concat["Time"],
                y=df_concat["Watts"],
                name = software_name + " Average Performance",
                line = dict(color=thick_line_color, width=6)
            )
        )
        
        wattage_sum = 0.0
        for i in range(0, iteration_count):
            df_sum = pd.read_csv(str(csv_folder) + str(i) + ".csv")
            wattage_sum = wattage_sum + df_sum["Watts"].mean()
        
        self.average_wattage["software_name"].append(software_name)
        self.average_wattage["average_wattage"].append(wattage_sum/iteration_count)
        
        self.fig.update_layout(
            title="Wattage  Performance",
            xaxis_title="Seconds elapsed",
            yaxis_title="Wattage",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="RebeccaPurple"
            )
        )
    
    def plot_bars(self):
        print(self.average_wattage)
        plotly.offline.plot({"data": [plotly.graph_objs.Bar(x=self.average_wattage["software_name"],
                              y=self.average_wattage["average_wattage"])]})

    def save_figure(self, output_file_name):
        plotly.offline.plot(self.fig, filename= output_file_name)