# storing the password in a variable named password with init value password
password = "class"
# create a variable named userInput with init value " ", 0
userInput = ""
# create variable named Edame with init value
Edame = True
# create the sentry variable
i = 0
# while loop for asking the user guess and store it in variable userInput
while Edame:
    userInput = input("Kalamaye obor ra vared konid? : ")
    if userInput == password and i < 2:
        print("success")
        Edame = False
    elif userInput != password and i < 2 :
        print("Again")
        i = i + 1
    elif userInput != password and i ==2 :
        print("your out of guesses ! goodbye ")
        Edame = False
