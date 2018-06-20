#Question 1

radius=int(input("Enter radius"))
def area(rad):
    area=3.14*rad*rad
    return area                                        # radius of circle
ar=area(radius)
print(ar)

#End

#Question 2

n=6
def perfect(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    if(sum==n):                                         #perfect number in range 1 to 1000
        return True
    else:
        return False
print(perfect(n))
for i in range(1,1001):
     if(perfect(i)==True):
         print(i)

#End

#Question 3

def mul(n,i=1):
    print(str(n)+"*"+str(i)+"="+str(n*i))                # table of 12
    if i!=10:
        mul(n,i+1)
mul(12)

#End

#Question 4

def power(a,b):
    if(b==1):                                           # power of a no. raised to other
        return a
    else:
        return a* power(a,b-1)
print(power(5,4))

#End

#Question 5

def factorial(n):
    if n==1:
        return 1                                         # factorial of a no.
    else:
        return n* factorial(n-1)
print(factorial(7))




