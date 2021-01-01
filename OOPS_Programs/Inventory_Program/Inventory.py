#Program to Calculate the total Price of each items from data.json
import json

class Inventory:
    filePath = ""
    def __init__(self, file):
        self.filePath = file

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
        newData = json.dumps(data) # converts dictionary data to JSON formatted string
        print(newData)
        print("Total Price of each items is calculated.")
        return newData

    # creates new JSON file from the Dictionary
    def createNewFile(self,newDetails):
        try:
            with open("/Users/kajol7052/Desktop/OOPS_PROGRAMS/output1.json", "w") as outfile:
                outfile.write(newDetails)
                print("New File is created.")
        except IOError:
            print("IOError occured during creation of new file.")
            

if __name__ == "__main__":
    path = '/Users/kajol7052/Desktop/OOPS_PROGRAMS/data.json'
    stock = Inventory(path) # object instantiated
    try:
        data = stock.openFile() # function call to open json file
        newData = stock.calculation(data = data) # function call to calculate total price of each items
    except Exception:
        print("Exception Occured")
    stock.createNewFile(newDetails = newData) # functiona call to create new json file