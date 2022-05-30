import os

#
#
def clearTerm():
    os.system('cls' if os.name == 'nt' else 'clear')

def prettyPrint():
    print("")

# Classes/constants containing the escape codes necessary to print
# "pretty" text in an ANSI terminal.
# From: https://www.geeksforgeeks.org/print-colors-python-terminal/
class colors:
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'        

# To use you must instantiate _Getch (e.g. getch = _Getch())
# From: https://code.activestate.com/recipes/134892/
class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()
class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            # An arrow key press returns 3 bytes '\x1b[A', '\x1b[B', '\x1b[C'
            # or '\x1b[D' where A=up, B=down, C=right and D=left. The first 
            # byte is the escaped character sequence '\x1b', the second is 
            # the '[', and the thirds is 'A', 'B', 'C' or 'D'.
            if ch == "\x1b":
                ch += sys.stdin.read(1)
                if ch == "\x1b[":
                    ch += sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()