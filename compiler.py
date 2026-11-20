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




# IMPORTS
import re





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










# takes in the code and checks it's valid
code = input()

if len(code) == 0: print("ERROR: no code") ; quit()
if code[0].isdecimal(): # gets the header, if there is one
    match = re.match(r"^(\d+)\s+(\d+)(.*)$", code)
    if match: headerLeft, headerRight, code = match.groups() ; int(headerLeft) ; int(headerRight)






# more validation
if not code[0].isdecimal(): print("ERROR: invalid start") ; quit()
if not code.startswith(tuple(validCommands)): print("ERROR: ")