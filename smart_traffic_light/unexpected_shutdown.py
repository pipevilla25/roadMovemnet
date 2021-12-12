#unexpected shutdown
import configuation_package as sy
import  RPi.GPIO as GPIO

yellow = 15
red = 13
green = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)

GPIO.cleanup()


