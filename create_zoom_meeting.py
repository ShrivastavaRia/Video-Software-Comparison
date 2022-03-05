import pyautogui
import time
import webbrowser
from insert_link_into_db import insert_link

import jwt
import requests
import json

# Enter your API key and your API secret
API_KEY = '6r10-mtrReaf-miViO273g'
API_SEC = '7rddurwrF5SniB5JQwbLLq5N1rqCNvDsKF6W'

def create_meeting(timeout):
    # get jwt token
    token = jwt.encode(
        {'iss': API_KEY, 'exp': time.time() + 5000},
        API_SEC,
        algorithm='HS256'
    )

    headers = {'authorization': 'Bearer ' + str(token),
               'content-type': 'application/json'}
    
    # create meeting
    # create json data for post requests
    timeout_in_mins = str(int(timeout/60) + 1)
    print(timeout_in_mins)
    meetingdetails = {"topic": "The title of your zoom meeting",
                    "type": 2,
                    "start_time": "2022-01-20T10: 16: 00",
                    "duration": timeout_in_mins,
                    "timezone": "Europe/Madrid",
                    "agenda": "test",

                    "recurrence": {"type": 1,
                                    "repeat_interval": 1
                                    },
                    "settings": {"host_video": "true",
                                "participant_video": "true",
                                "join_before_host": "False",
                                "mute_upon_entry": "False",
                                "watermark": "true",
                                "audio": "voip",
                                "auto_recording": "cloud"
                                }
                    }
    r = requests.post(
        f'https://api.zoom.us/v2/users/me/meetings',
        headers=headers, data=json.dumps(meetingdetails))
    y = json.loads(r.text)
    url = y["join_url"]
    url = 'https://us05web.zoom.us/j/84515494890?pwd=U2tTZUMrdVZJblhRQ0VDWTdMK1Q0Zz09'
    #insert_link(url)
    webbrowser.open(url)
    time.sleep(5)
    pyautogui.press('right')
    time.sleep(5)
    pyautogui.press('enter')