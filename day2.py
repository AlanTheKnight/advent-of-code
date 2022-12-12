def win(op):
    if op == "A":
        return "Y"
    if op == "B":
        return "Z"
    return "X"


def lose(op):
    if op == "A":
        return "Z"
    if op == "B":
        return "X"
    return "Y"


def draw(op):
    if op == "A":
        return "X"
    if op == "B":
        return "Y"
    return "Z"


move_score = {"X": 1, "Y": 2, "Z": 3}

round_score = {
    ("A", "X"): 3,
    ("A", "Y"): 6,
    ("A", "Z"): 0,
    ("B", "X"): 0,
    ("B", "Y"): 3,
    ("B", "Z"): 6,
    ("C", "X"): 6,
    ("C", "Y"): 0,
    ("C", "Z"): 3,
}

moves = []
with open("day2.input.txt", "r") as f:
    for line in f.readlines():
        moves.append(tuple(line.split()))

my_score = 0
for op, cur in moves:
    if cur == "X":
        my_move = lose(op)
    elif cur == "Y":
        my_move = draw(op)
    else:
        my_move = win(op)
    my_score += round_score[(op, my_move)] + move_score[my_move]

print(my_score)
