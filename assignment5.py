#QUESTION 1

leap=int(input("Enter year"))
if(leap%4==0):
    print("leap year")                               # check whether it is leap year or not
else:
    print("Not a leap year")
#END


#QUESTION 2

l=int(input("enter length"))
b=int(input("enter breadth"))
if(l==b):
    print("Dimensions are of square")                #check whether it is rectangle or square
else:
    print("Dimensions are of rectangle")
#END

#QUESTION 3

a=int(input("enter age"))
b=int(input("enter age"))
c=int(input("enter age"))                            #print eldest and youngest amongb them
if((a>b)and(a>c)):
    print("a is eldest")
elif((b>a)and(b>c)):
    print("b is eldest")
else:
    print("c is eldest")
    if((a<b)and(a<c)):
        print("a is youngest")
    elif((b<a)and(b<c)):
        print("b is youngest")
    else:
        print("c is youngest")
#END

#QUESTION 4

points=int(input("Enter points"))
if((points>1) and (points<50)):
    print("Sorry! No prize this time")
elif((points>51)and (points <151)):
    print("Conratulations!You won a Wooden bag")      # print message
elif((points >151)and(points <180)):
    print("Congratulations!You won a Book")
else:
    print("Congratulations!You won Chocolate")
#END

#QUESTION 5

cost=100
quantity=int(input("Enter quantity"))
c=quantity*cost
d=c-0.1*c                                            # print cost for user
if(c>1000):
    print(d)
else:
    print(c)
#END

