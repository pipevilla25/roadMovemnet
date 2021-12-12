import configuation_package as sy
import  RPi.GPIO as GPIO
import time
yellow = 15
red = 13
green = 11
#Inicializar
GPIO.setmode(GPIO.BOARD)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)

a = 0

GPIO.output(red,GPIO.HIGH)
GPIO.output(yellow,GPIO.HIGH)
GPIO.output(green,GPIO.HIGH)

time.sleep(3)
    
GPIO.cleanup()

