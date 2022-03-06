import datetime
from typing import DefaultDict
import pandas as pd
import pathlib
import plotly
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
from collections import defaultdict


SOFTWARES = ["zoom", "jitsi", "bbb"]
OUTPUTS = ["_share_output", "_output"]
LINE_STYLES = {
    "zoom": {
        "_output":{
            "name": "Zoom",
            "sample_line_color": "lightgreen",
            "average_line_color":"darkgreen",
            "line_style": "solid"
        },
        "_share_output": {
            "name": "Zoom Share Screen",
            "sample_line_color": "lightgray",
            "average_line_color":"darkgreen",
            "line_style": "dot"
        }
    },
    "jitsi": {
        "_output":{
            "name": "Jitsi",
            "sample_line_color": "lightpink",
            "average_line_color":"deeppink",
            "line_style": "solid"
        },
        "_share_output": {
            "name": "Jitsi Share Screen",
            "sample_line_color": "lightyellow",
            "average_line_color":"deeppink",
            "line_style": "dot"
        }
    },
    "bbb": {
        "_output":{
            "name": "Big Blue Button",
            "sample_line_color": "lightblue",
            "average_line_color":"darkblue",
            "line_style": "solid"
        },
        "_share_output": {
            "name": "Big Blue Button Share Screen",
            "sample_line_color": "cyan",
            "average_line_color":"darkblue",
            "line_style": "dot"
        }
    }
}

class PlotFigures:
    def __init__(self, iterations, file_prefix):
        self._dataframes = defaultdict(DefaultDict)
        self._iterations = iterations
        for software in SOFTWARES:
            for output in OUTPUTS:
                for iteration in range(iterations):
                    self._dataframes[software,output,iteration] = pd.read_csv(software + output + "/" + file_prefix + str(iteration) + ".csv")
                    self._dataframes[software,output,iteration]["Time"] = pd.to_datetime(self._dataframes[software,output,iteration]["Time"])
                    self._dataframes[software,output,iteration]["Time"] = (self._dataframes[software,output,iteration]["Time"] - self._dataframes[software,output,iteration]["Time"][0]).dt.seconds



    def plot_metric_and_average_line_chart_for_all_scenarios(self, metric, file_to_save, trace_lines=False, average_performance=True):
        figure = go.Figure()
        if trace_lines:
            for software in SOFTWARES:
                for output in OUTPUTS:
                    for iteration in range(self._iterations):
                        figure.add_trace(
                            go.Scatter(
                                x=self._dataframes[software,output, iteration]["Time"],
                                y=self._dataframes[software,output, iteration][metric],
                                name=LINE_STYLES[software][output]["name"] + " iteration {}".format(iteration),
                                line_color=LINE_STYLES[software][output]["sample_line_color"],
                                line_dash="dot",
                                line_width=2,
                            )
                        )
        if average_performance:
            for software in SOFTWARES:
                for output in OUTPUTS:
                    df_concat = self._dataframes[software, output, 0]
                    for iteration in range(1, self._iterations):
                        df_concat = pd.concat((df_concat , self._dataframes[software, output, iteration]))
                    df_concat =  df_concat.groupby(level=0).mean()
                    figure.add_trace(
                        go.Scatter(
                            x=df_concat["Time"],
                            y=df_concat[metric],
                            name = LINE_STYLES[software][output]["name"] + " Average Performance",
                            line = dict(color=LINE_STYLES[software][output]["average_line_color"], width = 6, dash = LINE_STYLES[software][output]["line_style"])
                    )
                )
        plotly.offline.plot(figure, filename=file_to_save)


    def plot_box_plots(self, metric, file_to_save):
        x_axis_names = []
        y_axis_names = []
        df_scores = []
        for software in SOFTWARES:
            for output in OUTPUTS:
                df_concat = self._dataframes[software, output, 0]
                for iteration in range(1, self._iterations):
                    df_concat = pd.concat((df_concat , self._dataframes[software, output, iteration]))
                df_concat =  df_concat.groupby(level=0).mean()
                df_scores.append(pd.DataFrame({metric :df_concat[metric].tolist(),'Video Software': LINE_STYLES[software][output]["name"]}))
        df_concat = df_scores[0]
        for i in range(1,len(df_scores)):
            df_concat = pd.concat([df_concat, df_scores[i]])
        figure = px.box(data_frame = df_concat,y = metric, x = 'Video Software',title = "Boxplot Comparison for {} consumed".format(metric), points="all", color_discrete_sequence = ["red", "green", "blue"],template="seaborn" )
        plotly.offline.plot(figure, filename=file_to_save)
