import json
import collections

class AddressBook:
    filePath=""
    
    def setUpFile(self,fileLocation):
        self.filePath=fileLocation
        self.contactlist=collections.OrderedDict()
 #       self.contactlist = json.load(open(self.filePath,'r'))
        print("File location : ",self.filePath)
#first and last names, address, city, state, zip, and phone number.
    def addNewContact(self):
        contactname = input( "Enter name: ")
        self.contactlist = json.load(open(self.filePath,'r'))
        self.contactlist[contactname] = {'name': contactname,'lname': input("Enter Last Name: "), 'phone': input("Enter phone number: "), 'email': input("Enter email: ").lower(),'city': input("Enter city: "), 'state': input("Enter State: ") , 'zip' : input("Enter zip code: ")}
        json.dump(self.contactlist, open(self.filePath,'w'),sort_keys=True,indent=5)
        print ("Contact Added!")
        print("contact Details Added : ",self.contactlist[contactname])
        
    def printHeader(self):
        print ("%-30s %-30s %-30s %-30s %-30s %-30s %-30s" % ('NAME','LNAME','PHONE','EMAIL','CITY','STATE','ZIP'))
        #better formatting than using tab spaces and keeps items in a predetermined space apart from eachother
    
    def listAllContacts(self):
        print ('\n', "Listing Contacts...")
        self.printHeader()
        try:
            #Open file in read mode
            contactlist = json.load(open(self.filePath,'r'))
            name_keys = list(contactlist.keys())
        except:
            print("Unable to read contacts")
        for k in name_keys:
            print ("%-30s %-30s %-30s %-30s %-30s %-30s %-30s" % (contactlist[k]['name'], contactlist[k]['lname'], contactlist[k]['phone'],contactlist[k]['email'],contactlist[k]['city'],contactlist[k]['state'],contactlist[k]['zip']))
            #same idea as fotmatting above for each of the dict values

    def searchForContact(self):
        print ('\n', "Searching Contacts...")
        search = input("Please enter name (case sensitive): ")
        try:
            contactlist = json.load(open(self.filePath,'r'))
        except:
            contactlist = []
        try:
            self.printHeader()
            print ("%-30s %-30s %-30s %-30s %-30s %-30s %-30s" % (contactlist[search]['name'], contactlist[search]['lname'], contactlist[search]['phone'],contactlist[search]['email'],contactlist[search]['city'],contactlist[search]['state'],contactlist[search]['zip']))
        except KeyError: #error reporting- whenever a dict() object is requested & key is not in the dict.
            print ("Not Found")

    def editContact(self):
        print ('\n', "Editing Contact...")
        search_edit = input("Please enter name: ")
        try:
            contactlist=json.load(open(self.filePath,'r'))
            keys=contactlist.keys()
            for key in keys:
                if contactlist[key]['name'] ==  search_edit:
                    contactlist[key]['lname'] = input("Enter new last name: ")
                    contactlist[key]['phone'] = input("Enter new phone: ")
                    contactlist[key]['email'] = input("Enter Email id: ")
                    contactlist[key]['city'] = input("Enter new city: ")
                    contactlist[key]['state'] = input("Enter new state: ")
                    contactlist[key]['zip'] = input("Enter new zip: ")
            json.dump(contactlist, open(self.filePath,'w'))
        except KeyError: #error reporting- whenever a dict() object is requested & key is not in the dict.
            print ('\n', "Contact Not Found")

    
    def deleteContact(self):
        print ("Deleting Contact...")
        contactname = input("Enter Contact Name: ")
        contacts = json.loads(open(self.filePath).read())
        try:
            contacts.pop(contactname)
            json.dump(contacts, open(self.filePath,'w'))
        except KeyError: #error reporting- whenever a dict() object is requested & key is not in the dict.
            print ('\n', "Contact Not Found")
            

def main():

    # Creates an empty list of contacts
    book = AddressBook()
    book.setUpFile('contacts.json')
    loops = True

    # While loop used for options, it loops for user input until sequence is over
    while loops == True:

        # Prints option list for the user
        print ('Greetings user! Lets make an addressbook!', '\n', '\n', 'Would you like to: ', '\n', '1.) Add a New Contact', '\n', '2.) List All Contacts', '\n', '3.) Search Contacts', '\n','4.) Edit A Contact', '\n', '5.) Delete A Contact', '\n')

        # Asks for users input from 1-6
        
        
        userInput=input("Enter choice: ")
        # 1 : Add a new contact to list, also start of program if no file is made
        if userInput == "1":
            book.addNewContact()
        #  2 : list of contacts in addressbook
        elif userInput == "2":
            book.listAllContacts()
        elif userInput == "3":
            book.searchForContact()
        elif userInput == "4":
            book.editContact()
        elif userInput == "5":
            book.deleteContact()
        else:
            print ("Invalid Input! Try again.")


main()