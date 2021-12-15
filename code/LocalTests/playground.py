import numpy as np
import time
import argparse


SEPERATION = 5 
PULSE_SEP   = 10
LED_COUNT = 40
WIDTH     = 3
strip = np.zeros(LED_COUNT)

pixels = np.array([5,6,7,8])

print(pixels)
pixels += 1
print(pixels + 1)

# class Pulse:
#     Pulses = []
#     def __init__(self):
#         self.p0 = 
#         self.p1 =
#     def pulsePosition(self):
#         return (self.p0,self.p1)


# x = Pulse(10)
# print(x.pulsePosition())
pulsePixels = []
def addPulse():
    if len(pulsePixels) == 0:
        pulsePixels.append(0)
        pulsePixels.append(-SEPERATION)
    else:
        if pulsePixels[-1] < PULSE_SEP:
            return
        pulsePixels.append(0)
        pulsePixels.append(-SEPERATION)

def updateStrip():
    global pulsePixels
    print(strip , "\n")
    print(pulsePixels , "\n")
    time.sleep(0.3)
    for x in pulsePixels:
        if x >= LED_COUNT:
            pulsePixels.remove(x)
        if x >= 0:
            # print("R1")
            for i in range(WIDTH):
                # print("H", i)
                try:
                    strip[i + x]  = 1
                except:
                    # print("Except" , i)
                    pass
            try:
                strip[x - 1] = 0
            except:
                pass
    pulsePixels = np.array(pulsePixels)  + 1
    pulsePixels = list(pulsePixels)


if __name__ == '__main__':
    print("Hi")
    while True:
        addPulse()
        # print(pulsePixels)
        updateStrip()




