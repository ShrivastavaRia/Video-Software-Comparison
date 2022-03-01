import join_jitsi_meeting
import pathlib

JITSI_CSV = pathlib.Path(__file__).parent.absolute() / "jitsi_output" / "measurement"

join_jitsi_meeting.measure_join_meeting(str(JITSI_CSV))