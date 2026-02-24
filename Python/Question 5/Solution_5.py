class inputOutString():

    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()
    
    def printString(self):
        print(self.s.upper())


string_object = inputOutString()
string_object.getString()
string_object.printString()