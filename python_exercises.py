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

# QUESTION - 4
# Solve the questions according to the dictionary structure below.

dict = {"Christian": ["America",18],
        "Daisy": ["England",12],
        "Antonia": ["Spain",22],
        "Dante": ["Italy",25]}

# Step - 1: Access key values

print(dict.keys())

# Step - 2: Access values 

print(dict.values()) 

# Step - 3: Update daisy key 12 to 13

dict.update({"Daisy":["England", 13]})
print(dict)

# Step - 4: Add a new item with key value = Ahmet, value = [Turkey, 24]

dict.update({"Ahmet": ["Turkey", 24]})
print(dict)

# Step - 5: Delete Antonio from the dictionary.

del dict["Antonia"]
print(dict)


# QUESTION - 5:
# Write a function that assigns odd and even numbers in a list to separate lists and returns those list

numbers = [2, 13, 18, 93, 22]

def func(numbers):
    odd = []
    even = []
    for number in numbers:
        if number %2 == 1:
            odd.append(number)
        else:
            even.append(number)
    return odd, even

odd, even = func(numbers)

print(odd)
print(even)


# QUESTION - 6:

# The list given below includes engineering and medical students. Print student classes with the department using "numbering".

students = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for index, student in enumerate(students,):
    if index <= 2:
        print(f"Enginering faculty {index + 1}.student: {student}")
    else:
        print(f"Medicine faculty {index - 2}. student: {student}")


# QUESTION - 7:

# Below are three lists. The lists include course code, credit and quota information, respectively. Print course information using zip.

lesson_code = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
credit = [3, 4, 2, 4]
quota = [30, 75, 150, 25]

for i in zip(lesson_code, credit, quota):
    print(f"Kredisi {i[0]} olan {i[1]} kodlu dersin kontenjanı {i[2]} kişidir.") 


# QUESTION - 8:

# Two sets are given below. Print the extent and difference of the two sets relative to each other.

set1 = set(["data", "python"])
set2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

# inclusivity
print(set1.issuperset(set2)) # False
print(set2.issuperset(set1)) # True

# difference 
print(set1.difference(set2)) # None
print(set2.difference(set1)) # qcut, lambda, python, miuul

# joint
print(set1.intersection(set2)) # python, data 
print(set2.intersection(set1)) # python, data
