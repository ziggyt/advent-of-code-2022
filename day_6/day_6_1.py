with open("input", "r") as file:
    contents = file.readlines()[0]
    for i in range(len(contents)):
        res = contents[i:i + 4]
        if len(set(res)) == 4:
            print(i + 4, res)
            break
