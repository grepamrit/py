
from unittest import mock


movies = ["12 Angry Man", "Avenger:Infinity War", "Dune", "Pushpa:The Rise"]

for ew in movies:
    print(ew)  # This prints all movie in new line 

for ew in movies: 
    print(ew, end=" ")  # It will put a space in between the movies name and print in single line 
print()



##### 
for i in range(5):
    print(i, end=" ")    # print i start from count 0 for 5 times 
print()

for i in range(10,15): # 1st Argumet is START and 2nd Argument is STOP 
    print(i, end=" ")
print()

for i in range(100,201,5): # 3rd argument is Step 
    print(i, end=" ")
print()


###############################
# Program to run sum of Number #
###############################
sum = 0 
for i in range(10):
    print(i)
    sum += i 
print("sum of first ", i , "number is: ", sum )


###################################
 # Converting a range in to a List # 
####################################

print(range(10)) # this doesn't give a list 

my_list = list(range(10)) 
print(my_list)


#################################################
# Printing no and name list together using range #
###################################################
movies = ["12 Angry Man", "Avenger:Infinity War", "Dune", "Pushpa:The Rise"]
print("\n")

for i in range(len(movies)):
    print(i, movies[i])
print()





 


