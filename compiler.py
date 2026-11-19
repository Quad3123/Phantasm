# this is going to be super messy bc im far from a pro at python
# i used NO ai to generate this code at all


# if you can see this, im still working on the compiler




# TO DO
# 
# uhhhhhhh
#
#
#
#
#
#
#


validCommands = [
    "+",
    "-",
    "(",
    ")",
    "/",
    "\\", # have to put 2 backslashes here bc python
    "<",
    "≤",
    ">",
    "≥",
    "[",
    "]",
    "{",
    "}",
    "^",
    "'",
    ".",
    ","]











code = input()

if len(code) == 0: print("ERROR: no code") ; quit()
if not code[0].isdecimal() and not code.startswith(tuple(validCommands)): print("ERROR: invalid start") ; quit()