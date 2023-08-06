import RPi.GPIO as GPIO
import time

relay_pin_number = 18  # Change this to the GPIO pin number connected to the relay

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin_number, GPIO.OUT)

# Turn the relay on
GPIO.output(relay_pin_number, GPIO.HIGH)
print("Relay ON")
time.sleep(5)

# Turn the relay off
GPIO.output(relay_pin_number, GPIO.LOW)
print("Relay OFF")

GPIO.cleanup()
