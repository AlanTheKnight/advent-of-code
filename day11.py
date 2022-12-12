from __future__ import annotations
from math import floor, lcm


PART2_MODE = True


with open("input/day11.input.txt", "r") as f:
    puzzle = f.readlines()


monkeys: list[Monkey] = []


class Monkey:
    def __init__(self, n: int, items: list[int], op: str, test: int, throw: tuple[int, int]) -> None:
        self.n = n
        self.items = items
        self.op = op
        self.test = test
        self.throw = throw
        self.inspections = 0

    def take(self, item: int):
        self.items.append(item)

    def inspect(self, limiter: int):
        while self.items:
            self.inspections += 1
            item = eval(self.op, {"old": self.items.pop(0)})
            if not PART2_MODE:
                item = floor(item / 3)
            elif item > limiter:
                item %= limiter
            monkeys[self.throw[(0 if item % self.test == 0 else 1)]].take(item)


for l in range(0, len(puzzle), 7):
    d = puzzle[l:l+6]
    monkeys.append(Monkey(
        d[0].strip("\n :").split()[1],
        list(map(int, d[1].strip("\n")[18:].split(", "))),
        d[2].strip("\n")[19:],
        int(d[3].split()[-1]),
        (int(d[4].split()[-1]), int(d[5].split()[-1])),
    ))


limiter = lcm(*[m.test for m in monkeys])

for i in range((10000 if PART2_MODE else 20)):
    for m in monkeys:
        m.inspect(limiter)

a, b = sorted([m.inspections for m in monkeys], reverse=True)[:2]
print(a * b)
