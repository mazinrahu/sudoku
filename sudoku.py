import copy
from random import shuffle, randint

class Sudoku:
    def __init__(self, board = False) -> None:
        if not board:
            self.b = [[0 for i in range(9)] for j in range(9)]
        else:
            self.b = board

    def generate(self):
        """Generates a random sudoku board

        Returns:
            List: Sudoku board
        """
        nums =[1,2,3,4,5,6,7,8,9]
        shuffle(nums)
        x = self.b
        x[0] = nums
        return self.solve(x)

    def remove(self):
        """Removes random numbers from the Sudoku board

        Returns:
            List: Sudoku board with random values removed
        """
        x = self.b
        for i in range(81 - 17):
            row = randint(0,8)
            col = randint(0,8)
            x[row][col] = 0
        return x
        

    def solve(self, board):
        """Solves a given Sudoku board

        Args:
            board (List): The sudoku board to be solved

        Returns:
            List: Solved sudoku board
        """
        f = self.empty_space(self.b)
        x = copy.copy(self.b)
        if f:
            row, col = f
        else:
            return x
        
        for i in range(1,10):
            if self.valid_pos(x, i, (row, col)):
                x[row][col] = i

                if self.solve(x):
                    return x

                x[row][col] = 0
        
    def valid_pos(self, board , num, cell):
        """Checks if the given cell is valid for num

        Args:
            board (list): 
            num (int): A number in range 1 to 9 which has to be checked for validity
            cell (tuple): The cell which has to be checked for validity

        Returns:
            Boolean: The given cell is valid for num
        """
        
        for i in range(9):
            if board[cell[0]][i] == num and cell[1] != i:
                return False
            if board[i][cell[1]] == num and cell[0] != i:
                return False

            box_x = cell[0] // 3
            box_y = cell[1] // 3

            for i in range(box_x*3, box_x * 3 + 3):
                for j in range(box_y*3, box_y*3 + 3):
                    if board[i][j] == num and cell != (i,j):
                        return False
        
        return True


    def empty_space(self, board):
        """Finds the next empty space in the sudoku board

        Args:
            board (list): The sudoku board

        Returns:
            tuple: The next empty cell available
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    return (i,j)
        return False

    def __str__(self) -> str:
        board = ""
        for row in self.b:
            board += f'{row}\n'
        return board



    