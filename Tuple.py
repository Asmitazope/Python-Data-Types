#1 create tuple

tup=(1,2,'abcd','defg',0.5,6.0)
print(tup)
#print(tup[0])
#print(tup[0:])
#print(tup[-1])
#print(tup[-1:])

print(type(tup))

## change items in tuple
#step 1 convert tuple to list
lst=list(tup)

# step 2 add items
lst[0]=6
lst.append('Hi')

#step 3 convert list to tuple
change_Tup=tuple(lst)

print(change_Tup)

