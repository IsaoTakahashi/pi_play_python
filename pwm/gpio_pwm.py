import RPi.GPIO as GPIO
import time

PWM_NO = 24
LED_NO = 17
BUT_NO = 18

dc = 95

GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_NO, GPIO.OUT)
GPIO.setup(LED_NO, GPIO.OUT)
GPIO.setup(BUT_NO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pwm = GPIO.PWM(PWM_NO, 50)

GPIO.output(LED_NO, GPIO.LOW)
pwm.start(dc)

print("Here we go! Press ^C to exit")

try:
 while 1:
  if GPIO.input(BUT_NO): # button is released
   pwm.ChangeDutyCycle(dc)
   GPIO.output(LED_NO, GPIO.LOW)
  else:
   pwm.ChangeDutyCycle(100-dc)
   GPIO.output(LED_NO, GPIO.HIGH)
   time.sleep(0.3)
   GPIO.output(LED_NO, GPIO.LOW)
   time.sleep(0.2)
except KeyboardInterrupt:
 pwm.stop()
 GPIO.cleanup()
