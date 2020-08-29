import random

correct = 0
wrong = 0

while True:
    print("")

    print("1) heads")
    print("2) tails")
    botChose = input("Choose: ")
    coinFlip = random.randint(0,1)

    print("")
    print("==============================================")
    print("")

    if botChose == "1":
        print("You chose: heads")
    elif botChose == "2":
        print("You chose: tails")
    else:
        print("INVALID")
        
    print("")

    if coinFlip == 0:
        print("Coin flipped: heads")
    elif coinFlip == 1:
        print("Coin flipped: tails")

    print("")

    if coinFlip == 0 and botChose == "1":
        print("You chose right!")
        correct += 1
    elif coinFlip == 1 and botChose == "2":
        print("You chose right!")
        correct += 1
    elif coinFlip == 0 and botChose == "2" or coinFlip == 1 and botChose == "1":
        print("You chose wrong!")
        wrong += 1
    else:
        print("Didn't choose anything.")
        
    print("")
    print("==============================================")

    print("Correct: " + str(correct))
    print("Wrong:   " + str(wrong))
    print("Total:   " + str(correct + wrong))



