
import RPi.GPIO as GPIO
import asyncio

class GpioHandler:
    def __init__(self,parent):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17 , GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.parent = parent 

    async def start_monitoring_door(self ,interval):
        while True: 
            if GPIO.input(17) == GPIO.HIGH:
                print("open")
                self.parent.open = True
            else:
                print("closed")
                self.parent.open = False

            await asyncio.sleep(interval)
    