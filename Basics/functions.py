
# function accepting and returning no values
def my_print():
    print("welcome ")

         
def add(n1,n2):
# def add(num1: int, num2: int) -> int:
    """Add two numbers"""
    n3 = n1 + n2
    return n3

# default arguments
def my_add(n1,n2=10):
# def add(num1: int, num2: int) -> int:
    """Add two numbers"""
    n3 = n1 + n2
    return n3



# same name cannot be used as function overloading not possible in python
# import package -> from multipledispatch import dispatch
# @dispatch(str)
# def my_print(msg):
def my_msg_print(msg): 
    print("welcome ", msg)
    print("welcome -> {0}".format(msg))

# Annotation example : adding metadata to function parameters and return type
def greet(name: str)-> str:
    return f"Hello, {name}"


# pass by value
def pass_by_value(x):
    x = 5
    return x

# pass by value : list tuple maps are always pass by ref
def pass_by_ref(lst):
    lst[0] = 100

strMsg = "global"
def scope_global():
    global strMsg # if this line removed then
    strMsg = "make it local" # strMsg will be local variable and global strMsg will not be updated.


# Defining main function 
def main(): 
    print("Inside Main") 
    my_print()
    my_msg_print("message")

    num1, num2 = 5, 15
    ans = add(num1, num2)
    print(f"The addition of {num1} and {num2} results {ans}.")  # f-> format

    print("my_add = ", my_add(12))

    print("greet : ", greet("John"))
  
    x = 10
    print("before pass by value : x = {0}| pass by value x = {1} |after pass_by_value : x = {2}".format(x, pass_by_value(x), x))

    x = [1,2,3,4,5]
    print("before pass by ref : x = {0}".format(x))
    pass_by_ref(x)
    print("after pass by ref : x = {0}".format(x))

    print("before scope_global: strMsg = ", strMsg)
    scope_global()
    print("before scope_global: strMsg = ", strMsg)

""" Since there is no main() function in Python, when the command to run a Python program is given to the interpreter, 
the code that is at level 0 indentation is to be executed. 
However, before doing that, it will define a few special variables. __name__ is one such special variable. 
If the source file is executed as the main program, the interpreter sets the __name__ variable to have a value __main__. 
If this file is being imported from another module, __name__ will be set to the module’s name.
__name__ is a built-in variable which evaluates to the name of the current module."""
# when run as 'python function.py' on terminal the variable __name__ will be populated to __main__. 
if __name__=="__main__": 
    main() 