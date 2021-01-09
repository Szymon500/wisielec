import random
def hangman(word):
        wrong = 0
        stages = ["",
                  "_","_","_","_","_      ",
                  "|          ",
                  "|    |     ",
                  "|    0     ",
                  "|   /|\    ",
                  "|   / \    ",
                  "|          "
                  ]
        rleters = list(word)
        board = ["_"] * len(word)
        win = False
        print("Gra w wisielca")
        while wrong < len(stages)-1:
                print("\n")
                msg = "Podaj litere:"
                char = input(msg)
                if char in rleters:
                        cind = rleters.index(char)
                        board[cind] = char
                        rleters[cind] = '$'
                else:
                        wrong += 1

                print((" ".join(board)))
                e = wrong +1
                print("\n".join(stages[0:e]))
                if "_" not in board:
                        print("Wygrałes!")
                        print(" ".join(board))
                        win =True
                        break
        if not win:
                print("\n".join(stages[0:wrong]))
                print("Przegrałes!Mailes odgadnac: {}.".format(word))

list1 = ["Poddawany","Slaby","zjeb","nerd","zycie"]

hangman(list1[random.randint(0,3)])

                
