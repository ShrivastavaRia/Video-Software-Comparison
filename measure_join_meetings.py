import datetime

import join_bbb_meeting
import join_jitsi_meeting
from plot_graphs import FigurePlotter

import pathlib
import time

JITSI_FOLDER = pathlib.Path(__file__).parent.absolute() / "jitsi_output" / "measurement_"
BBB_FOLDER  =  pathlib.Path(__file__).parent.absolute() / "bbb_output" / "measurement_"
NUM_ITERATIONS = 10

# for i in range(NUM_ITERATIONS):
#     jitsi_file_path = str(JITSI_FOLDER) + str(i) + ".csv"
#     join_jitsi_meeting.measure_join_meeting(jitsi_file_path)
#     time.sleep(5)
#     bbb_file_path = str(BBB_FOLDER) + str(i) + ".csv"
#     join_bbb_meeting.measure_join_meeting(bbb_file_path)

fp = FigurePlotter()
fp.plot_graphs("Jitsi", JITSI_FOLDER, NUM_ITERATIONS, "lightblue", "royalblue")
fp.plot_graphs("Big Blue Button", BBB_FOLDER, NUM_ITERATIONS, "lightpink", "deeppink")
fp.plot_bars()
fp.save_figure(str(pathlib.Path(__file__).parent.absolute() / "images"/("performance-figure" + str(datetime.datetime.now()))) + ".html")