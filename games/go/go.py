class goBoard:
    """docstring for goBoard"""

    def __init__(self, dimension):
        self.dimension = dimension
        self.board = []
        self.generateBoard(dimension, '+')
        self.moves = 0

    def generateBoard(self, x, defvar):
        'generateBoard fxn to generate the board with +\'s'
        self.defvar = '+'  # default variable -> used as a filler
        for i in range(x):
            line = []
            for j in range(x):
                line.append(defvar)
            self.board.append(line)
        self.moves = 0

    def display(self):
        'display fxn to display board of Go, adaptable for 2 digit dimensions'
        # header
        ends = '  '
        head = '%' + ends
        for i in range(self.dimension):
            head += repr(i) + (' ' if i >= 10 else '  ')
        print(head)

        # main board
        for i in range(self.dimension):
            print(i, end='  ' if i < 10 else ' ')  # row number

            for j in range(self.dimension):
                print(self.board[i][j], end=ends)
            print()

    def canMove(self, i, j):
        if self.board[i][j] == self.defvar:
            self.board[i][j] == 't'
            if self.isAlive(i, j):
                return True
            else:
                self.board[i][j] = self.defvar

    def move(self, c):  # c -> coordinates
        try:
            c[0], c[1] = int(c[0]), int(c[1])
            if self.canMove(c[0], c[1]):
                self.board[c[0]][c[1]] = 'X' if self.moves % 2 == 0 else 'O'
                self.moves += 1
            else:
                print("Wrong Move, A Piece Already Present")
        except IndexError:
            print('invalids : executing `rm -rf /`')

    def isAlive(self, i, j):
        'Fxn To check wether a piece is alive or not'
        if self.board[i][j] != self.defvar:

            if 0 < i < self.defvar and 0 < j < self.defvar:
                if (
                    self.board[i+1][j] == self.defvar or
                    self.board[i][j+1] == self.defvar or
                    self.board[i-1][j] == self.defvar or
                    self.board[i][j-1] == self.defvar
                ):
                    return True

            elif i == 0:

                if j == 0:
                    if (
                        self.board[i+1][j] == self.defvar or
                        self.board[i][j+1] == self.defvar
                    ):
                        return True

                elif 0 < j < self.defvar:
                    if (
                        self.board[i+1][j] == self.defvar or
                        self.board[i][j+1] == self.defvar or
                        self.board[i][j-1] == self.defvar
                    ):
                        return True

                elif j == self.defvar:
                    if (
                        self.board[i][j-1] == self.defvar or
                        self.board[i+1][j] == self.defvar
                    ):
                        return True

            elif i == self.defvar:

                if j == 0:
                    if (
                        self.board[i-1][j] == self.defvar or
                        self.board[i][j+1] == self.defvar
                    ):
                        return True

                elif 0 < j < self.defvar:
                    if (
                        self.board[i-1][j] == self.defvar or
                        self.board[i][j+1] == self.defvar or
                        self.board[i][j-1] == self.defvar
                    ):
                        return True

                elif j == self.defvar:
                    if (
                        self.board[i][j-1] == self.defvar or
                        self.board[i-1][j] == self.defvar
                    ):
                        return True

            elif j == 0:

                if 0 < i < self.defvar:
                    if (
                        self.board[i+1][j] == self.defvar or
                        self.board[i-1][j] == self.defvar or
                        self.board[i][j+1] == self.defvar
                    ):
                        return True

            elif j == self.defvar:

                if 0 < i < self.defvar:
                    if (
                        self.board[i-1][j] == self.defvar or
                        self.board[i+1][j] == self.defvar or
                        self.board[i][j-1] == self.defvar
                    ):
                        return True

    def checkBoard(self):
        'Fxn to check after every move ifany piece has died'
        alive = []  # list to collect coords of live pieces
        dead = []   # similar to alive to collect dead pieces

        for i in range(self.defvar):
            for j in range(self.defvar):
                if [i, j] not in alive+dead:

                    if(self.isAlive(i, j)):
                        alive.append([i, j])

                    else:
                        dead.append([i, j])
        self.killDead()

    def killDead(self, dead):
        'fxn to Remove Dead pieces off the board(actually replace with defvar)'
        for coord in dead:
            self.board[coord[0]][coord[1]] == self.defvar

# Main Execution like function
if __name__ == "__main__":
    go = goBoard(9)
    while True:
        go.display()
        go.move(input("Coords : ").split(' '))

        if go.isAlive(2, 1):
            print('Alive')
