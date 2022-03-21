import subprocess
import os
from dotenv import load_dotenv
import time
import webbrowser
from pynput.keyboard import Controller, Key
from datetime import datetime,timedelta

keyboard = Controller()

while(True):
    try:
        print()
        time.sleep(1)
        time_duration=input("Enter duration time of the meeting in the format (HH:MM || 12:59) = ")
        time_duration_split=time_duration.split(':')
        hours = int(time_duration_split[0])
        minutes = int(time_duration_split[1])
        if(hours > 12 or minutes > 59 or hours and minutes == 0 or hours and minutes < 0):
            time.sleep(1)
            print()
            print("Please enter the duration in correct format")
            continue
        else:
            seconds_duration = int(hours * 60 * 60 + minutes * 60)
            break
    except:
        time.sleep(1)
        print()
        print("Please enter time in the format mentioned (Use : ")

print()
time.sleep(1)
print("Program Started Successfully")
load_dotenv()
ZOOM_LINK = os.environ.get("ZOOM_LINK")
ZOOM_PATH = os.environ.get("ZOOM_PATH")

def openZoom():
    time.sleep(1)
    print("Time = ",datetime.now().strftime("%H:%M:%S"))
    subprocess.Popen(ZOOM_PATH)
    time.sleep(40)
    print("Zoom Started Sucessfully")
    return

def openBrowser():
    time.sleep(1)
    print("Time = ",datetime.now().strftime("%H:%M:%S"))
    webbrowser.open(ZOOM_LINK)
    print("Browser Opened Successfully")
    time.sleep(40)
    os.system("taskkill /im chrome.exe /f")
    time.sleep(2)
    print("Browser Closed Successfully")
    return

def leaveMeeting():
    print("Time = ",datetime.now().strftime("%H:%M:%S"))
    keyboard.press('w')
    time.sleep(2)
    print("Meeting Left Sucessfully")

openZoom()
openBrowser()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
time.sleep(1)
print("Current time = ",current_time)

future_time = now + timedelta(seconds=seconds_duration)
future_time_display = future_time.strftime("%H:%M:%S")
time.sleep(1)
print("Leaving Meeting After = ",future_time_display)

while(True):
    if(datetime.now().strftime("%H:%M:%S")==future_time_display):
        leaveMeeting()
        break
    else:
        continue



