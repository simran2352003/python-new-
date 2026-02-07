# create a list of friends
friends = ["aman","priya","simran","govind"]
print("current friends list:",friends)
new_friends = input("enter another friend name:")
friends.append(new_friends)
print("updated list:",friends)
important_friend = input("enter most important friend name:")
print("final friends list:",friends)

num = [1,2,3,4,5,6,7,8,9,10]
print(num)
 
num = [1,10,100,3,6,8]
num.insert(3,59)
num.append(5)
print("updated list:",num)
print("length of list:",len(num))

#find all the  short words from the list 
words = ["tree","python","moon","priya"]
short_words = [] 
for word in words:
 if len(word) < 4:
    short_words.append(word)
    print("words with less than 4 letters:", short_words)

 numbers = range(20)
for i in range (1,21): 
 if i%2 == 0:
    print('even')
 else:
    print("odd")   

for i in range(1,1000):
   if i%7 == 0:
  print(i)
find all the space from the string
str = input("enter a string:")
sum = str.count(" ")
print(sum)

a =[1,2,3,4]
b =[2,3,4,5]
common=[]
for i in a:
   for j in b:
        if i == j:
            common.append(i)

print(common)



    

