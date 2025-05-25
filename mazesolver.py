import random

# Maze dimensions (must be odd to ensure walls)
ROWS, COLS = 11, 11

# Initialize the maze with walls (1)
maze = [[1 for _ in range(COLS)] for _ in range(ROWS)]

# Directions: Up, Down, Left, Right
dirs = [(-2, 0), (2, 0), (0, -2), (0, 2)]

def is_valid(x, y):
    return 0 <= x < ROWS and 0 <= y < COLS

# DFS-based Maze Generation
def generate_maze(x, y):
    maze[x][y] = 0
    random.shuffle(dirs)
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny) and maze[nx][ny] == 1:
            maze[x + dx // 2][y + dy // 2] = 0
            generate_maze(nx, ny)

# DFS Maze Solver
def solve_maze(x, y, end_x, end_y, path):
    if not is_valid(x, y) or maze[x][y] != 0 or (x, y) in path:
        return False
    path.append((x, y))
    if (x, y) == (end_x, end_y):
        return True
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        if solve_maze(x + dx, y + dy, end_x, end_y, path):
            return True
    path.pop()
    return False

# Start generation and solving
generate_maze(1, 1)
start = (1, 1)
end = (ROWS - 2, COLS - 2)
path = []
solve_maze(*start, *end, path)

# Display Maze
for i in range(ROWS):
    for j in range(COLS):
        if (i, j) == start:
            print("S", end=" ")
        elif (i, j) == end:
            print("E", end=" ")
        elif (i, j) in path:
            print(".", end=" ")
        else:
            print("█" if maze[i][j] == 1 else " ", end=" ")
    print()
