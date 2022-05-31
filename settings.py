import term

# Settings display example
#############################################################
#         111111111122222222223333333333444444444455555555556
#123456789012345678901234567890123456789012345678901234567890
#############################################################
#
# >> [i]ntervals (focus/break):   25/5   50/10
#
#    [c]ycles:   1   2   3   4   5   6   7   8   9
#
#    [d]one   [n]evermind
#
#############################################################

# Line indicator constants
LINE_INDICATOR_X        = 2

# Intervals line constants
INTERVALS_25_5_X        = 32
INTERVALS_50_10_X       = 39
INTERVALS_Y             = 2

# Cycles line constants
CYCLES_Y                = 4

# Done nevermind line constants
DONE_NVM_INDICATOR_Y    = 6

#
#
def printSettings():
    term.clearTerm()
    print("")
    print("    [i]ntervals (focus/break):   25/5   50/10")
    print("")
    print("    [c]ycles:   1   2   3   4   5   6   7   8   9")
    print("")
    print("    [d]one   [n]evermind")
    printLineIndicator(LINE_INDICATOR_X, INTERVALS_Y)

    while True:
        getch = term._Getch()
        ch = getch()
        if   ch == "\x1b[A":
            print("up")
        elif ch == "\x1b[B":
            print("down")
        elif ch == "\x1b[C":
            print("right")
        elif ch == "\x1b[D":
            print("left")

#
#
def printLineIndicator(x, y):
    print("\033[%d;%dH>>" % (y, x))