class Animal:
    def speak(self):
        print("Animal Makes Sound") #parentclass
    def walk(self):
        print("Animal Walks!")
class Dog:
    def bark(self):
        print("Dog Bark")
class puppy(Dog,Animal):
    def speak(self):
        print("puppy Weeps")
puppy3=puppy()
puppy3.speak()
puppy3.bark()
puppy3.walk()
