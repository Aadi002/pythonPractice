class students:
    name = "student"
    age = "student"
    _class = "student"

    def __init__(self,name,age,_class):
        self.name = name
        self.age = age
        self._class = _class

    def average(self,score1,score2,score3):
        result = ((score1+score2+score3)/3)
        print(result)



calculate = students("ginger",24,3)
score1 = int(input("enter score1: "))
score2 = int(input("enter score1: "))
score3 = int(input("enter score1: "))

calculate.average(score1,score2,score3)

print(calculate.name,calculate.age,calculate._class)