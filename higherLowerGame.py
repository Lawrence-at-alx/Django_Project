import random

#card constant 
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
NCARDS = 8

#get a card deck and return a random card
def getRandomCard(cardDeck):
    cardPicked = cardDeck.pop()
    return cardPicked

#get a shuffled copy of card deck
def getShuffledCopy(cardDeck):
    cardDeckCopy = cardDeck.copy()
    shuffledResult = random.sample(cardDeckCopy)
    return shuffledResult

#Main Game 
print("Welcome to Higher or Lower")
print("You have to choose whether the next card to be shown will be higher or lower than the current card.")
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start.')
print()

#turn the tuple into list of dictionaries
cardDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        #create a card dictionaries template
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue +1}
        cardDeckList.append(cardDict)

score = 50

while True: #play game multiple time
    #now cardDeckList = cardDeck
    shuffledList = getShuffledCopy(cardDeckList)
    currentCardDict = getRandomCard(cardDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardSuit = currentCardDict['suit']
    currentCardValue = currentCardDict['value']
    print("First card is:", currentCardRank + "of" + currentCardSuit)
    print()

    #play game 8 times
    for cardNumber in range(0, NCARDS):
        answer = input('Will the card number be Higher or Lower than the' + currentCardRank + 'of ' + currentCardSuit + 
        '? (Enter h  or l):')
        answer = answer.casefold()

        nextCardDict = getRandomCard(cardDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print("next card is:", nextCardRank + "of" + nextCardSuit)

        if answer == 'h':
            if currentCardValue< nextCardValue:
                print("You got it right, it was higher ")
                score = score + 20
            else:
                print("sorry, it was lower")
                score = score - 15
        elif answer == 'l':
            if currentCardValue > nextCardValue:
                print("You got it right, it was lower")
                score = score + 20
            else:
                print("sorry, it was higher")
                score = score - 15
        print("Your score is:{}" .format(score))
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue

        #play again
        goAgain = input('To go again press ENTER, or "q" to quit')
        
        if goAgain == 'q':
            break

    print("OK, bye")
