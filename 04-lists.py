# LISTS 

ages = [13,14,15]
people = ["Sam", "Shiv", "Seri"]
my_favourite_things = ["Working out", 10 , ["12 Angry man", "Trace"]]


print(ages)
print(people)
print(my_favourite_things)

# Lists are not immutable like strings, lets test it 
my_favourite_things[0]= "Walking"
print(my_favourite_things)

print(len(my_favourite_things))

# Copy a LIST to another list 
new_list=my_favourite_things[:] # my_favourite_things[:] is same as my_favourite_things
new_list[0]= "Dancing"
print(new_list,my_favourite_things)

my_list=my_favourite_things[2] 
print(my_list, len(my_list))

# Another way of copying 
another_list=my_list.copy()
print(another_list)

# Nested list 
nested_list=["Coding", 20 , ["Batman", ["Thor","Endgame"], "Dune"]]
print(nested_list[2]) # This print the list inside the list in 2th position
print(nested_list[2][1]) # print 2nd of main list and then 2nd postion of that list
print(nested_list[2][1][0]) # This prints Thor


# Issue with normal copy / shallow copy in  List
print("\n Issue with shallow Copy ")
list = ["Eating", 23 , ["Breaking Bad", "Money Heist"]]
copy1=list.copy()
print(list,copy1)

copy1[2][1] = "Game of Thrones"
print(list,copy1)  # Did you see this is also changed in 

# This is happening because , point of reference inmemory are same
print(id(copy1[2]))
print(id(list[2]))


# Combile List 

print("\nCombinging Lists: ")
my_favourite_things = ["Working out", 10 , ["12 Angry man", "Trance"]]
least_favourite_things = ["oninios", "JAVA"]

print(my_favourite_things + least_favourite_things) # combining two lists 

least_favourite_things = least_favourite_things + ["Video Editing"]
least_favourite_things.append("Washing Dish")  # A convinenet way to appedning data in list 
print(least_favourite_things)

