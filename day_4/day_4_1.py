def contains_range(min_x, max_x, min_y, max_y):
    return 1 if (min_x <= min_y <= max_y <= max_x or min_y <= min_x <= max_x <= max_y) else 0

sum = 0
with open("input", "r") as file:
    for pair in file.readlines():
        elf_1, elf_2 = pair.split(',')

        a = int(elf_1.split('-')[0])
        b = int(elf_1.split('-')[1])
        c = int(elf_2.split('-')[0])
        d = int(elf_2.split('-')[1])

        res = contains_range(a, b, c, d)

        sum += res

print(sum)
