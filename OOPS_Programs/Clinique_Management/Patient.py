class Patient :
    def __init__(self,id = None,name = None,phone = None,age = None):
        self.id = id
        self.name = name
        self.phone = phone
        self.age = age
    def setId(self,id):
        self.id = id
    def setName(self,name):
        self.name = name
    def setPhone(self,phone):
        self.phone  = phone
    def setAge(self,age):
        self.age = age
    def getId(self):
        return self.id 
    def getName(self):
        return self.name
    def getPhone(self):
        return self.phone
    def getAge(self):
        return self.age