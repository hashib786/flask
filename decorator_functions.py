import time


def decorator_functions(function):
    def inner_functions():
        time.sleep(2)
        function()

    return inner_functions

# ------------------------------
# 1. Way
# def say_hello():
#     print("Hello Hashib")

# calling decorator_functions simple way
# hello_func = decorator_functions(say_hello)
# hello_func()
# ------------------------------

# ------------------------------
# 2. Way


@decorator_functions
def say_hello():
    print("Hello Hashib")


say_hello()
# ------------------------------
