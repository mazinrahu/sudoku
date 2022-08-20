import copy
def solve( board):
        """Solves a given Sudoku board

        Args:
            board (List): The sudoku board to be solved

        Returns:
            List: Solved sudoku board
        """
        f = empty_space(board)
        x = copy.copy(board)
        if f:
            row, col = f
        else:
            return x
        
        for i in range(1,10):
            if valid_pos(x, i, (row, col)):
                x[row][col] = i

                if solve(x):
                    return x

                x[row][col] = 0
        

def valid_pos(board , num, cell):
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

def empty_space(board):
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