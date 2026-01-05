class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age
        self.__ssn = "20"
    def get_ssn(self):
        return self.__ssn
    def set_ssn(self, new_ssn):
        self.__ssn = new_ssn
person1=Person("John", 18)
print(person1.get_ssn())
print(person1.name)
person1.set_ssn("25")
print(person1.get_ssn())
