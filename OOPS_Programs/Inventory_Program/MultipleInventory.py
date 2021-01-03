
#2 classes i) InventoryFactory , ii) InventoryManager
import json

class InventoryFactory:
    filePath = ""
    outputFile = ""
    def __init__(self, file,outputFile):
        self.filePath = file
        self.outputFile = outputFile

    # openFile function opens the json file and converts the json object into dictionary
    def openFile(self): 
        try:
            f = open(self.filePath)
            data = dict(json.load(f))
            print("Opened file successfully")
        except FileNotFoundError:
            print("File does not exists.")
            
        return data

    # calulation function calculates the total of each items and returns updated dictionary with total price key-value pair
    def calculation(self, data): # data represents dictionary
        for sub in data.values():
            for key, ele in sub.items():
                result = ele['price_per_kg'] * ele['weight']
                print("Total price of", key , "is", result)
                ele['TotalPrice'] = result
        newData = json.dumps(data,indent=4, sort_keys=True) # converts dictionary data to JSON formatted string
        print(newData)
        print("Total Price of each items is calculated.")
        return newData

    def createNewFile(self,newDetails):
        try:
            with open(self.outputFile,"w") as outfile:
                outfile.write(newDetails)
                print("New File is created.")
        except IOError:
            print("IOError occured during creation of new file.")

class InventoryManager:
    def manage(self):
        inventory1=InventoryFactory(file="data1.json",outputFile="output1.json")
        inventory2=InventoryFactory(file="data2.json",outputFile="output2.json")
        inventory3=InventoryFactory(file="data3.json",outputFile="output3.json")
        data1 = inventory1.openFile()
        newData1 = inventory1.calculation(data1)
        inventory1.createNewFile(newDetails = newData1)
        data2 = inventory2.openFile()
        newData2 = inventory2.calculation(data2)
        inventory2.createNewFile(newDetails = newData2)
        data3 = inventory3.openFile()
        newData3 = inventory3.calculation(data3)
        inventory3.createNewFile(newDetails = newData3)


inventoryMananger=InventoryManager()
inventoryMananger.manage()