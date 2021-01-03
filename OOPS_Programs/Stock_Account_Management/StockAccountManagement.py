import json
class Stock:

    def __init__(self,name,price,count):
        self.shareName = name
        self.sharePrice = price
        self.shareCount = count

    def getTotalStockValue(self):
        return self.shareCount * self.sharePrice


class StockManager:

    def __init__(self):
        self.filePath = "Stocks.json"

    def calculateValueOfStocks(self):
        totalCost = 0
        f = open(self.filePath)
        data = dict(json.load(f))
        print(data)
        for stockJson in data.items():
            print(stockJson)
            name = stockJson[1]["name"]
            price = int(stockJson[1]["price"])
            count = int(stockJson[1]["count"])
            stock = Stock(name,price,count)
            totalCostOfThisStock = stock.getTotalStockValue()
            totalCost += totalCostOfThisStock
        return totalCost

if __name__ == "__main__":
    stockManager = StockManager()
    print(stockManager.calculateValueOfStocks())