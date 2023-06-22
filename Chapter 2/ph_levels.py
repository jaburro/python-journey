# create a variable called ph and ask the user for a value between 0 and 14.

ph = float(input("Please enter a number between 0 and 14:  "))

# If ph is greater than 7, output "Basic".
# If ph is less than 7, output "Acidic".
# Else, output "Neutral".

if ph > 7:
    print("Base")
elif ph < 7:
    print("Acid")
else:
    print("Neutral")