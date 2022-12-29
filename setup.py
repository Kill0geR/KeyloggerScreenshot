from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 6 - Mature',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='KeyloggerScreenshot',
    version='0.2.0',
    description='Exporting Keylogger files, recording audio, recording mouse click information and screenshots of the target. For more information check out my website:https://pypi.org/project/KeyloggerScreenshot/ and my github: https://github.com/Facileee/KeyloggerScreenshot',
    long_description_content_type="text/markdown",
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Fawaz Bashiru',
    author_email='fawazbashiru@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='KeyloggerScreenshot',
    packages=find_packages(),
    install_requires=['pynput', "pyautogui", "pyaudio", "BetterPrinting", "Pillow"]
)