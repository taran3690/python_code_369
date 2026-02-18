# A Variable is a name give to a memory location in a program.
name="jassu"
age=18
price=25.254
print(name)
print(age)
print(price)
#name is variable. 
#"jassu" is value.
print("my name is : ",name) 
print("my age is :",age)
#data types.integers,string,float,boolean,none.
#integers=+ve,-ve,0.(25,-25,0).
#string="jassu","hello".
#float=3.99,2.55,5.99.
#boolean=true/false
#none=a=none, a = no value
print(type(name))#str value
print(type(age)) #int value
print(type(price))#float value
#boolean
old=True
even=False
print(type(old)) 

print(type(even))
#a=none value
a=None
print(type(a))
#print sum
a=5
b=2
sum=a+b
print(sum)
#type of operators
#an operator is a symbol that performs a certain operation between operands.
# arithmetic operators(+,-,*,%,**)
print(a-b)
print(a*b)
print(a%b)#remainder
print(a**b)#a^b
print(a/b)
#relation/comparison operators(==,!=,>,<,>=,<=)
A=50
B=20
print(A==B)#FALSE
print(A!=B)#TRUE
print(A>=b)#true
print(A>B)#true
print(A<=B)#false
print(A<B) #false   
#assignment operators(=,+=,*=,%=,**=)
num=10
#num+=10   #20
#num=num+10 #10+10=20
print(num)
num1=10
num1*=5
print(num1) #50
num2=10
num2/=5
print(num2) #2.0
num3=10
num3%=5
print(num3) #0
num4=10
num4**=5
print(num4)  #1,00,000       
 #logical operators(not,and,or)
print(not False)
print(not True)   
c=50
d=30
print(not (c>d))    
val1=True
val2=False
print("and operator",val1 and val2) # two val true ans true. but one val false ans  false.            
print("or operator",val1 and val2)#one val true ans true.but two val false ans false. 
print("or operator:",(c==d)or (c>d))


                                                                                                