s = input("enter a string")
if len(s) < 3:
    print("not a valid string")
else:
    result = s[:3] + s[-3:]
    print("result:",result)    

str1 = input("enter first string:")
str2 = input("enter second string:")
new_str1 = str2[0] + str1[2:]
new_str2 = str1[0] + str2[2:]
result = new_str1 +""+new_str2
print("result:",result)

str = input("enter a string:")
if len(str) < 3:
    result = str
elif str.endswith("ing"):
    result = str + "ly"
else:
    result = str + "ing"
    print("result:",result)        

string = input("enter a string:")
n = int(input("enter the index to remove:"))
if n<0 or n>= len(string):
    print("invalid index!")
else:
    new_string = string[:n]+string[n+1:] 
    print("string after removal:",new_string)    
