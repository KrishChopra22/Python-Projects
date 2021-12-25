Hello!
Before executing the translator.py file,
ensure that you have installed all the required modules.

For installing the modules, follow these steps :

1. Open Command Prompt, run as administrator.
2. Go to location where you need to install all the packages.
3. Now run this command...
	pip install googletrans==4.0.0-rc1  speechRecognition gTTS

4. We also need to install PyAudio but this wasn't working, so you need to go to this site
https://pypi.bartbroe.re/pyaudio/
and download the whl file knowing your python version and your system.
I downloaded "PyAudio-0.2.11-cp310-cp310-win_amd64.whl" this file.
For installing this simply go to the folder where this file was downloaded, open command prompt there
and run
	pip install PyAudio-0.2.11-cp310-cp310-win_amd64.whl

5. Done... All the packages are installed successfully, now simply run translator.py file.