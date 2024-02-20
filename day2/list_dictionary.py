my_list = [
	{
		'foo':12,
		'bar':14
	},
	{
		'foo':52,
		'bar':641
	},
	{
		'foo':6,
		'bar':84
	}
]

print(my_list)

my_list.append({
    'foo': 10,
    'bar': 12
})

print(my_list)

# using enumareate to loop through the array of dictionaries 

for key,element in enumerate(my_list):
    print(f"{key} {element}")
    print(element['foo'])
    print(element['bar'])