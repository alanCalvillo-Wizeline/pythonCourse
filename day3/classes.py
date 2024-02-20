class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def return_data(self):
        return {
            "name" : self.name,
            "age" : self.age
        }

    def print_data(self):
        print(f"name: {self.name}, age: {self.age}")

class Student(Person):
    def __init__(self,name,age,university):
        super().__init__(name,age)
        self.university = university

    def welcome(self):
        print(f"name:{self.name}, age:{self.age}, university:{self.university}")

class PublicAttributesStudent:
    schoolName = 'XYZ School' # class attribute

    def __init__(self, name, age):
        self.name=name # instance attribute
        self.age=age # instance attribute

class ProtectedStudent:
    _schoolName = 'XYZ School' # protected class attribute
    
    def __init__(self, name, age):
        self._name=name  # protected instance attribute
        self._age=age # protected instance attribute

class PrivateStudent:
    __schoolName = 'XYZ School' # private class attribute

    def __init__(self, name, age):
        self.__name=name  # private instance attribute
        self.__salary=age # private instance attribute
    def __display(self):  # private method
	    print('This is private method.')





# regular class usage 
p1 = Person("John", 36)
print(p1.return_data())
p1.print_data()


# class Inheritance
s1 = Student("John", 22, 'itesm')
s1.welcome()


# public attributes usage 
std = PublicAttributesStudent("Steve", 25)
print(std.schoolName)  #'XYZ School'
print(std.name)  #'Steve'
print(std.age)  #'age before mutate it'
std.age = 20
print(std.age)

# protected attributes usage
std = ProtectedStudent("Swati", 25)
print(std._name)  #'Swati'

std._name = 'Dipa'
print(std._name)  #'Dipa'

'''
# private attributes usage
std = PrivateStudent("Bill", 25)
print(std.__schoolName) #AttributeError
print(std.__name)   #AttributeError
print(std.__display())  #AttributeError

'''