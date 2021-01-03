class Doctor :
    def __init__(self,id=None,name=None,spec=None,avail=None):
        self.id = id
        self.name = name
        self.spec = spec
        self.avail = avail
    def setId(self,id):
        self.id = id
    def setName(self,name):
        self.name = name
    def setSpec(self,spec):
        self.spec  = spec
    def setAvail(self,avail):
        self.avail = avail
    def getId(self):
        return self.id 
    def getName(self):
        return self.name
    def getSpec(self):
        return self.spec
    def getAvail(self):
        return self.avail
    
    