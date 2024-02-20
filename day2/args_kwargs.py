# args handling 
def args_function(*args):
    for arg in args:
        print(arg)

args_function(1, 2, 3, 'hello')


# kwargs handling
def kwargs_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

kwargs_function(name='Alice', age=30, city='New York')