#Question1
a=input("enter name1")
b=input("enter name2")
c=input("enter name3")                                            #creating a user defined list
d=input("enter name4")
print (type(a))
L=[]
L.append(a)
L.append(b)
L.append(c)
L.append(d)
print("The list is",L)
#end

#Question 2
L=["a","b","c","d"]
L.insert(4,"google")
L.insert(5,"apple")
L.insert(6,"facebook")                                              #adding a list with previous one
L.insert(7,"microsoft")
L.insert(8,"tesla")
print(L)
#end

#Question 3
L=[1,2,3,4,5,2,4,2]                                                 #count the times object occurs
print(L.count(2))
#end

#Question 4
L=[1,4,3]                                                            #sorting a list in ascending order
L=sorted(L)
print("The sorted list in ascending order is",L)
#end

#Question 5
A=[5,3,1,2,4]
B=[7,9,8]
A=sorted(A)
B=sorted(B)
C=A+B                                                            #adding two lists
C=sorted(C)                                                      #sorting in ascending order
print("The sorted list is",C)
#end

#Question 6
L=[1,2,3,4]
L.pop()
print("After popping list is",L)
L.append(5)                                                     #Implementation of stack
print("After appending list is",L)
L.insert(3,4)
print("After inserting list is",L)
#end







