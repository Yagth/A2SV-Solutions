def printWinner(total, logs):
    countA = 0
    for log in logs:
        if log == 'A':
            countA += 1

    countB = total - countA

    if countA > countB:
        print("Anton")
    elif countB > countA:
        print("Dankin")
    else:
        print("Friendship")

total = int(input())
logs  = input()

printWinner(total, logs)

    