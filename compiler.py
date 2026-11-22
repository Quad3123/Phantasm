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





C_RUNTIME_HEADER = """#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

typedef __int128 i128;
typedef unsigned __int128 u128;

i128 *tape = NULL;
size_t cap = 0;
size_t P = 0, LB = 0, RB = 0;
i128 M = 0;

u128 abs128(i128 x) {
    return x < 0 ? -(u128)x : (u128)x;
}

void check_borders(void) {
    if (LB > P || RB < P) {
        fprintf(stderr, "ERROR: two borders on the same side of P\n");
        exit(1);
    }
}

void init_tape(size_t left_hdr, size_t right_hdr) {
    cap = left_hdr + right_hdr + 1024;
    tape = calloc(cap, sizeof(i128));
    P = cap / 2;
    LB = P - left_hdr;
    RB = P + right_hdr;
}

void ensure_bounds(void) {
    if (LB <= 2 || P <= 2 || RB >= cap - 3 || P >= cap - 3) {
        size_t new_cap = cap * 2;
        size_t offset = cap / 2;
        i128 *new_tape = calloc(new_cap, sizeof(i128));
        memcpy(new_tape + offset, tape, cap * sizeof(i128));
        free(tape);
        tape = new_tape;
        cap = new_cap;
        P += offset;
        LB += offset;
        RB += offset;
    }
}

void shift_left(void) {
    P++; LB++; RB++;
    ensure_bounds();
}

void shift_right(void) {
    ensure_bounds();
    P--; LB--; RB--;
}

void rotate_left(void) {
    if (LB >= RB) return;
    i128 first = tape[LB];
    memmove(&tape[LB], &tape[LB + 1], (RB - LB) * sizeof(i128));
    tape[RB] = first;
}

void rotate_right(void) {
    if (LB >= RB) return;
    i128 last = tape[RB];
    memmove(&tape[LB + 1], &tape[LB], (RB - LB) * sizeof(i128));
    tape[LB] = last;
}

void out_unicode(i128 val) {
    uint32_t c = (uint32_t)val;
    if (c <= 0x7F) {
        putchar(c);
    } else if (c <= 0x7FF) {
        putchar(0xC0 | (c >> 6));
        putchar(0x80 | (c & 0x3F));
    } else if (c <= 0xFFFF) {
        putchar(0xE0 | (c >> 12));
        putchar(0x80 | ((c >> 6) & 0x3F));
        putchar(0x80 | (c & 0x3F));
    } else if (c <= 0x10FFFF) {
        putchar(0xF0 | (c >> 18));
        putchar(0x80 | ((c >> 12) & 0x3F));
        putchar(0x80 | ((c >> 6) & 0x3F));
        putchar(0x80 | (c & 0x3F));
    }
    fflush(stdout);
}

i128 in_unicode(void) {
    int c = getchar();
    if (c == EOF) return 0;
    if ((c & 0x80) == 0) return c;
    int extra = 0;
    uint32_t res = 0;
    if ((c & 0xE0) == 0xC0) { extra = 1; res = c & 0x1F; }
    else if ((c & 0xF0) == 0xE0) { extra = 2; res = c & 0x0F; }
    else if ((c & 0xF8) == 0xF0) { extra = 3; res = c & 0x07; }
    for (int i = 0; i < extra; i++) {
        int next = getchar();
        if (next == EOF) return 0;
        res = (res << 6) | (next & 0x3F);
    }
    return (i128)res;
}"""