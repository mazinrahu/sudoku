from sudoku import Sudoku
import copy

a = Sudoku()
solved = copy.deepcopy(a.generate())
rem = a.remove()

for row in solved:
    print(row, end = "\n")
print("\n")

for i in range(9):
    for j in range(9):
        if rem[i][j] == 0:
            for row in rem:
                print(row, end = "\n")
            correct = False
            while correct == False:
                num = int(input(f"What number do you want to put in cell ({i+1},{j+1})? "))
                if a.valid_pos(rem, num, (i,j)):
                    rem[i][j] = num
                    if a.solve(rem) == None:
                        rem[i][j] = 0
                        print("Your answer was incorrect try another number\n")
                    else:
                        correct = True
                else: print("Your answer was incorrect\n")

