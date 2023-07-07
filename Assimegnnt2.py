# arithmetic operator
a=18
b=41
print("Addition: ",a+b)
print("Subtraction: ",a-b)
print("Multiplication: ",a*b)
print("Division: ",a/b)
print("Mod: ",a%b)
print("Floor Division: ",a//b)
print("Exponentation: ",a**b)

# assignment operator
a=10
a+=2
print("+=",a)
a=10 ; 
a-=2
print("-=",a)
a=10
a*=2
print("*=",a)
a=10
a/=2
print("/=",a)
a=10
a//=2
print("//=",a)
a=10
a%=2
print("%=",a)
a=10
a**=2
print("**=",a)

# comparision operator
a=10
b=18
print("10>=18",a>=b)
print("10<=18",a<=b)
print("10==18",a==b)
print("10!=18",a!=b)
print("10<18",a<b)
print("10>18",a>b)

# logical operator
c=True
b=False
print("and",c and b)
print("or",c or b)
print("not",not b)


# bitwise operator
a=10
b=50
print("bitwise &",a&b)
print("bitwise |",a|b)
print("bitwise ^",a^b)
print("bitwise >>",a>>2)
print("bitwise <<",a<<2)

#identity operator
x=20
y=20.0
print("is",x is y)
print("is not",x is not y)

# membership operators
a="Soham"
print("in","s" in a)
print("not in","S" not in a)


# char to ASCII ord()
b="S"
val=ord(b)
print(val)

# ASCII to char chr()
print(chr(4))

#string formatting
a=10
b=20
sum=a+b
print("The addition of ",a," and ",b," is : ",sum)
print("The addition of {} and {} is {}".format(a,b,sum))
print(f"The addition of {a} and {b} is {sum}")
print("The addition of %d and %d is %d"%(a,b,sum))

#if..else.. positive negative num.
a=int(input("Enter a num: "))
if a>0:
    print("+ve")
elif a<0:
    print("-ve")
else:
    print("0")