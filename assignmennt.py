maze = [['.','.','.','.'],
['.','x','x','x'],
['.','.','.','x'],
['x','x','.','.']]

# functions to print maze
def print_maze(maze):
    for row in maze:
        # variable to print the line
        output = ''
        for element in row:
            output += element + ' '
        print (output)


# funnction for client
def maze_solution(maze):
    # Helper Function to execute and figure out the solution
    return maze_solution_helper(maze, [], 0, 0)

# helper function
def maze_solution_helper(maze, sol, row, col):
    # 3 Base Case
    # Case 1: Exit Path is found
    row_end = len(maze)
    col_end = len(maze[0])
    if row == row_end - 1 and col == col_end - 1:
        return sol
    
    # Case 2: Maze is out of the bounnd
    if row >= row_end or col >= col_end:
        return None

    # Case 3: Maze is at x spot
    if maze[row][col] == 'x':
        return None

    # Maze is moving to the right
    sol.append('r')
    sol_right = maze_solution_helper(maze, sol, row, col + 1)
    if sol_right is not None:
        return sol_right

    # pop the solution if right does not work
    sol.pop()

    # Maze is moving to the bottom
    sol.append('d')
    sol_down = maze_solution_helper(maze, sol, row + 1, col)
    if sol_down is not None:
        return sol_down

    # if no solution 
    sol.pop()
    return None


print_maze(maze)
print(maze_solution(maze))