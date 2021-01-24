from gpiozero import LED
from time import sleep
led = LED(21)

for i in range(20):
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    
print("All done :)")