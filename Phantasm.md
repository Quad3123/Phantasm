A brainfuck-like esoteric programming language.  
Phantasm has unbounded data storage, potential for all arithmetic operations, conditional branching, and is Turing-Complete.

| Shorthand | Name          | Definition                                                                                                  |
| --------- | ------------- | ----------------------------------------------------------------------------------------------------------- |
| V         | Value         | A 128-bit signed number                                                                                     |
| E         | Entry         | The memory cells that make up the tape and store Vs                                                         |
| ME        | Memory Entry  | A single E not on the tape, which a number can be written to                                                |
| MV        | Memory Value  | The V stored within the ME, commonly referred to as M                                                       |
| P         | Pointer       | A specific E on the tape                                                                                    |
| PV        | Pointer Value | The V stored within the PE                                                                                  |
| LB        | Left Border   | A border (not E) between the leftmost RE and the rightmost LGE                                              |
| RB        | Right Border  | A border (not E) between the rightmost RE and the leftmost RGE                                              |
| R         | Real          | Es that are on the tape between the LB & RB                                                                 |
| G         | Ghost         | Es that are on the tape outside of the LB & RB                                                              |
| LC        | Loop Counter  | A 32-bit unsigned V assigned to each RL that tracks passes of the loop. Nested RLs have their own unique LC |
| LM        | Loop Memory   | A V assigned to each RL that tracks what the MV was whenthe RL started                                      |

R, G, L, and R can be used as prefixes.
- REs are Real Entries
- GEs are Ghost Entries
- LGEs are all GEs to the left of the leftmost RE, RGEs follow suit but to the right

RL is Repetition Loop

| Command | Assembly                | Description                                                                                                                                                                                                                                |
| ------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| +       | INC<br>INCrement        | Increase the PV by 1                                                                                                                                                                                                                       |
| -       | DEC<br>DECrement        | Decrease the PV by 1                                                                                                                                                                                                                       |
| (       | LR<br>Rotate Left       | Rotate all RVs left                                                                                                                                                                                                                        |
| )       | RR<br>Rotate Right      | Rotate all RVs right                                                                                                                                                                                                                       |
| /       | LS<br>Shift Left        | Shift all Vs left                                                                                                                                                                                                                          |
| \       | RS<br>Shift Right       | Shift all Vs right                                                                                                                                                                                                                         |
| <       | BLI<br>Border Left In   | Move the LB in one E                                                                                                                                                                                                                       |
| ≤       | BLO<br>Border Left Out  | Move the LB out one E                                                                                                                                                                                                                      |
| >       | BRI<br>Border Right In  | Move the RB in one E                                                                                                                                                                                                                       |
| ≥       | BRO<br>Border Right Out | Move the RB out one E                                                                                                                                                                                                                      |
| [       | LPI<br>Loop Pointer In  | PV ≤ 0<br>- jump forward to and continue from the command directly after the corresponding ]                                                                                                                                               |
| ]       | LPO<br>Loop Pointer Out | PV > 0<br>- jump back to and continue from the command directly after the corresponding [                                                                                                                                                  |
| {       | LMI<br>Loop Memory In   | if MV = 0<br>- jump forward to and continue from the command directly after the corresponding }<br>if MV ≠ 0<br>- Set LM to MV and LC to \|MV\|<br>- if MV >0<br>- - enter the loop normally<br>- if MV < 0<br>- - enter the loop Inverted |
| }       | LMO<br>Loop Memory Out  | DEC LC by 1<br>add \|LM\|-\|MV\| to LC<br>if LC = 0<br>- continue to the next command<br>if LC ≠ 0<br>- jump back to and continue from the command directly after the corresponding {                                                      |
| ^       | MW<br>Memory Write      | Write the PV to the ME                                                                                                                                                                                                                     |
| '       | MZ<br>Memory Zero       | Reset the MV to zero                                                                                                                                                                                                                       |
| .       | OUT<br>OUTput           | Output the PV in Unicode                                                                                                                                                                                                                   |
| ,       | IN<br>INput             | Take a Unicode input and write it at the PV                                                                                                                                                                                                |

#### Change + -
Vs will overflow or underflow, should the conditions arise
#### Rotation ( )
RVs wrap around. The leftmost RV, when Rotated left, will move to the rightmost RE  
GVs are unaffected
#### Shifting  \\ /
Ignores the P and Bs  
Every V (apart from the MV) is affected  
This is also the same as shifting the P, LB, and RB one in the opposite direction
#### Border Movement <≤≥>
There can never be 2 Bs on the same side of the P, attempting to do so will result in a crash
#### Writing ^ ,
The previous V of the E being written to will always be overwritten
#### Memory Loops { }
when the loop begins, 2 special values are assigned to both brackets  
- LC, or Loop Counter  
- LM, or Loop Memory  

LC keeps track of how many loops there are remaining to execute, and can be changed with the help of the LM  
LM never changes throughout the loop, and is the V that M was at the start of the loop
  
if MV < 0, the loop is executed Inverted  
Inverted execution changes:  

| +   | -   |
| --- | --- |
| (   | )   |
| /   | \   |
| <   | >   |
| ≤   | ≥   |

so `+/[-]` would become `-\[+]`




#### Initial State
The initial state is defined by a number, then a space, then a number, then the ret of the code  
these numbers are known as Headers  
The Headers signify the amount of Es to the left and right of the P  
For example "1 2codeGoesHere" would result in: `... 0 | 0 P0 0 0 | 0 ...`  
If no initial state is included, such as "code" it will be treated as "0 0code"  
which is `... 0 | P0 | 0 ...`







# Examples
## Idioms
Idioms are small command-like structures  

#### `[-]`  
sets P to 0 if it's positive  
if P < 0, nothing happens
#### `[+]`
sets P to 0 if it's negative  
if P > 0, nothing happens
#### `^{-}'`
sets P to 0
does reset M to 0 though
## Arithmetic

### Two Number Adder
`,^{-},{+}.`  
this is the first program I ever made , which can add 2 inputs  

`,^{-},`  
write the first input input at P  
write it to M  
reset P to 0 so there's no interference  
write the second input at P  
you now have the first input in M and the second in P  
`{+}.`  
if M is positive, increments P M times  
if M is negative, decrements P M times  
outputs P


