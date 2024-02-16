# Print a string 

first_name, age, job = "John", 33, "programmer"
 
# Method 1: String Concatenation
print(first_name + " " + "is a" + " " + str(age) + " " + "year old" + " " + job)
 
# Method 2: % Conversion specifier
print("%s is a %d year old %s" % (first_name, age, job))
 
# Method 3: Using format: Until Python 3.6
print("{0} is a {1} year old {2}".format(first_name, age, job))
 
# Method 4: The Pythonic Way: From Python 3.6 and above
print(f"{first_name} is a {age} year old {job}")

print('-----------------------------------------------------')


# loop on a string 

# Method 1
greet = "hello"
i = 0
for eachChar in greet:
    print(i, eachChar)
    i += 1

print('*****************************************************')

# Method 2: A better way
greet = "there"
for idx in range(len(greet)):
    print(idx, greet[idx])

print('*****************************************************')
 
# Method 3: The Pythonic way: enumerate()
greet = "again"
for idx, eachChar in enumerate(greet):
    print(idx, eachChar)