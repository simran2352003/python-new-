data = [
   {"name": "forest gump","year":1994,"duration":142,"genres":["Drama", "romance"]},
    {"name": "avengers: endgame", "year": 2019,"duration":181,"genres":["action","adventure","drama"]},
    {"name": "back to the future", "year":1985,"duration": 114,"genres":["adventure","comedy","Sci-Fi"]}
]
def input_int(prompt):
   while True:
        try:
           value = int(input(prompt))
           if value >= 1:
                return value
           else:
                print("please enter an integer greater than or equal to 1.")
        exceptValueError:
print("invalid input.please enter an integer.")
def input_something(prompt):
    while True:
       value = input(prompt).strip()
       if value != "":
            return value
       else:
            print("input cannot be empty or whitespace only.")
print("welcome to the movie manager!")
while True:
   print("choose [a]dd,[l]ist,[s]earch,[v]iew,[d]elete or [q]uit.")
   choice = input(">").lower()
   if choice == "a":
        name = input_something("enter movie name:")
        year = input_int("enter release year:")
        duration = input_int("enter duration (minute):")
        genres []
        print("enter generes(at least one required).")
        while true:
           genre = input_something("enter genre:")
           genre = append(genre)
           more = input("add another genre?(y/n):").lower()
           if more == "n":
              break
        new_movie = {
                "name": name,
                "year": year,
                "duration":duration,
                "genres": genres
            }
   data.append(new_movie)
   print(f"{name} added successfully.")
   elif choice == "1":
   if len(data) == 0:
            print("no movies saved.")
   else:
            for index, movie  is enumerical(data):
   print(f"{index + 1})") {movie['name']}({movie['year']})")
   elif choice == "s":
   if len(data) == 0:
            print("no movies saved.")
   else:
            term = input_something("enter search term:").lower()
            found = False
            for index,movie in enumerate(data):
              if term in movie["name"].lower():
                print(f"{index + 1}) {movie['name']} ({movie['year']})")
                found = True
            if not found:
   print("no matching movies found.")
   elif choice == "v":
   if len(data) == 0:
             print("no movies saved.")
   else:
           index = int(input("enter index number:"))
   if 1 <= index <= len(data):
           movie = data[index-1]
           genre_formatted = ",".join(movie["genres"])
           print(f"name:{movie["name"]}")
           print(f"year:(movie['year'])")
           print(f"duration:{movie{'duration'}} minutes")
           print(f"genres:{genres_formatted}")
   else:
           print("invalid index number.")
   elif choice == "d":
   if len(data) == 0:
        print("no movies saved.")
   else:
         index = int(input("enter movie index number:"))
         if 1 <= index <= len(data):
               removed_movie = data.pop(index - 1)
               print(f"{removed_movie['name']}")
         else:
               print("invalid index number.")
            elif choice == "q":
         print("goodbye!")
         break 
else:
 print("invalid choice!")




