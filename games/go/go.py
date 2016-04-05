class goBoard:
    """docstring for goBoard"""
    def __init__(self, dimension):
        self.dimension = dimension
        self.board = []
        self.generateBoard(dimension)
        self.moves = 0

    def generateBoard(self, x):
        'generateBoard fxn to generate the board with +\'s'
        for i in range(x):
            line = []
            for j in range(x):
                line.append('+')
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

    def move(self, i, j):
        self.board[i][j] = 'X' if self.moves % 2 == 0 else 'O'
        self.moves += 1

if __name__ == "__main__":
    go = goBoard(19)
    go.display()
    while True:
        go.move(input("i : "), input("j : "))
        go.display()
