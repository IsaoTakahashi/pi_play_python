import RPi.GPIO as GPIO
import time

IO_NO = 18

print("start")

GPIO.setmode(GPIO.BCM)
GPIO.setup(IO_NO, GPIO.IN)

try:
 while True:
   print(GPIO.input(IO_NO))
   time.sleep(0.5)
except KeyboardInterrupt:
 print("detect key interrupt\n")

GPIO.cleanup()
print("finished")
