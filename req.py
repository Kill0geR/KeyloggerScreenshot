import os
from sys import platform

pip_lst = ["pip3", "pip"]
pip_quest = input("Which pip is working for you?: ")
if platform == "linux":
    if pip_quest in pip_lst:
        print(f"{pip_quest} install BetterPrinting")
        os.system(f"{pip_quest} install BetterPrinting")
        print(f"{pip_quest} install pynput")
        os.system(f"{pip_quest} install pynput")
        print(f"{pip_quest} install pyautogui")
        os.system(f"{pip_quest} install pyautogui")
        print(f"{pip_quest} install Pillow")
        os.system(f"{pip_quest} install Pillow")
        print("sudo apt-get install portaudio19-dev python-pyaudio")
        os.system("sudo apt-get install portaudio19-dev python-pyaudio")
        print(f"{pip_quest} install pyaudio")
        os.system(f"{pip_quest} install pyaudio")
        print(f"{pip_quest} install KeyloggerScreenshot")
        os.system(f"{pip_quest} install KeyloggerScreenshot")

    else:print(f"{pip_quest} is not a pip version. Pleease choose between pip and pip3")