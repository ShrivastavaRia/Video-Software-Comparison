from multiprocessing import Process
import create_bbb_meeting
import create_jitsi_meeting
import create_zoom_meeting
import time
import sys

TIMEOUT = 120
KILL_TIMEOUT = 150
MEETING_CREATION_LAG = 70
create_zoom_meeting.create_meeting(timeout=TIMEOUT)
time.sleep(MEETING_CREATION_LAG)
bbb_process = Process(target=create_bbb_meeting.create_meeting, args=(TIMEOUT, ))
jitsi_process = Process(target=create_jitsi_meeting.create_meeting, args=(TIMEOUT, ))
bbb_process.daemon = True
jitsi_process.daemon = True

bbb_process.start()
jitsi_process.start()

bbb_process.join(KILL_TIMEOUT)
jitsi_process.join(KILL_TIMEOUT)

if bbb_process.is_alive():
    print("bbb process hung, terminating")
    bbb_process.terminate()

if jitsi_process.is_alive():
    print("bbb process hung, terminating")
    jitsi_process.terminate()
