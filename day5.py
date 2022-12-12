from copy import deepcopy

crates, moves, pos = [], [], []

d = {}

with open("input/day5.input.txt", "r") as f:
    for line in f.readlines():
        if not line.strip():
            continue
        if line[0] == "m":
            x = line.strip().split()[1::2]
            moves.append([int(x[0])] + x[1:])
        elif "[" in line:
            crates.append(line)
        else:
            pos = line

for i_x, x in enumerate(pos):
    if x.strip():
        d[x] = []
        for i in range(len(crates)):
            if crates[i][i_x] != " ":
                d[x].append(crates[i][i_x])


def solve_part2():
    data = deepcopy(d)
    for num, fr, to in moves:
        to_move = data[fr][:num]
        data[fr] = data[fr][num:]
        data[to] = to_move + data[to]
    ans = [val[0] for val in data.values()]
    print(*ans, sep="")


def solve_part1():
    data = deepcopy(d)
    for num, fr, to in moves:
        for _ in range(num):
            crate = data[fr].pop(0)
            data[to].insert(0, crate)
    ans = [val[0] for val in data.values()]
    print(*ans, sep="")


solve_part1()
solve_part2()
