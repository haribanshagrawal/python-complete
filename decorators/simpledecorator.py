def simple_decorator(func):
    def wrapper():
        #print("Before the function runs")
        func()
        #print("After the function runs")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

print('----Method 1------')
say_hello()
print('----Method 2-------')
say_hello1=simple_decorator(say_hello)
say_hello1()
