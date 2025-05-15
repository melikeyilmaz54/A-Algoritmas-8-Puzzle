import heapq

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_zero(state):
    for i, row in enumerate(state):
        if 0 in row:
            return i, row.index(0)

def misplaced_tiles(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                count += 1
    return count

def generate_successors(state):
    x, y = find_zero(state)
    successors = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            successors.append(new_state)
    return successors

def astar(start_state):
    heap = []
    heapq.heappush(heap, (misplaced_tiles(start_state), 0, start_state, []))  # (f, g, state, path)
    visited = set()

    while heap:
        f, g, state, path = heapq.heappop(heap)
        h = misplaced_tiles(state)
        print(f"g: {g}, h: {h}, f: {f}")
        for row in state:
            print(row)
        print("------")

        if state == goal_state:
            return path + [state]
        visited.add(tuple(map(tuple, state)))
        for succ in generate_successors(state):
            if tuple(map(tuple, succ)) not in visited:
                h_succ = misplaced_tiles(succ)
                heapq.heappush(heap, (g + 1 + h_succ, g + 1, succ, path + [state]))
    return None

start = [[1, 2, 3],
         [0, 4, 6],
         [7, 5, 8]]

solution = astar(start)

