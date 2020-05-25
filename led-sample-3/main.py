import wiringpi as pi
import time

LED_PIN = 23

pi.wiringPiSetupGpio()
pi.pinMode(LED_PIN, pi.OUTPUT)
pi.softPwmCreate(LED_PIN, 0, 100)

while True:
	value = 0
	while (value < 100):
		pi.softPwmWrite(LED_PIN, value)
		time.sleep(0.1)
		value = value + 1
	while (value > 0):
		pi.softPwmWrite(LED_PIN, value)
		time.sleep(0.1)
		value = value - 1
