'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_sudoku(sudoku):
    if len(sudoku) == 9:
    numsinrow = 0
    for i in range(0, 9):
        if len(sudoku[i]) == 9:
            numsinrow =numsinrow + 1
    if numsinrow == 9:
        for i in range(9):
            rowoccurence = [0,0,0,0,0,0,0,0,0,0]
            for j in range(9):
                rowoccurence[sudoku[i][j]] += 1
                temprow = rowoccurence[1:10]
                if temprow == [1,1,1,1,1,1,1,1,1]:
                    return True
                else:
                    return False
    else:
        return False
else:
    return False
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    

def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()