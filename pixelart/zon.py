from sense_hat import SenseHat
from time import sleep
sense=SenseHat()

r = (255, 0, 0)
e = (0, 0, 0)
o = (255, 128, 0)
y = (255, 255, 0)
c = (0, 255, 255)
w = (255, 255, 255)
b = (0, 0, 255)
g = (0, 255, 0)
f = (255, 0, 255)
p = (102, 0, 204)



frame1 = [e,e,e,e,e,e,e,e,e,e,e,y,y,e,e,e,e,e,y,y,y,y,e,e,e,y,y,y,y,y,y,e,e,y,y,y,y,y,y,e,e,e,y,y,y,y,e,e,e,e,e,y,y,e,e,e,e,e,e,e,e,e,e,e]

frame2 = [e,e,e,e,e,e,e,e,e,y,e,e,e,e,y,e,e,e,e,y,y,e,e,e,e,e,y,y,y,y,e,e,e,e,y,y,y,y,e,e,e,e,e,y,y,e,e,e,e,y,e,e,e,e,y,e,e,e,e,e,e,e,e,e]

frame3 = [e,e,e,e,e,e,e,e,e,e,e,y,y,e,e,e,e,e,y,y,y,y,e,e,e,y,y,y,y,y,y,e,e,y,y,y,y,y,y,e,e,e,y,y,y,y,e,e,e,e,e,y,y,e,e,e,e,e,e,e,e,e,e,e]

## This demo program will show each frame for 1 second ##
sense.set_pixels(frame1)
sleep(0.5)

sense.set_pixels(frame2)
sleep(0.5)

sense.set_pixels(frame3)
sleep(0.5)


sense.clear()
