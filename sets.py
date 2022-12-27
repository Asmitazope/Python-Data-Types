'''#1 creating set
set1=set("Hello World")
print(set1)

#2 create set using list
set2=set([1,'Hi',1.5])
print(set2)

myset={4,"welcome",8.0}
print(myset)

#3 adding elements to set using add() method

set_1=set()

set_1.add('key')
set_1.add(10)
set_1.add(1.1)
print(set_1)'''

#4 adding elements to set using update method
set_2={1,2,(3,4)}
set_2.update("Hello")
print(set_2)
'''
for i in set_2:
    print(i,end=' ')
'''
#5 removing elements from set using remove() or discard() method
set_2.remove(2)
set_2.discard(4)
set_2.pop()
print(set_2)


lst=list(set_2)

print('Converted SET to LIST: ',lst)

s=set(lst)

print('Converted LIST to SET: ',s)
