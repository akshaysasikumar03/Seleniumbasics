class Great:
    def greet(self,name=None):
        if name is not None:
            print("Hello" ,name)
        else:
            print("Hello World")
greet1 = Great()
greet1.greet("John")
greet1.greet()