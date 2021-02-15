import pyautogui 
import argparse
import time


def main():
    # Initialize parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--MeetId", help = "Meeting ID")
    parser.add_argument("-t", "--time", help = "Time to record (mins)")
    parser.add_argument("-p", "--passcode", help = "Passcode to meeting (if no passcode, don't use)")
    args = parser.parse_args()
    record(args.MeetId, float(args.time), args.passcode)


def record(meet_id, record_time, passcode=""):
    #esc clicked to ensure that the win key will open up correctly in the next step
    pyautogui.press('esc',interval=0.1)
    time.sleep(0.2)

    #these lines are simulating starting up zoom by pressing windows key and typing zoom to open program
    pyautogui.press('win',interval=0.1)
    pyautogui.write('zoom')
    pyautogui.press('enter',interval=0.5)
    #time delay to factor for zoom app to load up, good buffer is like 10 sec but its case specific
    time.sleep(3)


    #this part simulates clicking join meeting, entering meeting id and pressing enter to join
    ##Make sure the joinButton.png file is located in the same folder as the python file or else it will not work
    ##this tells the script where to click to join the meeting
    x,y = pyautogui.locateCenterOnScreen('joinButton.png', grayscale=True, confidence=.7)
    pyautogui.click(x,y)
    pyautogui.press('enter',interval=1)
    ## the interval of 1 second is important, if not there, then the meeting id will not be inputted
    pyautogui.write(meet_id)
    pyautogui.press('enter',interval=1)


    ###### password OPTIONAL!!! #####
    # if your meeting has a password then uncomment the code below and enter it here
    # change the value of the variable to your password
    if passcode:
        time.sleep(1)
        pyautogui.press('enter',interval=1)
        pyautogui.write(passcode, interval = 0.2)
        pyautogui.press('enter',interval = 1)

    time.sleep(5)
    ## opening up windows game bar overlay
    pyautogui.hotkey('win','g')
    time.sleep(1)
    ## commencing screen recording
    pyautogui.hotkey('win','alt','r')
    time.sleep(1)
    ## closing windows game bar overlay
    pyautogui.hotkey('win','g')

    #Time to record
    t = record_time*60
    time.sleep(t)

    ## ending screen recording
    pyautogui.hotkey('win','alt','r')
    time.sleep(2)
    ## By default, screen captures are sent to a folder called captures in "videos" in "this PC"

    ## closing Zoom
    pyautogui.hotkey('alt','f4')
    time.sleep(0.5)
    pyautogui.hotkey('alt','f4')


if __name__ == "__main__":
    main()