with open("input/day10.test.input.txt", "r") as f:
    data = f.readlines()

ans, cycle, x = 0, 0, 1


def do_clock():
    global ans, cycle, x
    print(end="##" if -1 <= cycle % 40-x <= 1 else "  ")
    cycle += 1
    if cycle % 40 == 20:
        ans += x*cycle
    if cycle % 40 == 0:
        print()


for line in data:
    if "noop" in line:
        do_clock()
    else:
        do_clock()
        do_clock()
        x += int(line.split()[1])
print(ans)
