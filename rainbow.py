import drawSvg as draw
from math import sqrt

size = 10

class Point:
    def __init__(self, x, y, z):
        if x+y+z != 0:
            raise ValueError("Coords must some to 0")
        self.x = x
        self.y = y
        self.z = z

    def rotate(self):
        self.x, self.y, self.z = -self.z, -self.x, -self.y

    def coords(self):
        x = size * (     3/2 * self.x                  )
        y = size * (sqrt(3)/2 * self.x  +  sqrt(3) * self.z)
        return (x, y)

    def __str__(self):
        return "Point("+str(self.x)+", "+str(self.y)+","+str(self.z)+")"


class RainbowSwirler:
    rainbow = ['#e05016', '#f0e65b', '#99d93f', '#54ebdc', '#3e45c9', '#d14bb9']

    def __init__(self):
        self.d = draw.Drawing(100, 100, origin='center', displayInline=False)

    def doInARainbow(self, pos, drawOne):
        v = pos
        for i in range(6):
            drawOne(v, RainbowSwirler.rainbow[i])
            v.rotate()
            print(v)

    def drawOneCircle(self, point, color, radius):
        pos = point.coords()
        self.d.append(draw.Circle(pos[0], pos[1], radius,
            fill=color, stroke_width=2, stroke='black'))

    def triangleOfCircles(self, pos, color):
        pass

    def save(self):
        self.d.setPixelScale(2)  # Set number of pixels per geometry unit
        self.d.saveSvg('rainbow.svg')
        self.d.savePng('rainbow.png')

r = RainbowSwirler()
r.doInARainbow(Point(3,0,-3), (lambda v, c: r.drawOneCircle(v, c, 5)))
r.save()