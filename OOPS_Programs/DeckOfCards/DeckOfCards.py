import random

class Cards:
    def __init__(self,cards,players):
        self.cards = cards
        self.players = players

    def divideCards(self):
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        players = []
        suitRanks = []
        for suit in suits:
            for rank in ranks:
                suitRank = rank + " of " + suit
                suitRanks.append(suitRank)
        unique = set()
        for player in range(0, self.players):
            count = 0
            player_cards = []
            while count < self.cards:
                random_card = random.randint(0, 51)
                if random_card not in unique:
                    unique.add(random_card)
                    count += 1
                    player_cards.append(suitRanks[random_card])
            players.append(player_cards)
            print(player_cards)

noOfPlayers = int(input("Enter the number of players: "))
noOfCardsForEachPlayer = int(input("Enter the numbers of cards to be distributed to each player: "))
if noOfCardsForEachPlayer*noOfPlayers > 52 :
    print("Less player or Cards to be distributed to each player")
    exit(1)
cards=Cards(noOfCardsForEachPlayer,noOfPlayers)
cards.divideCards()