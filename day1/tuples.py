record = ("Test User", 35, "Python Developer")

print(record)
print(record[0])
print(record[1])
print(record[2])

print('-----------------------------------------------------')

for idx,value in enumerate(record):
    print(idx,value)

print('-----------------------------------------------------')


days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

print(days)
print('-----------------------------------------------------')


data = tuple(["Jane Doe", 25, 1.75, "Canada"])

print(data)

print('-----------------------------------------------------')

data = tuple("Pythonista")

print(data)


print('-----------------------------------------------------')

data = tuple({
    "manufacturer": "Boeing",
    "model": "747",
    "passengers": 416,
}.values())

print(data)