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





validCommands = {
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
    ","}











code = input()

if len(code) == 0: print("ERROR: no code") ; quit() # makes sure there's actually code
if code[0].isdecimal(): # if theres a header... this assumes that if the first character is a number it must be the header and not a comment
    match = re.match(r"^(\d+)\s+(\d+)(.*)$", code) # splits up the parts
    if match: headerLeft, headerRight, code = match.groups() ; int(headerLeft) ; int(headerRight)

code = ''.join(char for char in code if char in validCommands)

print(code)









while True:continue # for testing, so python doesnt close immediately when i run it