A brainfuck-like esoteric programming language.
Phantasm has unbounded data storage, potential for all arithmetic operations, conditional branching, and is Turing-Complete.

| Shorthand | Name          | Definition                                                                                    |
| --------- | ------------- | --------------------------------------------------------------------------------------------- |
| V         | Value         | A 128-bit signed number                                                                       |
| E         | Entry         | The memory cells that make up the tape and store Vs                                           |
| ME        | Memory Entry  | A single E not on the tape, which a number can be written to                                  |
| MV        | Memory Value  | The V stored within the ME, also commonly referred to as M                                    |
| P         | Pointer       | A specific E on the tape                                                                      |
| PV        | Pointer Value | The V stored within the PE                                                                    |
| LB        | Left Border   | A border (not E) between the leftmost RE and the rightmost LGE                                |
| RB        | Right Border  | A border (not E) between the rightmost RE and the leftmost RGE                                |
| R         | Real          | Es that are on the tape between the LB & RB                                                   |
| G         | Ghost         | Es that are on the tape outside of the LB & RB                                                |
| LC        | Loop Counter  | A V assigned to each RL that tracks passes of the loop<br>Nested RLs have their own unique LC |
| LM        | Loop Memory   | A V assigned to each RL that tracks what the MV was whenthe RL started                        |

R, G, L, and R can be used as prefixes.
	REs are Real Entries
	GEs are Ghost Entries
		LGEs are all GEs to the left of the leftmost RE, RGEs follow suit but to the right

RL is Repetition Loop

| Command | Assembly | Description                                                                                                                                                                                                                            |
| ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| +       | INC      | Increase the PV by 1                                                                                                                                                                                                                   |
| -       | DEC      | Decrease the PV by 1                                                                                                                                                                                                                   |
| (       | LR       | Rotate all RVs left                                                                                                                                                                                                                    |
| )       | RR       | Rotate all RVs right                                                                                                                                                                                                                   |
| /       | LS       | Shift all Vs left                                                                                                                                                                                                                      |
| \       | RS       | Shift all Vs right                                                                                                                                                                                                                     |
| <       | LBI      | Move the LB in one E                                                                                                                                                                                                                   |
| ≤       | LBO      | Move the LB out one E                                                                                                                                                                                                                  |
| >       | RBI      | Move the RB in one E                                                                                                                                                                                                                   |
| ≥       | RBO      | Move the RB out one E                                                                                                                                                                                                                  |
| [       | MI       | MV ≤ 0<br>- jump forward to and continue from the command directly after the corresponding ]                                                                                                                                           |
| ]       | MO       | MV > 0<br>- jump back to and continue from the command directly after the corresponding [                                                                                                                                              |
| {       | RI       | if MV = 0<br>- jump forward to and continue from the command directly after the corresponding }<br>if MV ≠ 0<br>- Set LM to MV and LC to \|MV\|<br>- if MV >0<br>- - enter the loop in LTR<br>- if MV < 0<br>- - enter the loop in RTL |
| }       | RO       | DEC LC by 1<br>add LM-MV to LC<br>if LC = 0<br>- continue to the next command<br>if LC ≠ 0<br>- jump back to and continue from the command directly after the corresponding {                                                          |
| ^       | MW       | Write the PV to the ME                                                                                                                                                                                                                 |
| '       | MZ       | Reset the MV to zero                                                                                                                                                                                                                   |
| .       | OUT      | Output the PV in Unicode                                                                                                                                                                                                               |
| ,       | IN       | Take a Unicode input and write it at the PV                                                                                                                                                                                            |

Change + -
	Vs will overflow or underflow, should the conditions arise
Rotation ( )
	RVs wrap around. The leftmost RV, when Rotated left, will move to the rightmost RE
	GVs are unaffected
Shifting  \\ /
	Ignores the P and Bs
	Every V (apart from the MV) is affected
	This is also the same as shifting the P, LB, and RB one in the opposite direction
Border Movement <≤≥>
	There can never be 2 Bs on the same side of the P, attempting to do so will result in a crash
Writing ^ ,
	The previous V of the E being written to will always be overwritten
Repetition { }
LTR is as normal


Initial State
	The initial state is defined by a number, then a space, then a number at the start of the code
	The numbers signify the amount of Es to the left and right of the P
	For example "1 2" would result in: `... 0 | 0 P0 0 0 | 0 ...`
	If no initial state is included, it will be 0 0, which is `... 0 | P0 | 0 ...`







# Examples

## Repetition Loops
with the initial state of `... 2 2 2 | P2 | 3 3 3 3 ...`
^{^/}

`. . . 2 | P2 | 3 . . .`
^    write 2 to M
`. . . 2 | P2 | 3 . . .` M=2
{    M = 2, set LC to |2| and set LM to 2
`. . . 2 | P2 | 3 . . .` M=2 LC=2 LM=2
^    write 2 to M (redundant for now)
`. . . 2 | P2 | 3 . . .` M=2 LC=2 LM=2
/    left shift
`. . . 2 | P3 | 3 . . .` M=2 LC=2 LM=2
}    DEC LC, INC LC by LC-M (0), set LM to M (2), jump back
`. . . 2 | P3 | 3 . . .` M=2 LC=1 LM=2
^    write 3 to M
`. . . 2 | P3 | 3 . . .` M=3 LC=1 LM=2
/    left shift
`. . . 2 3 | P3 | 3 . . .` M=3 LC=1 LM=2
}    DEC LC, INC LC by LC-M (1), set LM to M, jump back
`. . . 2 3 | P3 | 3 . . .` M=3 LC=2 LM=3
the rest is unimportant, as it just writes 3 to M, which is already 3, and left shifts for a bit