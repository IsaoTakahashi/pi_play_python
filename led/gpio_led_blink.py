import RPi.GPIO as GPIO
import time

# set Using GPIO Pin
IO_NO = 18

print("start")

GPIO.setmode(GPIO.BCM)
GPIO.setup(IO_NO,GPIO.OUT)

GPIO.output(IO_NO, True)
time.sleep(0.5)
GPIO.output(IO_NO, False)
time.sleep(0.5)
GPIO.output(IO_NO, True)
time.sleep(0.5)

GPIO.cleanup()

print("finished")
