class Student:
    def display_details (self):
        print("Student details")
class Guardian(Student):
    def display_details (self):
        #super().display_details() To call the date from parent class
        print("Guardian details")
guardian1 = Guardian()
guardian1.display_details()


