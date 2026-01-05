class Person:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
    def greet(self):
        print("Hello, My name is " + self.name)
        print("Hello, my age is " + str(self.age))
        print("Hello, my city is " + self.city)
person1 = Person("John",23,"NYC")
person1.greet()


class AverageCalculation:
    def __init__(self,number1,number2,number3):
        self.number1=number1
        self.number2=number2
        self.number3=number3
    def average(self):
        print("The average is",(self.number1+self.number2+self.number3)/3)
average1=AverageCalculation(5,2,3)
avarage=average1.average()
