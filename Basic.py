#1 Hello Wprld
print("Hello World \r")

#2 Variable
num=123
print(num, "\r")

#3 String
str="Hello"
print(str,"\r")

#4 type of variable
print(type(1))
print(type(1.5))
print(type('Hello'))
print(type(u'r welcome',))
print("\r")

#5 range function
print(range(0,5))
print("\r")

#6 keywords in python
import keyword
print("Keywords in Python : ")
print(keyword.kwlist)
print("\r")

#True false,none
print(False==0)
print(True==1)
print(True+True+True)
print(True+False+False)
print(None==0)
print(None==[])
print("\r")

#7 AND OR NOT IS keywords
print(True and False)
print(True or False)
print(not True)
print('' is '')
print({} is {} )

#8 using \r
print("\r")


#9multiline statements
a=2;b=4;c=5
print(a+b+c);print(a-b-c)

#10check if string is valid or not

lst=["for","if","sam","while","tony"]
for i in range(len(lst)):
    if keyword.iskeyword(lst[i]):
        print(lst[i]+ " is python keyword")
    else:
        print(lst[i]+ " is not python keyword")


#11 print two sentences using comma
print("Hello ", end=" ") 
print("Welcome!!")

n=[1,2,3,4,5]
print(*n)

