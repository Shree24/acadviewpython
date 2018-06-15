#Question 1
a=input("enter name")
b=input("enter no.")
c=input("enter list")
t=(a,b,c)                                     # created three data types integer,string,list
print(len(t))                                             # returned length function
#end

#Question 2
t=(5,2,7,1,0)                                              # created tuple
print(min(t))                                              #minimum
print(max(t))                                              #maximum
#end

#Question 3
t=(1*4*5*9)                                                #product of no"s in tuple
print(t)
#end

#Question 4
c=input("enter no.1")
d=input("enter no. 2")
e=input("enter no. 3")
f=input("enter no. 4")
a=set([c,d,e,f])                                       # created 2 sets
b=set([e,f])
diff=a-b                                                   # difference between two sets
print(diff)
print(a>=b)                                                #comparison between sets
print(a<=b)
print(b>=a)
print(b<=a)
print(a&b)                                                 #intersection between two sets
#end

#Question 5
a=input("enter name")
b=input("enter age")
d={"name":a,                                               # create  DICTIONARY
     "age":b
   }
print(d)

#Question 7
m=['m','i','s','s','i','s','s','i','p','p''i']
n={'M':m.count('m'),                                       #count m in list
   'I':m.count('i'),                                       #count i in list
   'S':m.count('s'),                                       #count s in list
   'P':m.count('p')}                                       #count p in list
print(n)