import os
import shutil
import socket
import ast
import time
import threading
from .Server_photos import ServerPhotos


class DeleteList:
    lst = None

    @staticmethod
    def countdown(seconds):
        # 15 seconds more than the regular time
        seconds += 15
        
        while seconds:
            time.sleep(1)
            seconds -= 1
            
        os._exit(0)

    @staticmethod
    def start():
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("127.0.0.1", 1077))
        server.listen(5)
        while True:
            client_socket, ipaddress = server.accept()

            full_msg = ServerPhotos.get_data(DeleteList, client_socket, "r", 20)
            if "[" in full_msg:
                DeleteList.lst = ast.literal_eval(full_msg)

            elif full_msg == "done":
                if DeleteList.lst:
                    os.chdir("..")
                    for each in DeleteList.lst:
                        shutil.rmtree(each)
                os._exit(0)

            else:
                threading_lst = threading.Thread(target=DeleteList.countdown, args=(int(full_msg), ))
                threading_lst.start()
