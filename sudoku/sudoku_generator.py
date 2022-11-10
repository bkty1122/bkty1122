import random


# https://codereview.stackexchange.com/questions/88849/sudoku-puzzle-generator


class sudoku:
    # sudoku number random generator
    def __init__(self):

        # set grid number
        # generate [0,0,0,0,0,0,0,0,0] *9
        self.number = list(range(1, 10))
        self.grid = [[0 for _ in range(0, 9)] for _ in range(0, 9)]

    def make_board(self, c=0, m=3):
        "Recursively search for a solution starting at position c."
        grid = self.grid
        n = m**2  # ** = ^, n = 3^2 = 9
  # 設 C= 0, n = 9, c/n = 0 ...9
        i, j = divmod(c, n)
        i0, j0 = i - i % m, j - j % m  # Origin of mxm block
        numbers = self.number
        random.shuffle(numbers)
        for x in numbers:
            if (x not in grid[i]                     # row
                and all(row[j] != x for row in grid)  # column
                and all(x not in row[j0:j0+m]         # block
                        for row in grid[i0:i])):
                grid[i][j] = x
                if c + 1 >= n**2 or self.make_board(c + 1):
                    return grid
        else:
            # No number is valid in this cell: backtrack and try again.
            grid[i][j] = 0
            return None

    def default_board(self):
        self.make_board()
        board = self.grid
        part1 = random.randint(0, 4)
        part2 = random.randint(4, 7)
        part3 = random.randint(7, 10)

        for row in range(0, part1):
            for col in range(0, part1):
                num = 0
                # change board number to 0 to allocate empty spaces
                board[-row][-col] = num

        for row in range(4, part2):
            for col in range(4, part2):
                num = 0
                # change board number to 0 to allocate empty spaces
                board[-row][-col] = num

        for row in range(7, part3):
            for col in range(7, part3):
                num = 0
                # change board number to 0 to allocate empty spaces
                board[-row][-col] = num

        return board

    def print(self):
        if __name__ == '__main__':
            print(self.default_board())


x = sudoku()
x.print()

