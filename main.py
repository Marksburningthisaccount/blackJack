import random

playerHand = random.randint(1,10) + random.randint(1,10) #makes two hands equal to 2 randomly drawn camakes two hands equal to 2 randomly drawn cards
dealerHand = random.randint(1,10) + random.randint(1,10)
print(dealerHand)
while dealerHand < 17: #keeps adding a card to dealer while dealer is under 17
    dealerHand =+ random.randint(1,10)
    print(dealerHand)

gameCondition = 2

if dealerHand > 21:
    print("you win")
    gameCondition = 0

elif dealerHand == 21:
    print("you lose")
    gameCondition = 1

if gameCondition > 1:
    print(f"your current hand value is: {playerHand}")

    hitOrStand = input("hit or stand")

    while hitOrStand == ('hit'):
        playerHand =+ random.randint(1,10)
        