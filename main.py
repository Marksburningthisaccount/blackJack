import random

playerHand = random.randint(1,10) + random.randint(1,10) #makes two hands equal to 2 randomly drawn camakes two hands equal to 2 randomly drawn cards
dealerHand = random.randint(1,10) + random.randint(1,10)
print(dealerHand)
while dealerHand < 17:
    dealerHand =+ random.randint(1,10)
    print(dealerHand)
