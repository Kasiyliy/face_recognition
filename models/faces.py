class Faces:

    def __init__(self):
        self.full_name = ''
        self.file_name = ''


    def __init__(self , id  ,  full_name , file_name , group):
        self.id = id
        self.full_name = full_name
        self.file_name = file_name
        self.group = group

    def getId(self):
        return self.id

    def getFullName(self):
        return self.full_name

    def getFileName(self):
        return self.file_name

    def getGroup(self):
        return self.group

    def setId(self , id):
        self.id = id

    def setFullName(self , full_name):
        self.full_name = full_name

    def setFileName(self, file_name):
        self.file_name = file_name

    def setGroup(self, group):
        self.group = group