#Here's the final project of the chapter!

# We just got back from a trip to South America, specifically Colombia, Peru, and Brazil. There's some leftover cash in:

# 🇨🇴 Colombian peso  1 = 0.000240 USD
# 🇵🇪 Peruvian soles 1 = 0.28 USD
# 🇧🇷 Brazilian reais 1 = 0.21 USD
# Create a currency.py program that asks the user for the amount they have in peso, soles, and reais and calculates the total in USD.

# Make sure to Google the current exchange rates!

userIOp = 0
userIOs = 0
userIOr = 0



totCur = 0.0

userIOp = float(input("How many Peso's do you have left?:  "))
userIOs = float(input("How many Soles do you have left?:  "))
userIOr = float(input("How many Reais do you have left?:  "))

cPeso = userIOp * .000240
cSoles = userIOs * .28
cReais = userIOr * .21

totCur = cPeso + cSoles + cReais
totCur
print(f"You have {totCur:.2f} left in USD")