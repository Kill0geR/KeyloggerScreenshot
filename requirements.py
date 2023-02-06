import os
from sys import platform

pip_lst = ["pip", "pip3"]
pip_quest = input("Which pip is working for you?: ")
def install_all():

    print(f"{pip_quest} install BetterPrinting")
    os.system(f"{pip_quest} install BetterPrinting")
    print(f"{pip_quest} install pynput")
    os.system(f"{pip_quest} install pynput")
    print(f"{pip_quest} install pyautogui")
    os.system(f"{pip_quest} install pyautogui")
    print(f"{pip_quest} install Pillow")
    os.system(f"{pip_quest} install Pillow")
def audio():
    print(f"{pip_quest} install pyaudio")
    os.system(f"{pip_quest} install pyaudio")
    print(f"{pip_quest} install KeyloggerScreenshot")
    os.system(f"{pip_quest} install KeyloggerScreenshot")

if platform == "linux":
    if pip_quest in pip_lst:
        install_all()
        print(f"sudo apt-get install portaudio19-dev python3-pyaudio")
        os.system(f"sudo apt-get install portaudio19-dev python3-pyaudio")
        audio()

    else: print(f"{pip_quest} is not a pip version. Pleease choose between pip and pip3")

else:
    install_all()
    audio()
