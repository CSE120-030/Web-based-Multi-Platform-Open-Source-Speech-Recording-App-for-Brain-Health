class User:
    def __init__(self, userName, passWord):
        self.userName=userName
        self.passWord =passWord
    def printUser(self):
        print("UserName: "+self.userName,"passWord"+self.passWord)

class Language:
    def __init__(self,name):
        self.name=name

class Person:
    def __init__(self, firstName, lastName, languageID,email):
        self.firstName = firstName
        self.lastName = lastName
        self.languageID = languageID
        self.email= email

    def printPersonName(self):
        print("First Name: "+self.firstName,"Last Name "+self.lastName,"Language: "+self.languageID ,"email"+self.email)

class Expert(Person):
    def __init__(self, firstName,lastName,languageID,email,licenseNumber):

        super().__init__(firstName,lastName,languageID,email) #Inherit methods and properties from person class
        super(User, self).__init__()
        self.licenseNumber = licenseNumber


    def printExpertInfo(self):
        print("First Name: "+self.firstName,"Last Name "+self.lastName,"Language"+self.languageID,"license Number"+self.licenseNumber, "User_id"+self.userId)


class Patient(Person):
    def __init__(self, firstName,lastName,languageID,email,expertId,userID):
        super().__init__(firstName,lastName,languageID,email) #Inherit methods and properties from person class
        self.expertId =expertId
        self.userID =userID

    def printPatientInfo(self):
        print("First Name: " + self.firstName, "Last Name " + self.lastName, "Language" + self.languageID,
              "email" + self.email, "Expert id"+self.expertId,"User_id" + self.userId)



class Image:
    def __init__(self,filePath):
        self.filePath=filePath

    def returnImagePath(self):
        return self.filePath

class Audio:
    def __init__(self, filePath, patientID):
        self.filePath = filePath
        self.patientID = patientID

    def returnAudioPath(self):
        return self.filePath

class Type_Of_Prompt:
    def __init__(self, name, description, promptID, patientID):
        self.name =name
        self.description =description
        self.promptID= promptID
        self.patientID =patientID

class Prompt:
    def __init__(self,dirPrompt, languageID, type_of_prompt, expertID, imageID):
        self.dirPrompt =dirPrompt
        self.languageID =languageID
        self.type_of_prompt = type_of_prompt
        self.expertID =expertID
        self.imageID = imageID













