"""
Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

island_counter(islands) # returns 4
"""
# vertices: 1s
# edges: 1s connected N/S/E/W
# connected components: islands


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def get_neighbors(row, col, island_matrix):
    neighbors = []
    # check the neighbor above
    if row > 0 and island_matrix[row-1][col] == 1:
        neighbors.append((row-1, col))
    # check the neighbor below
    if row < len(island_matrix) - 1 and island_matrix[row+1][col] == 1:
        neighbors.append((row+1, col))
    # check the neighbor left
    if col > 0 and island_matrix[row][col-1] == 1:
        neighbors.append((row, col-1))
    # check the neighbor right
    if col < len(island_matrix[row]) - 1 and island_matrix[row][col+1] == 1:
        neighbors.append((row, col+1))
    return neighbors


def dft(starting_row, starting_col, island_matrix, visited):
    # create an empty stack
    stack = Stack()
    # push the starting row and col onto the stack
    stack.push((starting_row, starting_col))
    # while stack isn't empty
    while stack.size() > 0:
        # pop current row and rol off the stack
        row, col = stack.pop()
        # if current row and col NOT visited
        if visited[row][col] is False:
            # set the current row and col as visited
            visited[row][col] = True
            # get the neighbor rows and columns
            for neighbor in get_neighbors(row, col, island_matrix):
                # push them onto the stack
                stack.push(neighbor)


def island_counter(island_matrix):
    island_count = 0
    # keep track of all visited vertices (shared with island counter and dft)
    visited_matrix = []
    # visited_matrix will be a copy of island_matrix filled with False values
    for i in range(len(island_matrix)):
        visited_matrix.append([False] * len(island_matrix[0]))

    # walk through each cell of the matrix
    for row in range(len(island_matrix)):
        for col in range(len(island_matrix[row])):
            # if a cell value is 1 and has not been visited, that's the start of an island
            if island_matrix[row][col] == 1 and visited_matrix[row][col] is False:
                # traverse the connected component (graph)
                # dft starting at the current cell
                dft(row, col, island_matrix, visited_matrix)
                # once we are done traversing, that means we have found a new island
                # increment some island_count value
                island_count += 1
    return island_count


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

print(island_counter(islands))
