class Test:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def print_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
test = Test("John",18)
test.print_details()