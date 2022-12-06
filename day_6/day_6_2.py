with open("input", "r") as file:
    contents = file.readlines()[0]
    for i in range(len(contents)):
        res = contents[i:i + 14]
        if len(set(res)) == 14:
            print(i + 14, res)
            break
