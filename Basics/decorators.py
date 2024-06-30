import time
def squareIt(x):
    return x*x

def doubleIt(x):
    return 2*x

# passing function as object
SqFunc = squareIt
print("SqFunc : ", SqFunc(10))

# Passing the function as an argument
def arithMatic(func):
    result = func(20)
    return result

print("arithMatic Square It : ",arithMatic(squareIt))
print("arithMatic Double It : ",arithMatic(doubleIt))

# nested functions. creating function wrapper to protect it
def modifyvalue(val):
    print("modifyvalue Input : ", val)
    
    def modifier(x):
        return x*x*x
    
    qube = modifier(val)
    print("modifyvalue output = ",qube)

modifyvalue(3)

# --------------------------------------------------------------------------------
# defining a decorator
def my_decorator(func):
    # inner function as wrapper for 
    def wrapper():
        print("my_decorator : before function execution")
        # calling the actual function now
        # inside the wrapper function.
        func()
        print("my_decorator : after function execution")

    return wrapper


# defining a function, to be called inside wrapper
def my_function():
    print("my_function for manual decorator")
# Manually assigning decorator
my_function = my_decorator(my_function)
# calling the function
my_function()

@my_decorator       # my_function_1 passed as func argument to my_decorator which returns new wrapper function 
def my_function_1():
    print("my_function_1 for python decorator")

my_function_1()

# --------------------------------------------------------------------------------
def timestamping(func):
    def wrapper(*arg, **karg):
        start = time.time()
        ret = func(*arg, **karg) 
        end = time.time()
        print("Time for execution of {0} : {1} Sec".format(func.__name__, end-start))
        return ret
    return wrapper


@timestamping  
def function1():
    print("Entry function1")
    time.sleep(2)
    print("Exit function1")
@timestamping
def function2(x,y):
    print("Entry function2")
    z = x+y
    time.sleep(1)
    print("Exit function2")
    return z

function1()
print("Result of function2 = ", function2(10,20))

# --------------------------------------------------------------------------------
# decorator chaining

def squareFunc(func):
    print("squareFunc")
    def wrapper(*arg, **karg):
        x = func(*arg, **karg)
        ret = x * x
        return ret
    return wrapper

def doubleFunc(func):
    print("doubleFunc")
    def wrapper(*arg, **karg):
        x = func(*arg, **karg)
        ret = 2 * x
        return ret
    return wrapper

print("Chaining Decorator : squareFunc, doubleFunc")
@squareFunc     # called 2nd
@doubleFunc     # called 1st
def Testfunction1(val):
    print("Testfunction1 : ", val)
    return val

print("squareFunc, doubleFunc : ", Testfunction1(10))

print("Chaining Decorator : doubleFunc, squareFunc")
@doubleFunc # called 2nd
@squareFunc # called 1st
def Testfunction2(val):
    print("Testfunction2 : ", val)
    return val

print("squareFunc, doubleFunc : ", Testfunction2(10))
