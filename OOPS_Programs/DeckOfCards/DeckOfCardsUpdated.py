import random
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
# A class to represent a queue 
  
# The queue, front stores the front node 
# of LL and rear stores the last node of LL 
class Queue: 
      
    def __init__(self): 
        self.front = self.rear = None
  
    def isEmpty(self): 
        return self.front == None
      
    # Method to add an item to the queue 
    def EnQueue(self, item): 
        temp = Node(item) 
          
        if self.rear == None: 
            self.front = self.rear = temp 
            return
        self.rear.next = temp 
        self.rear = temp 
  
    # Method to remove an item from queue 
    def DeQueue(self): 
          
        if self.isEmpty(): 
            return
        temp = self.front 
        self.front = temp.next
  
        if(self.front == None): 
            self.rear = None
class Player:
    def __init__(self):
        self.queue = Queue()

    def setupQueueCards(self,cards):
        for card in cards:
            self.queue.EnQueue(card)

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
        return player_cards

noOfPlayers = int(input("Enter the number of players: "))
noOfCardsForEachPlayer = int(input("Enter the numbers of cards to be distributed to each player: "))
if noOfCardsForEachPlayer*noOfPlayers > 52 :
    print("Less player or Cards to be distributed to each player")
    exit(1)
cards=Cards(noOfCardsForEachPlayer,noOfPlayers)
playerCards=  cards.divideCards()
playerQueue = Queue()
for playerArr in playerCards:
    player=Player()
    player.setupQueueCards(playerArr)
    playerQueue.EnQueue(player)
node = playerQueue.front
while node.next != None:
    print(node.data.queue.front.data,end=" ")
    node = node.next

print("Completed")
