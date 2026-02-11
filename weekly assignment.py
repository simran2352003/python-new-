<<<<<<< HEAD
#print all prime numbers between 1 to 100
int = int(input("enter a number:"))
for num in range(2,101):
    is_prime = True
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break
        if is_prime:
            print(num,end="")

for num in range(1,51):
 if num % 3 == 0 and num % 5 == 0:
       print("fizzbuzz")
 elif num % 3 == 0:
    print("fizz")
 elif num % 5 == 0:
    print("buzz")
 else :
    print(num)        

# ask from user to input a score
score = int(input("enter your score(0-100):"))
if score >= 90 and score <= 100:
    print("grade:A")
elif score >=80 and score <=89:
    print("grade:B") 
elif score >=70 and score <=79:
    print("grade:C")
elif score >=60 and score <=69:
    print("grade D")
else:
    print("invalid output! please enter a value between 0 and 100.")

num = int(input("enter a number:"))
for i in range(1,11):
    print(f"{num}*{i} = {num*i}")

squares = []
for num in range(1,21):
    if num % 2 == 0:
        squares.append(num ** 2)
        print(squares) 
year = int(input("enter a year:"))
if (year % 4 == 0 and year % 100!=0)or(year % 400 == 0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")    
a = float(input("enter first side:"))
b = float(input("enter second side:"))
c = float(input("enter third side:"))
f a+b>c and a+c>b and b+c>a:
    sides = sorted([a,b,c])
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("right angle triangle")
    elif a == b == c:
        print("equilateral triangle")
    elif a == b or b == c or a == c:
        print("isosceles triangle")
    else:
        print("scalene triangle")
else:
     print("not a valid triangle")

num = int(input("enter an integer:"))
if num>0:
    print("positive number")
elif num < 0:
    print("negative number")
else:
    print("zero") 

weight = int(input("enter a body mass index:"))
bmi = weight /(weight * weight)
if   bmi < 18.5:
    print("it is underweight")
elif bmi < 24.9:
    print("normal weight")
elif bmi < 29.9:
    print("overweight")
else:    
    print("obesity")


a = int(input("enter a days of week:"))
if  a == 1:
    print("sunday:")
else:
    print("monday:")

discount = float(input("enter a product based discount:"))
price =    float(input("enter a price:"))      
if price > 1000 :
    discount = price*0.10
elif price >= 500 and price <= 1000:
    discount = price*0.05
else:
    discount = 0
    final_price = price - discount
print("discount:",discount) 
print("final price:",final_price)   
employee_details = {
 101:{"name": "priya","department":"IT", "salary": 60000},
  102:{"name": "rahul","department":"IT","salary": 45000 },
  103:{"name": "kartik","department":"IT","salary": 75000}
high_salary_employee = [] 
for emp in employee_details.values():
 if emp ["salary"]>50000:
   high_salary_employee.append(emp["name"])
    print(high_salary_employee)
text = input("enter a string:")
count = 0
for i in text:
    if i in "aeiou":

     count += 1
     print("number of vowels:", count)   
num = int(input("enter a number:"))
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit#
    num = num // 10
    print("sum of digits:",sum)


n = 5
or i in range (1, n+1):
   print("*" * i)

number = random.randint(1,100)
guess = 0 
while guess != number:
guess = int(input("enter your guess (1to100):"))

if guess > number:
    print("too high")
elif guess < number:
    print("too low") 
else:
    print("correct! you guessed the number:")
 
a = int(input("enter a number:"))
for i in range(1,a+1):
    if i % 2 == 0:
      print(i,end=" ")

# create a list of 10 number elements 
numbers = [10,26,25,20,67,89,21,22,44,11]
if 25 in numbers:
    print("25 exists in the list")
else:
    print("25 does not exists in the list")
print("length of the list:", len(numbers))
print("total occurrence of 25:", numbers.count(25))
print("traversing the list:")
for i in numbers: 
    print(i) 
print("even numbers in the list:")
for i in numbers:
   if i % 2 == 0:
          print(i,end=" ")

#string
str = " i love python"
print(str) 
print("length of string:",len(str))
if str == str[::-2]:
    print("string is palindrome")
else:
   print("string is not palindrome") 
 #tell middle word in the string
words = str.split()
middle = len(words)//2
print("middle character:",words[middle])   
if len(words)>= 2:
    print("second last words:", words[-2])
else:
     print("invalid string")  


a = int(input("enter a number:"))   
b = int(input("enter a number:"))
print(a^b)
print(a+b)
print(a-b)
print(a*b)

X = ['abc','xyz','aba','1221']
count = 0
for s in X:
  if len(s) >= 2 and s[0] == s[-1]:
    count += 1   
print("number of matching strings:",count)






  
=======
#print all prime numbers between 1 to 100
#int = int(input("enter a number:"))
#for num in range(2,101):
#    is_prime = True
#    for i in range(2,num):
#        if num % i == 0:
#            is_prime = False
#            break
#        if is_prime:
#            print(num,end="")

for num in range(1,51):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else :
        print(num)        
>>>>>>> 9b4b7c86dbb5d0ff2fcd5ac2ba4ba622bfc4dac2
