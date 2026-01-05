file_path="C:/Users/Aksha/OneDrive/Desktop/TextFile.txt"

f=open(file_path,"w+")
f.write("hello world\n")
f.write("Hiiiiiiiiiii\n")
for line in f:
    print(line.strip())
f.close()
f=open("test.txt","r+")
for line in f:
    print(line.strip())
f.write("hello world1111\n")
f.close()
f=open("test.txt","a")
f.write("Appending the file")
f.close()