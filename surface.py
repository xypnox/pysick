"""
My crazy surface program

ToDo:

    [ ] ->  check compare fxn (direction = across) !!important!!
    [ ] ->  code other directions fro compare
    [ ] ->  code the win fxn
"""


class surface:
    """Class : Surface
    This is class for the surface or "board" of a 2D game
    """

    def __init__(self, dimensionX, dimensionY, populateString='.'):
        """Initialisation Fxn :
        Initiates the surface with dimensions(X,Y)
        Then populates surface with <populateString>
        """

        self.surf = []
        self.count = []
        self.popString = populateString

        for y in range(dimensionY):
            self.count.append(0)

        for x in range(dimensionX):
            self.surf.append([])

        for x in range(dimensionX):
            for y in range(dimensionY):
                self.surf[x].append(populateString)

    def play(self, coloumn, changeString):
        """Play Fxn :
        Inserts the <changeString> into the specified coloumn,
        If and only if the <count> is less than the empty space of <surface>
        Ideal for games like "4 in a Row" where the turn is
        from down to up
        """

        try:
            self.surf[self.count[coloumn]][coloumn] = changeString
            self.count[coloumn] += 1

        except IndexError:
            print("Enter correct Coloumn")

    def display(self, option=0, header=False):
        """Display Fxn : display the 2D surface according :
        0 : Normal (default)
        1 : Rows Down to Up (useful in games like "4inarow")
        """

        if option == 0:

            if header is True:
                for i in range(len(self.surf[0])):
                    print(i, end=' ')
                print()

                for i in range(len(self.surf[0])):
                    print('=', end=' ')
                print()

            for x in range(len(self.surf)):
                for y in range(len(self.surf[0])):
                    print(self.surf[x][y], end=' ')
                print()

        elif option == 1:

            if header is True:
                for i in range(len(self.surf[0])):
                    print(i, end=' ')
                print()

                for i in range(len(self.surf[0])):
                    print('=', end=' ')
                print()

            for x in range(len(self.surf)):
                for y in range(len(self.surf[0])):
                    print(self.surf[len(self.surf) - x - 1][y], end=' ')
                print()

    def comp(self, iterations, direction):
        if direction == "across":
            incX, incY = 0, 1
            rangeX, rangeY = len(self.surf), len(self.surf[0]) - iterations
        for x in range(rangeX):
            for y in range(rangeY):
                if self.surf[x][y] != self.popString:
                    for i in range(iterations):
                        if self.surf[x + incX][y + incY] == self.surf[x][y]:
                            a = True
                        incX += incX
                        incY += incY
        return a

    def win(self, iterations, equality=True):
        pass

simple = surface(3, 4)
simple.play(3, 'x')
simple.play(2, '0')
simple.display(1, True)
