#find the length of the name
name = input("enter your name")
print(len(name))
for i in range(O,len(name)):
    print(name)
n = int(input("enter a  first natural numbers:"))
total = sum(range(1,n+1))
print("sum of first natural numbers",total)

num = int(input("enter a number:"))
for i in range(1,11):
    print(num,num*i)
n = int(input("enter number"))
print(n**0.5)
if n<=1:
 print("false")
else:
    prime = True
    for i in range(2,n+1):
       if n%i==0:
            prime = False
            print(prime)

#print numbers from 1 to 100:
numbers = int(input("enter a numbers:"))
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
       print("fizzBuzz")
    elif i % 3 == 0:
        print("buzz")
    else:
        print(i)        

num = input("enter a number:")
if num == num[::-1]:
    print("palindrome number")
else:
    print("not a palindrome number")    