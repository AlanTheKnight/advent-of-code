food = []
with open("day1.input.txt", "r") as f:
    cur = []
    for line in f.readlines():
        if line != '\n':
            cur.append(int(line.strip()))
        else:
            food.append(cur)
            cur = []
    food.append(cur)


# Part 1
print(max(list(map(sum, food))))

# 67633

# Part 2
print(sum(list(sorted(list(map(sum, food)), reverse=True))[:3]))

# 199628
