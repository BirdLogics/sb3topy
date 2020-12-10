"""

"""

def recurse_error(i):
    print(i)
    while i:
        if i:
            # This function should call itself
            # Another function calling this function
            # from within this one halves the recursion
            # depth since two functions are adding to it
            recurse_error2(i+1) # wrong
            recurse_error(i+1) # correct

def recurse_error2(i):
    recurse_error(i)

recurse_error(1)