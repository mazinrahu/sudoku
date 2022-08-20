import pygame
import time
pygame.font.init()
from sudoku import Sudoku

class Grid:
    def __init__(self, rows, cols, width, height, diff):
        a = Sudoku(diff)
        a.generate()
        self.board = a.remove()
        self.rows = rows
        self.cols = cols
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height
        self.model = None
        self.selected = None

    def update_model(self):
        """Updates the board with the new value 
        """
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def place(self, val):
        """Places the value on the board if it is valid

        Args:
            val (int): The value to be placed on the board

        Returns:
            Boolean: Can the value be placed on the board
        """
        a = Sudoku("easy")
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set(val)
            self.update_model()
            #Checks for the validity of the value in the given cube
            if a.valid_pos(self.model, val, (row,col)) and a.solve(self.model):
                return True
            else:
                self.cubes[row][col].set(0)
                self.cubes[row][col].set_temp(0)
                self.update_model()
                return False

    def sketch(self, val):
        """Draws the temporary value given to the sudoku board before the enter key is pressed

        Args:
            val (int): The temporary value given to the sudoku board
        """
        row, col = self.selected
        self.cubes[row][col].set_temp(val)

    def draw(self, win):
        """Draws the grid and cubes on the given surface

        Args:
            win : The surface to be drawn on
        """
        # Draw Grid Lines
        gap = self.width / 9
        for i in range(self.rows+1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, (0,0,0), (0, i*gap), (self.width, i*gap), thick)
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)

        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win)

    def select(self, row, col):
        """Selects the specific cube on the board

        Args:
            row (int): The row index of the cube to be selected
            col (int): The col index of the cube to be selected
        """
        # Reset all other
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        self.cubes[row][col].selected = True
        self.selected = (row, col)

    def clear(self):
        """Removes the number added to the ube by pressing the Delete key 
        """
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temp(0)

    def click(self, pos):
        """Returns the position of the cube that has been clicked on

        Args:
            pos (tuple): The position of the mouse click 

        Returns:
            tuple: (row,col) of the cube which has been clicked on
        """
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y),int(x))
        else:
            return None

    def is_finished(self):
        """SHows if the game ended when there are no more empty spaces left

        Returns:
            Boolean: Has the game ended?
        """
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False
        return True


class Cube:
    def __init__(self, value, row, col, width ,height):
        self.value = value
        self.temp = 0
        self.row = 9
        self.col = 9
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        """Draws the red square around the cube to show it is selected. It also draws the number in the cube.

        Args:
            win : The surface on which things have to be drawn
        """
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        #Enters the temporary value given by the user until the Enter key is pressed
        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, (128,128,128))
            win.blit(text, (x+5, y+5))
        #Sets the correct value when the user presses enter    
        elif self.value != 0:
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))
        #Draws a red square around the box which is selected
        if self.selected:
            pygame.draw.rect(win, (255,0,0), (x,y, gap ,gap), 3)

    def set(self, val):
        """Sets the value in the cube

        Args:
            val (int): The number entered for the cube
        """
        self.value = val

    def set_temp(self, val):
        """Temporarily sets the value in the cube until the enter key is pressed

        Args:
            val (int): The number entered for the given cube
        """
        self.temp = val


def redraw_window(win, board):
    """Draws the grid and board with the values

    Args:
        win : The surface where the window has to be drawn
        board (List): The Sudoku board
    """
    win.fill((255,255,255))
    # Draw grid and board
    board.draw(win)



def main(diff):
    """The main function run the game and all the key presses

    Args:
        diff (str): The difficulty at which the Sudoku game runs
    """
    win = pygame.display.set_mode((540,600))
    pygame.display.set_caption("Sudoku")
    board = Grid(9, 9, 540, 540, diff)
    key = None
    run = True
    while run:

        #All the key presses needed to play the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None
                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.cubes[i][j].temp != 0:
                        if board.place(board.cubes[i][j].temp):
                            print("Success")
                        else:
                            print("Wrong")
                        key = None

                        if board.is_finished():
                            print("Game over")
                            run = False
            #The mouse click to select the cube
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key != None:
            board.sketch(key)

        redraw_window(win, board)
        pygame.display.update()

pygame.quit()