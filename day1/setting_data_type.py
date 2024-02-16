x = str("Hello World")
print(type(x),x)

x = int(20)
print(type(x),x)

x = float(20.5)
print(type(x),x)

x = complex(1j)
print(type(x),x)

x = list(("apple", "banana", "cherry"))	
print(type(x),x)


x = tuple(("apple", "banana", "cherry"))
print(type(x),x)

x = range(6)
print(type(x),x)

x = dict(name="John", age=36)
print(type(x),x)

x = set(("apple", "banana", "cherry"))
x.add("x")
print(type(x),x)

x = frozenset(("apple", "banana", "cherry"))
print(type(x),x)

x = bool(5)
print(type(x),x)

x = bytes(5)
print(type(x),x)

x = bytearray(5)
print(type(x),x)

x = memoryview(bytes(5))
print(type(x),x)
