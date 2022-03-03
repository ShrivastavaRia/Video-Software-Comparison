import datetime

import join_bbb_meeting
import join_jitsi_meeting
import join_zoom_meeting
from plot_graphs import FigurePlotter

import pathlib
import time

JITSI_FOLDER = (
    pathlib.Path(__file__).parent.absolute() / "jitsi_output" / "measurement_"
)
METRIC_FOLDER = str(pathlib.Path(__file__).parent.absolute() / "images"/"performance_")
BBB_FOLDER = pathlib.Path(__file__).parent.absolute() / "bbb_output" / "measurement_"

ZOOM_FOLDER = pathlib.Path(__file__).parent.absolute() / "zoom_output" / "measurement_"
NUM_ITERATIONS = 4

# for i in range(NUM_ITERATIONS):
#     zoom_file_path = str(ZOOM_FOLDER) + str(i) + ".csv"
#     jitsi_file_path = str(JITSI_FOLDER) + str(i) + ".csv"
#     bbb_file_path = str(BBB_FOLDER) + str(i) + ".csv"
#     join_zoom_meeting.measure_join_meeting(zoom_file_path)
#     time.sleep(10) # recover from previous software impact
#     join_jitsi_meeting.measure_join_meeting(jitsi_file_path)
#     time.sleep(10) # recover from previous software impact
    # join_bbb_meeting.measure_join_meeting(bbb_file_path)
    # time.sleep(10) # recover from previous software impact

fp = FigurePlotter()
fp.plot_graphs("Jitsi", JITSI_FOLDER, NUM_ITERATIONS, "lightblue", "royalblue","Watts", METRIC_FOLDER + "Watts.html")
fp.plot_graphs("Big Blue Button", BBB_FOLDER, NUM_ITERATIONS, "lightpink", "deeppink", "Watts", METRIC_FOLDER + "Watts.html")
fp.plot_graphs("Zoom", ZOOM_FOLDER, NUM_ITERATIONS, "lightgreen", "darkgreen", "Watts", METRIC_FOLDER + "Watts.html" )

fp.plot_graphs("Jitsi", JITSI_FOLDER, NUM_ITERATIONS, "lightblue", "royalblue","pkg-0", METRIC_FOLDER + "pkg-0.html")
fp.plot_graphs("Big Blue Button", BBB_FOLDER, NUM_ITERATIONS, "lightpink", "deeppink", "pkg-0", METRIC_FOLDER + "pkg-0.html")
fp.plot_graphs("Zoom", ZOOM_FOLDER, NUM_ITERATIONS, "lightgreen", "darkgreen", "pkg-0", METRIC_FOLDER + "pkg-0.html" )


fp.plot_graphs("Jitsi", JITSI_FOLDER, NUM_ITERATIONS, "lightblue", "royalblue","dram", METRIC_FOLDER + "dram.html")
fp.plot_graphs("Big Blue Button", BBB_FOLDER, NUM_ITERATIONS, "lightpink", "deeppink", "dram", METRIC_FOLDER + "dram.html")
fp.plot_graphs("Zoom", ZOOM_FOLDER, NUM_ITERATIONS, "lightgreen", "darkgreen", "dram", METRIC_FOLDER + "dram.html" )

fp.plot_graphs("Jitsi", JITSI_FOLDER, NUM_ITERATIONS, "lightblue", "royalblue","Sys", METRIC_FOLDER + "Sys.html")
fp.plot_graphs("Big Blue Button", BBB_FOLDER, NUM_ITERATIONS, "lightpink", "deeppink", "Sys", METRIC_FOLDER + "Sys.html")
fp.plot_graphs("Zoom", ZOOM_FOLDER, NUM_ITERATIONS, "lightgreen", "darkgreen", "Sys", METRIC_FOLDER + "Sys.html" )
#fp.plot_bars()
fp.save_figure()
