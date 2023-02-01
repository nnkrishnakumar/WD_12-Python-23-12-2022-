#str()--> string 
#int()--> Integer
#float()--> float
#list()--> list
#tuple() --> tuple
#set()  --> set
#dict()  --> dictionary
#bool() --> boolean
#complex()--> complex 


a=1
print("a",a,type(a))
b=str(a)             #str() convert integer to string
print("b",b, type(b))  #1 <class 'str'>

c=float(a)   #1.0
print(c)

d=10.0
print(int(d))

# c="krishna"
# print(float(c))     #error

d="10k"
e=d[0:2]     #"10"
print("e",e,type(e))
f=int(e)
print("f",f,type(f))


d="10k"
print(type(int(d[0:2])))   #<class 'int'>
print(int(d[0:2]))   #10


d="10k"
print(type(int(d[0:2])),int(d[0:2]))   #<class 'int'> 10



e="10.0"
f=float(e)   #10.0
print(f)
g=int(f)     #10
print(g)


e="10.0"
print(int(float(e)))