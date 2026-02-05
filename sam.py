#name = input("enter passenger name:")
#age = int(input("enter passenger age:"))
#print("choose travel class:")
#print("1.first class-1500")
#print("2.second class-10000")
#print("3.sleeper class-500")
#choice = int(input("enter class number(1,2,3):"))
#if choice == 1:
#    travel_class = "first class"
#    price = 1500
#elif choice == 2:
#    travel_class = "second class"
#    price = 500
#else:
 #   print("invalid class selection!")
#    price = 0
#    travel_class = "invalid"
#if age < 5:
#   final_price = 0
#else:
#    final_price = price
#if age >=60:
#    discount = final_price*0.20
#    final_price = final_price - discount
#meal = input("do you want to add a meal ?(yes/no):").lower()
#if meal == "yes" and age >=5:
#    final_price +=200
#    meal_status = "meal added"
#else:
#    meal_status = "no meal" 
#print("----ticket details----")
#print("passenger name :", name) 
#print("age            :",  age) 
#print("class          :",travel_class)
#print("meal option    :",meal_status)
#print("final price    :",final_price)  
#print("thank you for booking with coderail!")



print("welcome to burger king self-order kiosk")
whopper_price  = 150
crispyveg_price = 100
wings_price    = 120
print("menu")
print("1. whopper burger -150")
print("2. crispy veg     -100")
print("3. chicken wings  -120")
choice = int(input("enter item number(1-3):"))
qty = int(input("enter quantity:"))
if choice == 1:
    item_name = "whopper burger"
    total = whopper_price*qty
elif choice == 2:
    item_name = "crispy veg"
    total = crispyveg_price * qty
elif choice == 3:
    item_name = "chicken wings"
    total = wings_price * qty
else:
    print("invalid choice!")

coupon = input("do you have a coupon code? Enter code or type 'no':")
discount = 0
valid_coupon = "BK10"
if coupon == valid_coupon:
   discount = total * 0.10
   print("coupon applied! you got 10% OFF")
else:
   print("no valid coupon applied.")
 
final_bill = total - discount
print("---bill---")
print("item:",item_name)
print("quantity:",qty)
print("subtotal:",total)
print("discount:",discount)
print("total to pay:",final_bill)
print("thank you for ordering from burger king!")


