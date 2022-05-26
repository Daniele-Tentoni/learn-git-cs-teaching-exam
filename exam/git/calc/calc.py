"""Complete the main function to invoke functions to perform simple calc
operations.

For example:
1. Invoke the program with arguments: ['div', 10, 2.5]
2. Expect to see printed in the standard output '4'

Expect only the operations defined in the help tip that you can read by
invoking this program giving as argument '-h' and only valid inputs that don't
produce any unexpected result.
"""

import sys
import textwrap

def sum(first: float, second: float) -> float:
    pass

def main(*args):
    if "-h" in args or len(args) != 4:
        print(textwrap.dedent("""\
            usage: python3 calc.py [-h] {div, mul, sub, sum} <arg1> <arg2>
            subcommands:
                div: make a division between a dividend (arg1) and a divisor (arg2)
                mul: make a multiplication between (arg1) and (arg2)
                sub: make a subtraction between (arg1) and (arg2)
                sum: make a sum between (arg1) and (arg2)
            """))
        return

    match args[1]:
        case "sum":
            pass
        case fail:
            print(f"Unsupported operation {fail}")

if __name__ == "__main__":
    main(*sys.argv)
