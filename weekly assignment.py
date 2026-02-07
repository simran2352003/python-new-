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