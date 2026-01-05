list1=[1,7,14,21,28]
print(list1)
print(list1[0])
list2=[2]*5
print(list2)
print(list1[-1])
list3=[]
print(list3)
list4=["abc","bcd","efg","pqr","def"]
list4.insert(2,"Hi")
print(list4)
list4.append("Hello")
print(list4)
print(list4.index("Hi"))
print(list4.sort())
list5=[100,81,64,121,32,100]
#list5.sort()
print(list5)
list5.reverse()
#list5.sort(reverse=True)
print(list5)

"""while True:
    for item in list5:
        print(item)
    break"""
print(list5.count(120))
list5.remove(100)
print(list5)
for i in range(1):
 list5.remove(100)
print(list5)