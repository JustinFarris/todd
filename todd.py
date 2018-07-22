#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os
import subprocess
import sys


## Replace all filenames with generic variables
## 

GPIO.setmode(GPIO.BCM)

GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

playfile = "/tmp/playing"
if os.path.exists(playfile):
    os.remove(playfile)
playing = False

print('ToddMode activated!')
print('Do you want to work?')
print('White for NO')
print('Yellow for YES')
print('Both to exit')

while True:
    no_state = GPIO.input(20)
    yes_state = GPIO.input(21)
    if os.path.exists(playfile):
        playing = True
    else:
        playing = False

    if no_state == False and yes_state == True:
        if playing == False:
            print('White/No pressed - White/No button disabled until song completes')
            playing = True
            nopid = subprocess.Popen(["touch /tmp/playing && play -q Songs/BangOriginal.mp3 && rm /tmp/playing"], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
            time.sleep(0.2)
    if yes_state == False and no_state == True:
        print('Yellow/Yes pressed - button still enabled')
        yespid = subprocess.Popen(["play -q brad.wav"], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
        time.sleep(0.2)
    if yes_state == False and no_state == False:
        print ('Both buttons pressed, stopping playback and exiting')
        os.system('killall play')
        exit()
        
