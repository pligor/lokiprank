#!/usr/bin/env python3

from tkinter import *
import time
import pygame
import os
import pyautogui
from pygame import camera
import random
from time import sleep
from os.path import expanduser

PHOTO_COUNT = 3
INITIAL_SECONDS_SLEEP = 10

path = expanduser('~/PRANK_PID')

if os.path.isfile(path):
  with open(path) as fp:
    pid_option = fp.readline()
  #pygame.camera.quit()
  os.system("kill {}".format(pid_option))
  #os.system("echo 'kill' | festival --tts")
  os.unlink(path)
  exit()
else:
  with open(path, 'w') as fp:
    fp.write(str(os.getpid()))
  sleep(INITIAL_SECONDS_SLEEP)

  def take_shot(cam):
    # pygame.camera.list_camera() #Camera detected or not
    img = cam.get_image()
    pygame.image.save(img, "filename{}.jpg".format(random.randint(1, 1e8)))

  pygame.camera.init()
  cam = pygame.camera.Camera("/dev/video0",(800,600))
  cam.start()

  root = Tk()

  def current_position():
    return [root.winfo_pointerx(), root.winfo_pointery()]

  pos1 = current_position()
  print(pos1)
  counter = 1
  while True:
    time.sleep(2.0)
    pos2 = current_position()
    if not pos1 == pos2: #run a command:
      print("action!")
      take_shot(cam)

      if counter >= PHOTO_COUNT:
        #os.system("echo 'say hello to candid camera' | festival --tts")
        pyautogui.hotkey('winleft', 'l')
        break

      counter += 1
    pos1 = pos2

  os.unlink(path)

  #root.mainloop()
