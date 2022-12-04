import string

priority_dict = {}
sum = 0

alphabet = list(string.ascii_lowercase)
alphabet.extend(list(string.ascii_uppercase))

for i, char in enumerate(alphabet, 1):
    priority_dict.update({char: i})

with open("puzzle_input_3.txt", "r") as file:
    elf_group = []
    badge_list = []
    ctr = 0

    for rucksack in file.readlines():
        rucksack = rucksack.replace('\n', '')

        elf_group.append(rucksack)

        if len(elf_group) == 3:
            for item in elf_group[0]:
                if item in elf_group[1] and item in elf_group[2]:
                    badge_list.append(item)
                    break

            elf_group = []

    for item in badge_list:
        sum += priority_dict.get(item)

print(sum)
