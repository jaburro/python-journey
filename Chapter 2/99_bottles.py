currBottles = 99

for b in range(99):
    if currBottles > 1:
        print(f"{format(currBottles)} bottles of beer on the wall.")
        print(f"{format(currBottles)} bottles of beer.")
        print("Take one down, pass it around.")
        currBottles = currBottles - 1
    else:
        print(f"{format(currBottles)} bottle of beer on the wall.")
        print(f"{format(currBottles)} bottle of beer.")
        print("Take it down, and pass it around. \nNo more bottles of beer on the wall.")

