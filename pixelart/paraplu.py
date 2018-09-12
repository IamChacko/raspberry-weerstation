from sense_hat import SenseHat
from time import sleep
sense=SenseHat()

g = (0, 255, 0)
c = (0, 255, 255)
o = (255, 128, 0)
y = (255, 255, 0)
r = (255, 0, 0)
b = (0, 0, 255)
w = (255, 255, 255)
p = (102, 0, 204)
e = (0, 0, 0)
f = (255, 0, 255)



frame1 = [e,e,e,c,e,e,e,e,e,c,c,c,c,c,e,e,c,c,c,c,c,c,c,e,c,e,e,c,e,e,c,e,e,e,e,c,e,e,e,e,e,e,e,c,e,e,e,e,e,e,e,c,e,c,e,e,e,e,e,e,c,e,e,e]

## This demo program will show each frame for 1 second ##
sense.set_pixels(frame1)
sleep(1.5)


sense.clear()
