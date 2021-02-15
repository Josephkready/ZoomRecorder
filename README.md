# ZoomRecorder
Automated zoom meeting recorder with full desktop and audio support. Built for **windows**. This uses the installable version of Zoom and OBS. Shout out to https://github.com/BigchillRK/Zoom-Meeting-and-Recording to source code and inspiration. He has great explanations of the setup, so I am coping most of the setup information from there. 


# Installation
1. Install zoom https://zoom.us/download
2. Install OBS https://obsproject.com/welcome
3. Clone the repo to a directory
    git clone https://github.com/Josephkready/ZoomRecorder.git
4. Install requirements `pip install -r requirements.txt`
5. Follow through with configuration 3 steps...
6. Schedule recordings in task scheduler (optional)

# Configuration

1. ### Awake and Signed in
Your computer needs to be AWAKE and SIGNED IN for this method to work.

My preferred method is to keep my computer signed in and block it from going to sleep. You can follow this guide https://www.wikihow.com/Prevent-Windows-10-from-Going-to-Sleep

Alternatively, if you want the pc to wake up at some time and sign in to run this program, you need to enable these settings which I will outline. If your pc can start up from shutdown (e.g. RTC alarm) then you can also do that however I was not able to get this to work. The best way was to wake the pc from sleep and run the python script. Your computer must also be in the desktop directly after waking and must skip the sign in splash screen. To do this, go to start and open up ‘Sign in options’ (just type that in). Find the setting that reads “Require sign-in”, underneath which says, “if you’ve been away, when should Windows require you to sign in again?” and change the setting to “never”.

2. ### Zoom Settings
 There’s some zoom settings you must alter so that the script runs smoothly, mainly settings that automatically join you into the call without clicking join with audio. You can also ensure settings to see that you join with your mic and camera muted but that is optional. Check the boxes of the settings I’ve outlined below

General
 -  Enter full screen automatically when starting or joining a meeting
	- This is so that screen capture will capture the entire screen properly

Video
- Turn off my video when joining meeting (Optional and case specific)

Audio
- Automatically join audio by computer when joining a meeting
	- Very Critical for script to work (NOT OPTIONAL)
- Mute my microphone when joining a meeting (optional)

Finally you will want to make sure you zoom application is already signed into the proper account. The script assumes you have already signed in. A future version might support auto sign in. Once you have signed into zoom, you should remained signed in even if you close the application. 

3. ### OBS Settings

First you need to configure your scene. Here is a example video to help get you up to speed on OBS scenes https://www.youtube.com/watch?v=nQjH1h2bNjQ. Generally I have OBS set to record my entire screen with desktop audio and mic audio. That way if I share my screen during the meeting, it will also be recorded. 

Also you will need to setup your output settings (File->Settings->Output). Most important thing is to set the 'Recording Path' for the output of the recordings. Set this to what ever folder you would like to save the recordings to. Other settings to note are the 'Recoding Format', which I use mp4 (you can use something different if you like). 

Finally we will need to setup a Hotkey. Go to (File->Settings->Hotkeys). Set 'Start Recording' and 'Stop Recording' to 'Pause' (but click in the box and pressing the Pause key). The script is configured to use the Pause key to control recording. If you wish to change it, you will need to update the hotkey in OBS and inside zoom.py file at lines 34 & 71. 

*Note Do NOT add your webcam to your scene in OBS. Zoom and OBS will fight over the webcam. 

## Runtime Arguments

After you have finished installation, you can run the script by calling `python zoom.py -m _____`. You must include some of the following requirements: 

- `-m` Meeting ID (required) 
	- You can find inside the zoom URL, it's an 11 digit number
	- Example: https://us05web.zoom.us/j/**85961665874**
	- `python zoom.py -m=85961665874`
- `-t` Time to record in minutes (required)
	- Set this to the length of time you plan on recording. 
	- Example `python zoom.py -m=85961665874 -t=60` would record the meeting for 1 hour (60 minutes in 1 hour)
	- Note that once the time expires, the recording will stop and **you will leave the zoom meeting automatically**. You may want to set the time a little longer in cause the meeting runs over. 
- `-p` meeting passcode/password. If it's an open meeting don't use it
	- meeting passcodes are often inside the meeting invitation.
	- Example `python zoom.py -m=85961665874 -t=60 -p=Test` 

# Task scheduling

On Windows you can use task scheduler to run this script automatically when you have a scheduled meeting. First you will want to create a bat file for running the ZoomRecorder. Here is an example bat file

 

    cd PathToYourGitCloneofZoomRecorder
    call python zoom.py -m=66666666666 -t=60 -p=test
Then you can create a task in task scheduler to run this bat file when your meeting is about to begin. You can use this guide as a reference https://www.digitalcitizen.life/how-create-task-basic-task-wizard/
