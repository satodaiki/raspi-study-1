import wiringpi as pi
import time

LED_PIN = 23

pi.wiringPiSetupGpio()
pi.pinMode(LED_PIN, pi.OUTPUT)

while True:
	pi.digitalWrite(LED_PIN, pi.LOW)
	time.sleep(1)

	pi.digitalWrite(LED_PIN, pi.HIGH)
	time.sleep(1)
