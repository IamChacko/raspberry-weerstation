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



frame1 = [e,e,e,e,e,e,e,e,e,e,e,b,b,b,e,e,e,e,b,b,b,b,b,e,e,e,b,b,c,b,b,e,e,e,c,b,b,b,c,e,e,e,e,e,c,e,e,e,e,e,c,e,e,e,c,e,e,e,e,e,c,e,e,e]

frame2 = [e,e,e,e,e,e,e,e,e,e,e,b,b,b,e,e,e,e,b,b,b,b,b,e,e,e,c,y,b,b,c,e,e,e,e,y,c,b,e,e,e,e,c,e,y,e,c,e,e,e,e,e,c,y,e,e,e,e,c,e,y,e,c,e]

frame3 = [e,e,e,e,e,e,e,e,e,e,e,b,b,b,e,e,e,e,b,b,b,b,b,e,e,e,b,b,c,b,b,e,e,e,c,b,b,b,c,e,e,e,e,e,c,e,e,e,e,e,c,e,e,e,c,e,e,e,e,e,c,e,e,e]

## This demo program will show each frame for 1 second ##
sense.set_pixels(frame1)
sleep(0.5)

sense.set_pixels(frame2)
sleep(0.5)

sense.set_pixels(frame3)
sleep(0.5)


sense.clear()
