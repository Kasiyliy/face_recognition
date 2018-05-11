class Groups:

    def __init__(self):
        self.id = 0
        self.name = ''

    def __init__(self , id  ,  name ):
        self.id = id
        self.name = name

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setId(self , id):
        self.id = id

    def setName(self , name):
        self.name = name
