import heapq

import time

class Node:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = self.depth + self.heuristic()

    def __lt__(self, other):
        return (self.cost < other.cost)

    def __eq__(self, other):
        return (self.state == other.state)

    def __hash__(self):
        return hash(str(self.state))

    def heuristic(self):
        # calculate the Manhattan distance heuristic
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    x, y = divmod(self.state[i][j]-1, 3)
                    distance += abs(x-i) + abs(y-j)
        return distance

def get_moves(state):
    moves = []
    i, j = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)
    if i > 0:
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
        moves.append(new_state)
    if i < 2:
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
        moves.append(new_state)
    if j > 0:
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
        moves.append(new_state)
    if j < 2:
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
        moves.append(new_state)
    return moves

def a_star(start_state):
    start_node = Node(start_state)
    frontier = []
    heapq.heappush(frontier, start_node)
    explored = set()

    while frontier:
        node = heapq.heappop(frontier)

        if node.state == goal_state:
            moves = []
            while node.move is not None:
                moves.append(node.move)
                node = node.parent
            moves.reverse()
            return moves

        explored.add(node)

        for move in get_moves(node.state):
            child = Node(move, parent=node, move=move, depth=node.depth+1)

            if child in explored:
                continue

            heapq.heappush(frontier, child)

    return None


start_state = [[2, 8, 3],
               [1, 6, 4],
               [7, 0, 5]]

goal_state = [[1, 2, 3],
              [8, 0, 4],
              [7, 6, 5]]

start_time = time.time()
moves = a_star(start_state)
end_time = time.time()

if moves is None:
    print("No solution found!")
else:
    print("Solution found in", len(moves), "moves:")
    for i, move in enumerate(moves):
        print("Step", i+1, ":")
        for row in move:
            print(row)
        print()

print("Time taken:", end_time - start_time, "seconds")        
