import wiringpi as pi
import time

LED_PIN = 23

pi.wiringPiSetupGpio()
pi.pinmode(LED_PIN, pi.OUTPUT)

pi.softPwmCreate(LED_PIN, 0, 100)
pi.softPwmWrite(LED_PIN, 50)
time.sleep(100)