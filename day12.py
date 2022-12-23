from collections import deque
import sys


def BFS(data, start, end):
    def is_valid(pos):
        return 0 <= pos[0] < len(data) and 0 <= pos[1] < len(data[0])

    shifts = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    q = deque([(start, 0)])
    visited = set()

    while q:
        cur, dist = q.popleft()

        if cur not in visited:
            visited.add(cur)

            if cur == end:
                return dist

            for dx, dy in shifts:
                nbr = (cur[0] + dx, cur[1] + dy)
                if is_valid(nbr) and ord(data[nbr[0]][nbr[1]]) - ord(data[cur[0]][cur[1]]) <= 1:
                    q.append((nbr, dist + 1))
    return -1


def read_puzzle(test=True):
    with open(f"input/day12.{'test.' if test else ''}input.txt", "r") as f:
        data = f.readlines()
    start, end = None, None
    a_coords = []
    for row in range(len(data)):
        for col in range(0, len(data[0])):
            cur = data[row][col]
            if cur == "S":
                start = (row, col)
            elif cur == "E":
                end = (row, col)
            if cur == "a" or cur == "S":
                a_coords.append((row, col))
        data[row] = data[row].replace("E", "z").replace("S", "a").strip()
    return data, start, end, a_coords


def main():
    data, start, end, a_coords = read_puzzle(test="-t" in sys.argv)
    
    if "--pt2" in sys.argv:
        dist = [BFS(data, coord, end) for coord in a_coords]
        print(min([i for i in dist if i != -1]))
    else:
        print(BFS(data, start, end))


if __name__ == "__main__":
    main()
