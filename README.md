# Loki Prank

Leave your computer unlocked and if anyone tries to mess with it (by moving the mouse), grab a few photos from webcamera and then lock desktop!

## Usage
If you don't already have python: `sudo apt install python3`
if you don't already have pip: `sudo apt-get install python3-pip`

For testing purposes:
If you don't already have virtualenv: `sudo pip3 install virtualenv`
Every timem, enable virtual environment: `source prankvenv/bin/activate`

For the first time install requirements: `pip3 install -r requirements.txt`

Again for testing purposes to execute it inside the virtual environment simply run: `python prank.py`

For easier usage you need to:
1) Install it globally: `pip3 install -r requirements.txt` executed outside of the virtual environment
2) add it as a hotkey in Ubuntu: Setting > Keyboard

For stealth reasons there is no indication that you have enabled the locking mechanism. If you hit it again it should cancel. So keep switch in your head

Find the webcam captures inside the folder where prank.py is located if executed manually or inside HOME_FOLDER if executed via an Ubuntu hotkey

## Configuration
`PHOTO_COUNT = 3` # change the number for more or less photographs

`INITIAL_SECONDS_SLEEP = 10` # change the number if you want to give yourself some more or less time to move out away from the computer

