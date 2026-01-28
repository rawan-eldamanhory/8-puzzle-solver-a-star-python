# 8-Puzzle Solver using A* Search (Python)

This project solves the classic **8-Puzzle Problem** using the **A\*** (A-Star) informed search algorithm with the **Manhattan Distance heuristic**.

It demonstrates advanced Artificial Intelligence concepts including heuristic evaluation, priority queues, and optimal path finding.

## 🔹 Problem Description
The 8-puzzle consists of a 3×3 grid with 8 numbered tiles and one empty space.
The goal is to reach a target configuration using the minimum number of moves.

## 🔹 Algorithm Used
- A* (Informed Search)
- Manhattan Distance Heuristic
- Priority Queue (Min-Heap)

## 🔹 Features
- Optimal solution using heuristics
- Efficient state exploration
- Tracks solution path
- Measures execution time
- Uses Node-based state representation

## 🔹 Heuristic

**Manhattan Distance**:

The sum of the distances of each tile from its goal position.

## 🔹 Technologies
- Python
- A* Search Algorithm
- Heuristic Functions
- Data Structures (Heap, Set)

## 🔹 How to Run
```bash
python 8Puzzle-Astar.py
```

## 🔹 Example

Start State:

2 8 3

1 6 4

7 0 5

Goal State:

1 2 3

8 0 4

7 6 5

## 🔹 Output

Prints each step of the solution

Displays total number of moves

Shows execution time
