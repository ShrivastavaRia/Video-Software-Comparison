import datetime

import join_bbb_meeting
import join_jitsi_meeting
import join_zoom_meeting
from plot_graphs import  PlotFigures

import pathlib
import time

JITSI_FOLDER = (
    pathlib.Path(__file__).parent.absolute() / "jitsi_output" / "measurement_"
)
JITSI_SHARE_FOLDER = (
    pathlib.Path(__file__).parent.absolute() / "jitsi_share_output" / "measurement_"
)

BBB_FOLDER = pathlib.Path(__file__).parent.absolute() / "bbb_output" / "measurement_"
BBB_SHARE_FOLDER = pathlib.Path(__file__).parent.absolute() / "bbb_share_output" / "measurement_"

ZOOM_FOLDER = pathlib.Path(__file__).parent.absolute() / "zoom_output" / "measurement_"
ZOOM_SHARE_FOLDER = pathlib.Path(__file__).parent.absolute() / "zoom_share_output" / "measurement_"

METRIC_FOLDER = str(pathlib.Path(__file__).parent.absolute() / "images"/"performance_")


NUM_ITERATIONS = 10

for i in range(NUM_ITERATIONS):
    print("Iteration %s time %s" % (i, datetime.datetime.now()))
    bbb_file_path = str(BBB_FOLDER) + str(i) + ".csv"
    bbb_share_file_path = str(BBB_SHARE_FOLDER) + str(i) + ".csv"
    join_bbb_meeting.measure_join_meeting(bbb_file_path, is_share=False)
    time.sleep(10)
    join_bbb_meeting.measure_join_meeting(bbb_share_file_path, is_share=True)
    time.sleep(10)


# for i in range(NUM_ITERATIONS):
#     zoom_file_path = str(ZOOM_FOLDER) + str(i) + ".csv"
#     zoom_share_file_path = str(ZOOM_SHARE_FOLDER) + str(i) + ".csv"
#     join_zoom_meeting.measure_join_meeting(zoom_file_path, is_share=False)
#     time.sleep(10)
#     join_zoom_meeting.measure_join_meeting(zoom_share_file_path, is_share=True)
#     time.sleep(10)

# for i in range(NUM_ITERATIONS):
#     jitsi_file_path = str(JITSI_FOLDER) + str(i) + ".csv"
#     jitsi_share_file_path = str(JITSI_SHARE_FOLDER) + str(i) + ".csv"
#     join_jitsi_meeting.measure_join_meeting(jitsi_file_path, is_share=False)
#     time.sleep(10)
#     join_jitsi_meeting.measure_join_meeting(jitsi_share_file_path, is_share=True)
#     time.sleep(10)



plot_figure = PlotFigures(NUM_ITERATIONS, "measurement_")
plot_figure.plot_metric_and_average_line_chart_for_all_scenarios("Watts", METRIC_FOLDER + "Watts.html")
plot_figure.plot_metric_and_average_line_chart_for_all_scenarios("core", METRIC_FOLDER + "core.html")
plot_figure.plot_metric_and_average_line_chart_for_all_scenarios("dram", METRIC_FOLDER + "dram.html")
plot_figure.plot_metric_and_average_line_chart_for_all_scenarios("Sys", METRIC_FOLDER + "Sys.html")
plot_figure.plot_box_plots("Watts", METRIC_FOLDER + "Watts_boxplot.html")
plot_figure.plot_box_plots("dram", METRIC_FOLDER + "dram_boxplot.html")