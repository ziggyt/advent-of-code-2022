rock_other, rock_me = "A", "X"
paper_other, paper_me = "B", "Y"
scissors_other, scissors_me = "C", "Z"



res_other = 0
res_me = 0

with open("puzzle_input_2_1.txt", "r") as file:
    for round in file:
        if round[0] == rock_other:
            res_other += 1  # !
            if round[2] == paper_me:
                res_me += (2 + 6)
            elif round[2] == rock_me:
                res_me += (1 + 3)
                res_other += 3
            else:
                res_me += 3
                res_other += 6

        if round[0] == paper_other:
            res_other += 2
            if round[2] == paper_me:
                res_me += 2

                res_me += 3
                res_other += 3

            elif round[2] == rock_me:
                res_me += 1
                res_other += 6
            else:
                res_me += 3

                res_me += 6

        if round[0] == scissors_other:
            res_other += 3
            if round[2] == paper_me:
                res_me += 2

                res_other += 6

            elif round[2] == rock_me:
                res_me += 1
                res_me += 6
            else:
                res_me += 3

                res_me += 3
                res_other += 3

class RoundChoices:
    rock, lose = "A", "X"
    paper, draw = "B", "Y"
    scissors, win = "C", "Z"


with open("puzzle_input_2_1.txt", "r") as file:
    for round in file:

        match round[0]:
            case RoundChoices.rock:
                match round[2]:
                    case RoundChoices.lose:
                        res_me += 3

                    case RoundChoices.draw:
                        res_me += 3
                        res_me += 1

                    case RoundChoices.win:
                        res_me += 6
                        res_me += 2


            case RoundChoices.paper:
                match round[2]:
                    case RoundChoices.lose:
                        res_me += 1

                    case RoundChoices.draw:
                        res_me += 3
                        res_me += 2

                    case RoundChoices.win:
                        res_me += 6
                        res_me += 3

            case RoundChoices.scissors:
                match round[2]:
                    case RoundChoices.lose:
                        res_me += 2

                    case RoundChoices.draw:
                        res_me += 3
                        res_me += 3

                    case RoundChoices.win:
                        res_me += 6
                        res_me += 1



print(res_me, res_other)
