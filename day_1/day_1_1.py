res = []
val = 0

with open("puzzle_input_1_1.txt", "r") as file:
    for row in file:
        if row == "\n":
            res.append(val)
            val = 0
            continue
        else:
            val += int(row)

res.sort()
ans_1 = res[-1:][0]
ans_2 = sum(res[-3:])

print(f"Answer 1: {ans_1}")
print(f"Answer 2: {ans_2}")
