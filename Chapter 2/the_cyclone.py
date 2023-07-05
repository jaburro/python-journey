minHeight = 120
tokens = 10
tooShort = f"We are sorry, but you must be atleast {minHeight}cm to ride this ride."
needTokens = f"We are sorry, but you must have atleast {tokens} to ride this ride."



getHeight = int(input("How tall are you in Centimeters?"))
getTokens = int(input("How many tokens do you currently have?"))

if getHeight < minHeight:
    print(tooShort)


if getTokens < tokens:
    print(needTokens)


if getHeight >= minHeight and getTokens >= tokens:
    print("You are tall enough and have enough tokens for the ride.  Please insert tokens and wait for further instruction.  Enjoy your ride!")
