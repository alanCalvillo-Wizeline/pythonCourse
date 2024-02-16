
name = 'alan'
id = 10



# https://docs.python.org/3/library/stdtypes.html#old-string-formatting 
# old way to print 
print('Hello, %s' % name)

# if we have multiple variables 

print('Hey %(name)s, there is a task with this id: %(id)d' % {"name": name, "id": id })


print('-----------------------------------------------------')


# str.format(name)

print('Hello, {}'.format(name))

# if we have multiple variables 

print('Hey {name}, there is a task with this id: {id}'.format(name=name, id=id))

print('-----------------------------------------------------')

# f-Strings

print(f'Hello, {name}!')

print(f'Hey {name}, there is a task with this id: {id}')

# using f-strings allows us to execute simple operations in there

a = 10 
b = 1

print(f'Hey {name}, there is a task with this id: {id} it will take {a + b } mins to be solved')

print('-----------------------------------------------------')


# split

string = "Hello, World!"
string_split = string.split(",")

print(string_split)
print('-----------------------------------------------------')


# join 

string_join = " ".join(string_split)
print(string_join)
print('-----------------------------------------------------')



# replace

string = "Hello World!"
string_love = string.replace("Hello", "Good Bye")

print(string_love)
print('-----------------------------------------------------')


# strip 

string = "   Hello World!   "
string_no_space = string.strip()

print(string_no_space) 
print('-----------------------------------------------------')

# upper | lower

string = "this is A Test"
print(string.upper())
print(string.lower())
print(string)
print('-----------------------------------------------------')