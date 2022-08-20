import copy
from random import shuffle, randint

class Sudoku:
    def __init__(self, diff, board = False,) -> None:
        if not board:
            self.b = [[0 for i in range(9)] for j in range(9)]
        else:
            self.b = board
        self.d = diff

    def generate(self):
        """Generates a random sudoku board

        Returns:
            List: Sudoku board
        """
        nums =[1,2,3,4,5,6,7,8,9]
        shuffle(nums)
        x = self.b
        x[0] = nums  #Sets a shuffled nums as first row of x
        return self.solve(x) #Solves x with the first row in it to generate a sudoku board

    def remove(self):
        """Removes random numbers from the Sudoku board based pn the difficulty 

        Returns:
            List: Sudoku board with random values removed
        """
        if self.d == "easy": #Decides the number of empty spaces in the board based on difficulty
            a = 81 - randint(50, 60)
        elif self.d == "medium":
            a = 81 - randint(40, 50)
        elif self.d == "hard":
            a = 81 - randint(20, 30)

        x = self.b
        count = 0
        while count != a: #Sets random numbers to zero
            row = randint(0,8)
            col = randint(0,8)
            if x[row][col] != 0:
                x[row][col] = 0
                count += 1
        return x
        

    def solve(self, board):
        """Solves a given Sudoku board

        Args:
            board (List): The sudoku board to be solved

        Returns:
            List: Solved sudoku board
        """
        f = self.empty_space(board)
        x = copy.copy(board)
        if f:
            row, col = f
        else:
            return x
        
        for i in range(1,10):
            if self.valid_pos(x, i, (row, col)):
                x[row][col] = i #Puts in the number in the given position if its not already in the row column or box

                if self.solve(x): #Uses recursion on the given board with new value added to it
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
            if board[cell[0]][i] == num and cell[1] != i: #Checks the row for validity
                return False
            if board[i][cell[1]] == num and cell[0] != i: #Checks the column for validity
                return False

            box_x = cell[0] // 3
            box_y = cell[1] // 3

            for i in range(box_x*3, box_x * 3 + 3): #Checks a 3 x 3 box for the validity of given value
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



    