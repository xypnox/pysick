class point:
    'A simple point in a 2d space'

    def __init__(self, x=0, y=0):
        'Point Initialisation, (xCordinate, yCordinate) both by default are 0'
        self.position(x, y)

    def position(self, x, y):
        'move the point to a position (x, y) in the 2d space'
        self.x = x
        self.y = y

    def distance(self, p):
        'Calculate the distance between self and another point (p)'
        dist = ((self.x - p.x)**2 + (self.y - p.y)**2)**(1/2)
        return dist


me = point(3, 4)
you = point(0, 0)

print(me.distance(you))
