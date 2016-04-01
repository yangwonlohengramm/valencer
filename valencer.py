from random import randrange
elements = ["Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ag", "Cd", "Sn", "Au", "Hg", "Pb"]
valences = [[3, 2], [2, 4], [3, 2], [2, 3], [2, 3], [2, 1], [2], [1], [2], [4, 2], [3, 1], [2, 1], [2, 4]]
print("*Hint*: Type \"QUIT\" and press enter to quit when prompted for an answer.\n\n==============================\n")
print("*Hint*: Type \"SKIP\" and press enter when you don't know the answer.\n\n==============================\n")
right = 0
wrong = 0
while True:
    idx = randrange(len(elements))
    print("What is/are the valence(s) of the element", elements[idx]+"?")
    ans = input().lower()
    if len(valences[idx]) == 1:
        compare = str(valences[idx][0])
    else:
        compare = " ".join(list(map(str, list(valences[idx]))))
    if ans == compare:
        print("You got it!")
        right += 1
    elif ans == "skip":
        print(elements[idx]+":", " ".join(list(map(str, list(valences[idx])))))
        print("You'll get it next time!")
        wrong += 1
    elif ans == "quit":
        break
    else:
        print(elements[idx]+":", " ".join(list(map(str, list(valences[idx]))))+".")
        print("Good try!")
        wrong += 1
    print("CURRENT PERCENTILE: %20s" % str(round(right/(right+wrong)*100, 2))+"%")
    print("\n==============================")
print("\n\n==============================\nRemember that \"ous\" means less positive and \"ic\" means more positive!")
print("\n\n==============================\n")
print("TOTAL PERCENTILE: %20s" % str(round(right/(right+wrong)*100, 2))+"%")
