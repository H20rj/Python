

answerDict: dict[int, str] = {}
string = input("Enter a list of answers:\n").replace(" ", "")
iterations = 0
run = True
for letter in string: # create dictionary
    iterations += 1
    answerDict[iterations] = letter
iterations = 1

while run:
    jump_to: str = input("Enter a question number to jump to (q to exit, enter for next): ")
    if jump_to.isdigit():
        print(f"{jump_to}: {answerDict[int(jump_to)]}")
        iterations = int(jump_to) + 1
    elif jump_to == "q":
        run = False
    elif not jump_to.isdigit() and not jump_to == "":
        print("Invalid input")

    else:
        if iterations > len(answerDict):
            print("No more answers")
            run = False
        else:
            print(f"{iterations}: {answerDict[iterations]}")
            iterations += 1