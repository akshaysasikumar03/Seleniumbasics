def string_handling():
    text="abstract"
    print(text[0])
    print(text[1])
    print(text[:2])
    print(text[1:5])
    pretext="Hello"
    print(pretext+" "+text)
#changeincase    print(text.capitalize())
    message= "Hello World"
    print("Hi" in message)
    new_message= message.replace("Hello","Hey")
    print(new_message)
string_handling()