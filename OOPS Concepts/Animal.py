class Animal:
    def speak(self):
        print("Animal Makes Sound") #parentclass
class Dog(Animal):
    def bark(self):
        print("Dog Bark")
dog1 = Dog() #dog1 is object
dog1.speak()
dog1.bark()
