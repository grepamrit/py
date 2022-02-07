## STRINGS 

msg = "Hi Everyone"
print(msg)  # Simple string print 

print ("Hi\nThere, \t How are you? ") # \n for new line and \t for tab

# print \t and \n and " 
print ("He said, \" This is actually cool \"")
print("You can use \\t for a tab & \\n for a new line")

## Double Quote and Single Quote, you can use anything you want
print("Hey")
print('Hi')

# Concatenation 
msg1 = "Hi there,"
msg2 = "how you doing today? "
print(msg1+" "+ msg2)
print(msg1 + "Sam!")

# multiline string 
multiline = """
when i see you 
my heart sing a sing \
a love song 
Happy ! Happy ! :) 
"""
print(multiline)


# Indexes 
poem = "Where am I?"
print(poem[4])
print(poem[-1])   # print last value 
print(poem[-5])   # do indexing from right side

# Slicing 
print(poem[6:])  # slice a string after 6th position 6-end
print(poem[:5])  # slice a string upto 5th position 0-5
print(poem[1:3]) # slice a sting 1-3 postion i.e 1th and 2nd 

print(poem[:-6])
print(poem[-5:])

print(poem[6:-1])  # In x:y , x is inlcusive & y is exclusive 

start = 6 
print(poem[start:start+5])  # can use this trick as well, which seems preety well for understanding

# String Memory 
task = "Learn"
print(id(task))  # shows sting memory store id 

task = "Okey"
print(id(task))


# Strings Function 

msg="Please go away"
print(len(msg))   # total length=index+1 , since index count from 0
print(msg[13])

# converting int to str 
print("Your message was " + str(len(msg)) + " character long")
print("Your message was",str(len(msg)),"character long")
# here its passing them as seperate argument which is different than previous print section where concatenation is happpening and string can not concanate wirh int






