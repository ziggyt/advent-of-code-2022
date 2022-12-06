stacks = []
for i in range(9):
    stacks.append([])


def init_state():
    with open("input", "r") as file:
        contents = file.readlines()[:9]
        stack_order_index = contents.pop()
        for move in contents:
            for i, char in enumerate(move):
                char: str
                if (char.isalpha()):
                    stack_num = int(stack_order_index[i]) - 1

                    # print(f"Appending {char} to stack {stack_num}")
                    stacks[stack_num].append(char)

        for stack in stacks:
            stack.reverse()

        file.close()


init_state()

print(stacks)

with open("input", "r") as file:
    for move in file.readlines()[9:]:
        if move[0] != 'm':
            continue

        info = ''.join(filter(str.isdigit, move))

        if len(info) == 3:
            n_crates = int(info[0])
            from_info = int(info[1]) - 1
            to_info = int(info[2]) - 1

        else:
            n_crates = int(info[:2])
            from_info = int(info[2]) - 1
            to_info = int(info[3]) - 1

        for i in range(n_crates):
            # print(f"Appending {n_crates-i} from {from_info} to stack {to_info} ")
            # print(stacks[from_info], stacks[to_info])
            stacks[to_info].append(stacks[from_info].pop())

    res = ''

    for stack in stacks:
        res += stack.pop()

    print(res)
