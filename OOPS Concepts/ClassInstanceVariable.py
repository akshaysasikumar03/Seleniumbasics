class Test:
    school_name="oxford school"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def print_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("School Name:",Test.school_name)
test = Test("John",18)
test1 = Test("Xavier",22)
test.print_details()
test1.print_details()
test.name="Charles"
Test.school_name="X School"
test.print_details()
test1.print_details()
