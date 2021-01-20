def print_board(bo):
    for row in range(len(bo)):
        if row % 3 == 0 and row != 0:
            for i in (range(len(bo)+3)):
                print('- ', end='')
            print('')
        for col in range(len(bo[0])):
            if col % 3 == 0 and col != 0:
                print(' | ', end='')
                print(str(bo[row][col]) + " ", end='')
            else:
                print(str(bo[row][col]) + " ", end='')
        print('')

def solve(bo):
    # need to check if a number (1-9) can be slotted there
    # each row, col and 3x3 sections must contain unique numbers and all these conditions must be satisfied together
    # base case: once the board is full, all the slots have been filled and the algorithm has come to a soln

    available = find_empty(bo)
    if not available:
        return True
    else:
        row, col = available

    # take the empty slot returned from find_empty
    for i in range(1,10):
        if is_possible(bo, i, row, col):
            bo[row][col] = i
            # try to solve board with new update
            if solve(bo):
                return True

        # need to reset the current slot because no values are possible and proceed to backtrack
        bo[row][col] = 0
    # cannot solve
    return False

def find_empty(bo):
    for row in range(len(bo)):
        for col in range(len(bo[0])):
            if bo[row][col] == 0:
                return [row, col]
    return None

# return a boolean if the number can be slotted there or not
def is_possible(bo, num, row, col):
    col_list = []
    for i in bo:
        col_list.append(i[col])

    # check if num in row is valid
    if num in bo[row]:
        return False

    #check if num in col is valid
    if num in col_list:
        return False

    # check if it is in the 3x3 section
    # first we need to determine which section we are in
    # can divide the boxes into 9 diff boxes which start from 0,0 to 2,2 being at the far right bottom box

    # example: 
    # 0,0 | 0,1 | 0,2
    # 1,0 | 1,1 | 1,2
    # 2,0 | 2,1 | 2,2

    # can use integer division to determine what section you are in and then find the index
    box_x = (row // 3) * 3
    box_y = (col // 3) * 3

    # box_x and box_y gives us the section boxes, and to get to each individual box, multiply by 3
    for i in range(box_x, box_x + 3):
        for j in range(box_y, box_y + 3):
            if num == bo[i][j]:
                return False
    return True
           
def main():

    # below is an example question challenge 1 from Sudoku Solver under 'not fun' difficulty
    board = [
                [0,2,0,0,0,0,0,0,0],
                [0,0,0,6,0,0,0,0,3],
                [0,7,4,0,8,0,0,0,0],
                [0,0,0,0,0,3,0,0,2],
                [0,8,0,0,4,0,0,1,0],
                [6,0,0,5,0,0,0,0,0],
                [0,0,0,0,1,0,7,8,0],
                [5,0,0,0,0,9,0,0,0],
                [0,0,0,0,0,0,0,4,0]
            ]

    print_board(board)
    solve(board)
    print('*************************')
    print_board(board)

if __name__=="__main__":
    main()