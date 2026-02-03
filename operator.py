#input student details
Name = input("enter a name:")
stu_class = input("enter a class:")
section = input("enter a section:")
m1 = int(input("enter a marks of subject 1:"))
m2 = int(input("enter a marks of subject 2:"))
m3 = int(input("enter a marks of subject 3:"))
m4 = int(input("enter a marks of subject 4:"))
m5 = int(input("enter a marks of subject 5:"))
total = m1+m2+m3+m4+m5
percentage =(total/500)*100
print("n-----Student Result-----")
print("name",Name)
print("class",stu_class)
print("section",section)
print("percentage",percentage,"%")

#enter a number and return sum of it.
a = 10
b = 20
c = 10
sum = a+b+c
print("the sum is",sum)

#input a number and return a square of it.
num = int(input("Enter a number:"))
square = num*num
print("square is",square)

#take the temperature in celsius as input
celsius_str = input("enter temperature in celsius:")
celsius = float(celsius_str)
fahrenheit = (celsius*9/5) + 32
print("temperature in celsius:",celsius)
print("temperature in fahrenheit:",fahrenheit)
#quotient and remainder
a = int(input("enter a number:"))
b = int(input("enter a number:"))
quotient = a // b
remainder = a % b
print("quotient",quotient)
print("remainder",remainder)
#Simple interest
P = float(input("enter principal amount:"))
R = float(input("enter rate of interest:"))
T = float(input("enter time(in years):"))
SI = (P*R*T)/100
print("simple interest is:",SI)




