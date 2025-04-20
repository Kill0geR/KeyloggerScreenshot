import os
from sys import platform

pip_lst = ["pip", "pip3"]
pip_quest = input("Which pip is working for you (pip or pip3)?: ")


def install_all():
    print(f"{pip_quest} install KeyloggerScreenshot")
    os.system(f"{pip_quest} install KeyloggerScreenshot")
    

if platform == "linux":
    if pip_quest in pip_lst:
        install_all()
        print(f"sudo apt-get install portaudio19-dev python3-pyaudio -y")
        os.system(f"sudo apt-get install portaudio19-dev python3-pyaudio -y")
        install_all()
        print("sudo apt-get install scrot -y")
        os.system("sudo apt-get install scrot -y")

    else: 
        print(f"{pip_quest} is not a pip version. Pleease choose between pip and pip3")

else:
    install_all()
