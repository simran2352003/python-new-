#sentence
sentence = input("enter a sentence:")
words = sentence.lower().split()
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
        sorted_freq = dict(sorted(freq.items(),key = lambda x: x[1], reverse = True))
        print(sorted_freq)

#students
students = {
    "aman" : 75,
    "riya": 85,
    "karan": 65,
    "neha": 90,
    "rahul": 70
}
total = sum(students.values())
count = len(students)
average = total/count
print("average marks:",average)
print("students scoring above average:")
for name, marks in students.items():
    if marks > average:
        print(name)
#dictionary
dict1 = {'a': 50,'b': 30,'c': 70}
dict2 = {'b': 60,'c': 65,'d': 40}
result = {}
for key in dict1:
    if key in dict2:
        result[key] = max(dict1[key],dict2[key])
    else:
        result[key] = dict1[key]
        for key in dict2:
            if key not in result:
                result[key] = dict2[key]
                print(result)

#maximum length value
data = {'name': 'alice', 'city':'banglore','course':'data science'}
max_key = None
max_length = 0
for key, value in data.items():
 if len(value)> max_length:
  max_length = len(value)
  max_key = key
  print("key with longest value:",max_key)

#using loop
data = {'a': 5, 'b': 20,'c':55,'d': 40,'e': 10}
result = {}
for key,value in data.items():
    if 10 <= value <= 50:
        result[key] = value
        print(result)
#votes
votes = {}
n = int(input("enter number of voters:"))
for i in range(n):
    candidate = input("enter candidate name:").lower()
    if candidate in votes:
        votes[candidate] += 1 
    else:
        votes[candidate] = 1
        print("/nvote count:")
        for name,count in votes.items():
            print(name,":", count)
            winner = max(votes,key=votes.get)
            print("/nwinner is:",winner)    

# original dictionary
data = {'a': 10, 'b': 20, 'c': 30}
update = {'b': 200, 'c':300}
for key in data:
    if key in update:
        data[key] = update[key]
        print(data)



