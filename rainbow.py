import drawSvg as draw
import numpy as np


class RainbowSwirler:
    rainbow = ['#e05016', '#f0e65b', '#99d93f', '#54ebdc', '#3e45c9', '#d14bb9']

    def __init__(self):
        self.d = draw.Drawing(100, 100, origin='center', displayInline=False)

    def doInARainbow(self, pos, drawOne):
        v = pos
        theta = np.radians(60)
        rotate = np.array([[np.cos(theta), -np.sin(theta)],[np.sin(theta), np.cos(theta)]])
        for i in range(6):
            drawOne(v, RainbowSwirler.rainbow[i])
            v = rotate.dot(v)

    def drawOneCircle(self, pos, color, radius):
        self.d.append(draw.Circle(pos[0], pos[1], radius,
            fill=color, stroke_width=2, stroke='black'))

    def save(self):
        self.d.setPixelScale(2)  # Set number of pixels per geometry unit
        self.d.saveSvg('rainbow.svg')
        self.d.savePng('rainbow.png')

r = RainbowSwirler()
r.doInARainbow([30, 0], (lambda v, c: r.drawOneCircle(v, c, 5)))
r.save()