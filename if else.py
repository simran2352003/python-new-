
# ifelse,forloop
num = int(input("enter a month:"))
if num == 1:
   print("january:")
elif num == 2:
    print("february:")
elif num == 3:
    print("march:")
elif num == 4:
    print("april:")
elif num == 5:
    print("may:")
elif num == 6:
    print("june:")
elif num == 7:
    print("july:")
elif num == 8:
    print("august:")
elif num == 9:
    print("september:")
elif num == 10:
    print("october:")
elif num == 11:
    print("november:")
elif num == 12:
    print("december:")    
else:
    print("invalid output:") 
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
if num1 == num2:
    print("both numbers are equal:")
else:
    print("both numbers are not equal:")

num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))
if num1>num2:
    print("num1 is bigger than num2:")
else:
    print("num1 is smaller than num2:")

a = int(input("enter a first number:"))
b = int(input("enter a second number:"))
if a<=b :
    print("first number is smaller than second:")
else:
    print("first number is equal to second:")

num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))
first_name = "Simran" 
surname = "dhiman"
if num1 > num2 :
  for i in range(5):
   print("first_name",first_name)
elif num1 < num2 :
  for i in range(3):
   print("surname",surname)
else:
   print("wrong output:")                            


str1 = input("enter a string:")
str2 = input("enter a string:")
if str1 == str2:
   print("both string is equal:")
else:
    print("both strings are not equal:")    

str1 = input("enter a string:")
str2 = input("enter a string:")
if str1 is str2:
    print("both equal or not:")
else:
    print("both are not equal:")


str1 = input("enter a string:")
str2 = input("enter a string:")
num1 = int(str1)
num2 = int(str2)
if num1 is num2:
    print("both are equal:")
else:
    print("both are not equal:")

num = int(input("enter a number:")) 
total = 0
for i in range(1,num + 1):
   total += i
    print("sum of numbers from 1 to",num,"is:",total)

num = int(input("enter a number:"))
print("even numbers are:")
for i in range(2,num+1,2):
    print(i,end="")

num = int(input("enter a number:"))
op = input("enter op(+ o -):")
if op == "+":
 for i in range(num):
        print(i,end=",")
elif op == "-":
 for i in range(num, 0,-1):
        print(i,end=",")
else:
        print("invalid operator")            