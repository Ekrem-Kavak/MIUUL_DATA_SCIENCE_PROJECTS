# QUESTION - 1
# Examine the data structures of the values below
x = 8
y = 3.2
z = 8j + 18
a = "HELLO WORLD"
b = True
c = 23 < 22
l = [1, 2, 3, 4]
d = {"Name": "Jake",
    "Age": 27,
    "Adress":"Downtown"}
t = ("Machine learning", "Data science")
s = {"Pyhton","Machine Learning", "Data Science"}

print(type(x)) # integer
print(type(y)) # float
print(type(z)) # complex
print(type(a)) # string
print(type(b)) # Boolean
print(type(c)) # Boolean
print(type(l)) # list
print(type(d)) # dictionary
print(type(t)) # tuple
print(type(s)) # set


# QUESTION - 2

# Convert all words to uppercase. Substitute spaces for commas and periods.

# text = "The goal is to turn data into information, and information into insight. "
# output = ["THE", "GOAL", "TO", "TURN", "INTO", "INFORMATION", "AND", "INFORMATION", "INTO", "INSIGHT"] 

text = "The goal is to turn data into information, and information into insight."

print(text.upper().replace(",",".").split())

# QUESTION - 3

# Use the following uses to the provided list
# lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Step - 1: Find the number of elements of the list

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

print(len(lst)) 

# Step - 2: Find the elements at index 0 and 10.

print(lst[0]) 
print(lst[10]) 

# Step - 3: Create a list ["D", "A", "T", A"] from the given list.

print(lst[:4])

# Step - 4: Delete the item in the 8th index.

del(lst[8])
print(lst)

# Step - 5: Add a new element.

lst.append("E")
print(lst)

# Step - 6: Add the "N" element back to the 8th index.
 
lst.insert(8,"N")
print(lst) 
