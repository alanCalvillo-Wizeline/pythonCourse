
my_dict = {
    'name': 'Alice', 
    'age': 30, 
    'city': 'New York'
}

print(my_dict)

# using dict constructor 

dict_constructor = dict(name = "John", age = 36, country = "Norway")
print(dict_constructor)


# how to access into the dictionary 
my_dict = {
    'name': 'Alice', 
    'age': 30, 
    'city': 'New York'
}
name = my_dict["name"]
print(name)

# what if I need to be aware of the keys 

keys = my_dict.keys()
print(keys)

# what if I need all the values of this dictionary

values = my_dict.values()
print(values)

# the dictionary is mutable so... 

my_dict['city'] = 'Chicago'
print(my_dict)


# what if we are looking to loop through them using less memory via a tuple 
tuples = my_dict.items()
print(tuples)
