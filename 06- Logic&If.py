# Getting Infomration 
print("Hi there !")
print("Can you let us know what is your age ?:")
age = int(input())

# Condition

if age >= 65:
    print("Hey, you get a special discount")
elif age == 21: 
    print("SUPER SPECIAL !")
elif age > 20:
    print("Welcome to our app!")
else: 
    print("You're not age enough to use our app. ")

print("Thank you for using out App :)")

# AND Operators 
subscribe = True
hit_like = False 

if subscribe and hit_like:  # If one of them is false then it will be false
    print("Welcome")
else:
    print("You either forget to subscribe or hit like buttom")

# OR Operator , if will be true if one of them is true 
# NOT Operator , it negated the state 
liked = True 
print(not liked) # This will print false 
