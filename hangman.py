wort = "Polarexpress"
lives = 6
won = False

fortschritt = [False] * len(wort)

while not won:
    buchstaben = input("Buchstabe: ").lower()

    for i in range(len(wort)):
        if wort[i].lower() == buchstaben:
            fortschritt[i] = True
    if False in fortschritt:
        output = ""
        for i in range(len(wort)):
            if fortschritt[i] == True:
                output += wort[i]
            else:
                output += "_"
        print(output)
        print("Lives: " + str(lives))
    else:
        print("You won!")
        won = True
wort = "Polarexpress"
lives = 6
ended = False

fortschritt = [False] * len(wort)

while not ended:
    buchstaben = input("Buchstabe: ").lower()
    erraten = False
    for i in range(len(wort)):
        if wort[i].lower() == buchstaben:
            fortschritt[i] = True
            erraten = True
    if False in fortschritt:
        output = ""
        for i in range(len(wort)):
            if fortschritt[i] == True: #hier ist ein kommentar
                output += wort[i]
            else:
                output += "_"
        print(output)
        if erraten == False:
            lives -= 1
        if lives <= 0:
            print("You lost! The word was: " + wort)
            ended = True
        else:
            print(f"Lives: {lives}")
    else:
        print("You won!")
        ended = True