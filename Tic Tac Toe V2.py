import random
import time
my_border = ["_", "_", "_",
             "_", "_", "_",
             "_", "_", "_"]


def printBord():
    for num in range(9):
        if num in [3, 6]:
            print()
        print(my_border[num], " ", end="")
    print()


numTakaen = []


def winar():
    if my_border[0] == my_border[1] == my_border[2] != '_':
        print(f"{my_border[0]} is the winar")
        return True
    elif my_border[3] == my_border[4] == my_border[5] != '_':
        print(f"{my_border[3]} is the winar")
        return True
    elif my_border[6] == my_border[7] == my_border[8] != '_':
        print(f"{my_border[6]} is the winar")
        return True
    elif my_border[0] == my_border[3] == my_border[6] != '_':
        print(f"{my_border[0]} is the winar")
        return True
    elif my_border[1] == my_border[4] == my_border[7] != '_':
        print(f"{my_border[1]} is the winar")
        return True
    elif my_border[2] == my_border[5] == my_border[8] != '_':
        print(f"{my_border[2]} is the winar")
        return True
    elif my_border[0] == my_border[4] == my_border[8] != '_':
        print(f"{my_border[0]} is the winar")
        return True
    elif my_border[2] == my_border[4] == my_border[6] != '_':
        print(f"{my_border[2]} is the winar")
        return True
    else:
        return False


def tic_tok():

    printBord()
    if len(numTakaen) == 9:
        print("There is no wainer")
    else:
        while(not winar()):
            print()
            xinput = int(input("X :"))
            while(xinput in numTakaen):
                print("This number Takean")
                xinput = int(input("X :"))
            else:
                numTakaen.append(xinput)
                my_border[xinput - 1] = "X"
                printBord()

            if winar():
                break
            if len(numTakaen) == 9:
                print("There is no wainer")
                break
            time.sleep(.5)
            print()
            oinput = random.randint(1, 9)
            while(oinput in numTakaen):
                # print("This number Takean")
                oinput = random.randint(1, 9)
            else:
                numTakaen.append(oinput)
                my_border[oinput - 1] = "O"
                printBord()


print("="*30)
tic_tok()
print("="*30)
