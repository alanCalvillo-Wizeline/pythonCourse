
name = 'alan'
id = 10



# https://docs.python.org/3/library/stdtypes.html#old-string-formatting 
# old way to print 
print('Hello, %s' % name)

# if we have multiple variables 

print('Hey %(name)s, there is a task with this id: %(id)d' % {"name": name, "id": id })




# str.format(name)

print('Hello, {}'.format(name))

# if we have multiple variables 

print('Hey {name}, there is a task with this id: {id}'.format(name=name, id=id))



# f-Strings

print(f'Hello, {name}!')

print(f'Hey {name}, there is a task with this id: {id}')

# using f-strings allows us to execute simple operations in there

a = 10 
b = 1

print(f'Hey {name}, there is a task with this id: {id} it will take {a + b } mins to be solved')


