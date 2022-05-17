# Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper(*args):
        print(f"you called {function.__name__}{args}")
        total=function(args[0],args[1],args[2])
        print(f"it gave {total}")
    return wrapper


# Use the decorator 👇

def decorator(a,b,c):

