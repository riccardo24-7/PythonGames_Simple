import random

game = True
computerWord = ["R", "S", "P"]
while game:
    ranNum = random.randint(0,2)
    pcAnswer = computerWord[ranNum]
    userAnswer = input("Введите: R - камень, S - ножницы, P - бумага ")
    pcAnswer = pcAnswer.upper()
    userAnswer = userAnswer.upper()
    if userAnswer not in computerWord:
        print("Incorrect input. Try again")
        continue
    winningCombin = (('R', 'P'), ('S', 'R'), ('P', 'S'))
    if (pcAnswer, userAnswer) in winningCombin:
        print("You're a winner")
    elif(pcAnswer == userAnswer):
        print("Draw")
    else:
        print("You're a loser")
    print(f"Computer answer {pcAnswer}")
    print(f"User answer {userAnswer}")

    gameContinue =input("Do you want to continue? [y/n] ")
    gameContinue = gameContinue.lower()
    if gameContinue == "n":
        game = False
        break