print("Hey, What's your name?: ")
name = input()
print("Hi," + name)

print("\nWhat's you favourite number? :")
num1= input()
print("Give us another one:")
num2= input()
print("Adding two of your fav no:", num1+num2) # This is concanating cause its srting , letc check
print(type(num1))
print(type(num2))


# Lets do this Way
print ("\nAnother way: ")
print("What's you favourite number? :")
num1= int(input()) # converting input to integer  
print("Give us another one:")
num2= int(input())
print("Adding two of your fav no:", num1+num2) # This is concanating cause its srting , letc check
print(type(num1))
print(type(num2))
