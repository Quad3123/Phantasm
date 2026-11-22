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



loopStack = []









code = input()

if len(code) == 0: print("ERROR: no code") ; quit() # quits if there's no code
if code[0].isdecimal(): # if theres a header... this assumes that if the first character is a number it must be the header and not a comment
    match = re.match(r"^(\d+)\s+(\d+)(.*)$", code) # splits up the parts
    if match: headerLeft, headerRight, code = match.groups() ; headerLeft = int(headerLeft) ; headerRight = int(headerRight)
    else: headerLeft = headerRight = 0
else:
    headerLeft = headerRight = 0

code = ''.join(char for char in code if char in validCommands)


for i in range(len(code)):
    if code[i] == "[": loopStack.append("]") # if the start of a pointer loop is found, push its inverse to the loop stack
    if code[i] == "{": loopStack.append("}") # same for memory loops
    if code[i] == "]" or code[i] == "}": # if the end of a loop is found
        if len(loopStack) == 0: print("ERROR: loop closed when none was opened") ; quit()
        elif code[i] != loopStack.pop(): print("ERROR: mismatched brackets") ; quit()





if len(loopStack) > 0: print("ERROR: unclosed loop") ; quit() # quits if any loops are left open





