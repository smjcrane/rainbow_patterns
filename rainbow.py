import drawSvg as draw
from math import sqrt

size = 10

class Point:
    def __init__(self, x, y, z):
        if abs(x+y+z) >= 1e-6:
            raise ValueError("Coords must some to 0, but received "+str(x+y+z))
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
    rainbow = ['#d63333', '#eda334', '#2abf43', '#52b5f7', '#5d32c2', '#d93dc1']

    def __init__(self):
        self.d = draw.Drawing(250, 250, origin='center', displayInline=False)
        self.d.append(draw.Rectangle(-250,-250,500,500, fill='#000000'))

    def doInARainbow(self, pos, drawOne):
        v = pos
        for i in range(6):
            drawOne(v, RainbowSwirler.rainbow[i])
            v.rotate()

    def drawOneCircle(self, point, color, radius):
        pos = point.coords()
        self.d.append(draw.Circle(pos[0], pos[1], radius,
            fill=color, stroke_width=2, stroke='black'))

    def trianglesOfCircles(self):
        for p in [[3,-2,-1],[3,-1,-2],[3,0,-3],[3,1,-4],[3,2,-5],[4,1,-5],[5,0,-5],[6,-1,-5],[7,-2,-5],[6,-2,-4],[5,-2,-3],[4,-2,-2],[13/3,-2/3,-11/3]]:
            self.doInARainbow(Point(*p), lambda v, c: r.drawOneCircle(v, c, 6))

    def save(self):
        self.d.setPixelScale(2)  # Set number of pixels per geometry unit
        self.d.saveSvg('rainbow.svg')
        self.d.savePng('rainbow.png')

r = RainbowSwirler()
r.trianglesOfCircles()
r.save()