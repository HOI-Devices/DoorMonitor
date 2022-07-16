# DoorMonitor
Simple Smart device that will notify you if your door is open!

Many people have seen this type of device being used everywhere , most notably it is used in home alarm systems. 
We are using a reed switch "sensor" to determine when a door is open/closed. When the door is open we want to get an alert/to be able to see it
from our user interface(HOI-WebClient/HOI-MobileClient).

## How does this even work?

Reed switches are switches that close/open when a magnet is near. You may be confused why I said "close/open" , but there are some reed switches that are "Normally open"
and some that are "Normally closed". When you put the magnet on the door and the reed switch on the wall closing/opening the door with trigger the circuit to open/close.
We can supply voltage to the reed switch(constant voltage from a 3v hot pin) and on the other end of the circuit we can use a gpio pin to know if the circuit is open/closed.
This we can use to determine if the door is open/closed.

## What will I need to complete this project?

1. Raspberry Pi 4.
2. Reed Switch.
3. Three Female to Female dupont jumper wires.
4. One 1k resistor.

## Guide 
[here](https://github.com/House-of-IoT/Tutorials/blob/main/DoorMonitor.md)
