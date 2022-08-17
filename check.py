from sudoku import Sudoku
import copy
a = Sudoku()
a.generate()
a.remove()
print(a)
b = copy.deepcopy(a)
b.solve(b.b)

print(b)
print(a)