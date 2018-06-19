#QUESTION 1

for i in range(10):
    i=int(input("enter no."))            # input 10 integers
    print(i)                             # print 10 integers
#END

#QUESTION 2

i="true"
while(i=="true"):                        #infinite loop
    print("loop is infinite")

#END

#QUESTION 3

l=[]
a=int(input("enter element"))
b=int(input("enter element"))             #square of no's
l.append(a)
l.append(b)
for i in l:
    print(i**2)
#END

#QUESTION 4

l=[2,2.5,"hello",8,"red",6.5,9]
Int=[]
String=[]                                #print integers,float and string seperately
Float=[]
for i in l:
    if isinstance(i,int):
        Int.append(i)

    elif isinstance(i,str):
        String.append(i)

    else:
        Float.append(i)
print(Float)
print(String)
print(Int)
#END

#QUESTION 5

even=[]
odd=[]
for i in range(1,101):
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)                        #print odd &even no.
print("no. is even",even)
print("no. is odd",odd)
#END

#QUESTION 6


for i in range(0,4):
    for i in range(0,i+1):
        print("*",end=" ")                   #print pattern
    print()
#END

#QUESTION 7

a=input("enter name")
b=input("enter age")                          # get keys to corresponding values in dictionary
d={"name": a, "age":b}
for i in d:
    d.get(i)
    print(i)
#END