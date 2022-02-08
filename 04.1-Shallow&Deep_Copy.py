import copy 

# Issue with normal copy / shallow copy in  List
list = ["Eating", 23 , ["Breaking Bad", "Money Heist"]]
copy1=list.copy()
print(list,copy1)

copy1[2][1] = "Game of Thrones"
print(list,copy1)  # Did you see this is also changed in 

# This is happening because , point of reference inmemory are same
print(id(copy1[2]))
print(id(list[2]))

# Deep Copy 
c = copy.deepcopy(list)

# Check id 
print("\nDeep Copy Operation \nChecking ID:")
print(id(c[2]))
print(id(list[2]))

# chagin something in c list 
c[2][1]="Mr.ROBOT"
print(list,c)
