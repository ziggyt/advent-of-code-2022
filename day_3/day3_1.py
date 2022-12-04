import string

priority_dict = {}
res = []
sum = 0

alphabet = list(string.ascii_lowercase)
alphabet.extend(list(string.ascii_uppercase))

for i, char in enumerate(alphabet, 1):
    priority_dict.update({char: i})

with open("puzzle_input_3.txt", "r") as file:
    for rucksack in file:
        first_compartment = rucksack[:(len(rucksack) // 2)]
        second_compartment = rucksack[(len(rucksack) // 2):]

        for item in first_compartment:
            if item in second_compartment:
                res.append(item)
                break

for item in res:
    sum += priority_dict.get(item)

print(priority_dict)
print(res)
print(sum)
