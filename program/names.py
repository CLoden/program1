from database import Database

class name:
    __name = ""
    __year = ""
    __gender = ""
    __count = ""

    def __init__(self, name, year, gender, count):
        self.__name = name
        self.__year = year
        self.__gender = gender
        self.__count = count

    def getName(self):
        return self.__name

    def getYear(self):
        return self.__year

    def getGender(self):
        return self.__gender

    def getCount(self):
        return self.__count

    def setName(self, newName):
        self.__name = newName

    def setYear(self, newYear):
        self.__year = newYear

    def setGender(self, newGender):
        self.__gender = newGender

    def setCount(self, newCount):
        self.__count = newCount

    #Your Name.py file should include a static method called readNames()
    # that takes two parameters, and passes those parameters into the readNames() method in Database.py.
    # It should return the list of names that it gets from readNames() in Database.py,
    # just like in the previous assignment.
    @staticmethod
    def readNames(name, gender):
        return Database.readNames(name, gender)

