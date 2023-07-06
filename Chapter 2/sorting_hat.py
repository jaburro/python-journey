#Variables
Gryffindor = 0
Ravenclaw = 0 
Hufflepuff = 0
Slytherin = 0

#Functions
print("Please type the number of your selection for the following questions.")

q1 = int(input("Do you like Dawn or Dusk?" + "\n1) Dawn" + "\n2) Dusk\n"))

if q1 == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif q1 == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print("Wrong Input")

q2 = int(input("When I'm Dead, I want people to remember me as:" + "\n1) The Good" + 
               "\n2) The Great" + "\n3) The Wise" + "\n4) The Bold\n"))

if q2 == 1:
    Hufflepuff += 2
elif q2 == 2:
    Slytherin += 2
elif q2 == 3:
    Ravenclaw += 2
elif q2 == 4:
    Gryffindor += 2
else:
    print("Wrong Input")

q3 = int(input("Which kind of instrument most pleases your ear?" +
               "\n1) The violin" +
               "\n2) The trumpet" +
               "\n3) The piano" +
               "\n4) The drum\n"))

if q3 == 1:
    Slytherin += 4
elif q3 == 2:
    Hufflepuff += 4
elif q3 == 3:
    Ravenclaw += 4
elif q3 == 4:
    Gryffindor += 4
else:
    print("Wrong Input")

if Gryffindor >= Slytherin and Gryffindor >= Ravenclaw and Gryffindor >= Hufflepuff:
    print("Gryffindor was the house with the most points {}! ".format(Gryffindor))
elif Slytherin >= Gryffindor and Slytherin >= Ravenclaw and Slytherin >= Hufflepuff:
    print("Slytherin was the house with the most points {}! ".format(Slytherin))
elif Ravenclaw >= Gryffindor and Ravenclaw >= Slytherin and Ravenclaw >= Hufflepuff:
    print("Ravenclaw was the house with the most points {}! ".format(Ravenclaw))
elif Hufflepuff >= Gryffindor and Hufflepuff >= Slytherin and Hufflepuff >= Ravenclaw:
    print("Hufflepuff was the house with the most points {}! ".format(Hufflepuff))
else:
    print("There has been a horrible error in my calculations |>.<| ")