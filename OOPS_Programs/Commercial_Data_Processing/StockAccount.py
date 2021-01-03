import json
import random

class StockAccount:
    def __init__(self,filePath,totalAmount):
        self.filePath=filePath
        self.totalAmount = totalAmount

    def valueOf(self):
        return self.totalAmount

    def buy(self,amount,symbol):
        self.updateTransaction(amount,symbol,True) #True denotes buy

    def sell(self,amount,symbol):
        self.updateTransaction(amount,symbol,False) #False denotes sell
        
    def printReport(self):
        completeData = json.loads(open(self.filePath,'r'))
        print(completeData)

    def updateTransaction(self,amount,symbol,buyOrSell):
        updated = False
        data = dict(json.load(open(self.filePath,'r')))
        if buyOrSell:
            for share in data.items():
                if(share[1]['symbol'] == symbol):
                    cost = int(share[1]['price'])*amount
                    if cost >= self.totalAmount:
                        print("Not enough money")
                    else:
                        newAmount = int(share[1]['count'])+amount
                        share[1]['count'] = str(newAmount)
                        updated = True
                        self.totalAmount -= cost
            json.dump(data, open(self.filePath,'w'), indent=3)
        else:
            for share in data.items():
                if(share[1]['symbol'] == symbol and int(share[1]['count'])>amount):
                    cost = int(share[1]['price'])*amount
                    newAmount = int(share[1]['count'])-amount
                    share[1]['count'] = str(newAmount)
                    self.totalAmount += cost
            json.dump(data, open(self.filePath,'w'), indent=3)

if __name__ == "__main__":
    stockAccount = StockAccount("StocksAccount.json",1000)
    stockAccount.buy(2,"B")
    print(stockAccount.totalAmount)
    stockAccount.sell(2,"A")
    print(stockAccount.totalAmount)