import itertools
import numpy as np
size = 9
def print_grid(a):
    for i in range(size):
        for j in range(size):
            print(a[i][j],end = " ")
        print()
def valid_grid(grid, row, col, num):
    # check if we find the same num in the similar row , we return false
    for i in range(9):
        if grid[row][i] == num:
            return False
    
    # check if we find the same num in the similar column , we return false
    for i in range(9):
        if grid[i][col] == num:
            return False

    # check if we find the same num in the similar 3x3 matrix , we return false
    startRow = row - row % 3
    startCol = col - col % 3
    return all(
        grid[i + startRow][j + startCol] != num
        for i, j in itertools.product(range(3), range(3))
    )
 
def Suduko(grid, row, col):
    
    if (row == size - 1 and col == size):
        return True
    if col == size:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, size + 1): 

        if valid_grid(grid, row, col, num):

            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False






import itertools
# grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1], 250030901
#         [0, 1, 0, 0, 0, 4, 0, 0, 0], 010004000
#     [4, 0, 7, 0, 0, 0, 2, 0, 8], 407000208
#     [0, 0, 5, 2, 0, 0, 0, 0, 0], 005200000
#     [0, 0, 0, 0, 9, 8, 1, 0, 0],  00981000
#     [0, 4, 0, 0, 0, 3, 0, 0, 0], 004003000
#     [0, 0, 0, 3, 6, 0, 0, 7, 2], 000360072
#     [0, 7, 0, 0, 0, 0, 0, 0, 3], 070000003
#     [9, 0, 3, 0, 0, 0, 6, 0, 4]] 903000604
grid = np.zeros((9, 9), dtype=int)
# make a interface for the user to enter the values
# for i, j in itertools.product(range(9), range(9)):
#     grid[i][j] = int(input("Enter the element: "))
#     # print the grid
#     print(grid)

sudoku = input("Enter the sudoku: ")
sudoku = sudoku.split()
print(sudoku)
for i in range(9):
    for k, j in enumerate(sudoku[i]):
        # print(f"sudoku{i}{sudoku[i]}")
        # print(f"j:{int(j)}")
        grid[i][k] = int(j)
        # print(f"grid:{grid[k][i]}")
print(grid)
if (Suduko(grid, 0, 0)):
    print_grid(grid)
else:
    print("Solution does not exist:(")