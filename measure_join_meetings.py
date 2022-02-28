import join_jitsi_meeting

MEASUREMENT_DURATION = 90

jitsi_output = join_jitsi_meeting.join_meeting(MEASUREMENT_DURATION)
print(jitsi_output)