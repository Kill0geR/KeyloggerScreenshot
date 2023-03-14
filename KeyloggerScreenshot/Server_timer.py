import time
import socket
from .Server_photos import ServerPhotos

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
        full_msg = ServerPhotos.get_data(self, client_socket, "r", 10)
        seconds = int(full_msg)
        self.countdown(seconds)
