import term

def test():
    getch = term._Getch()
    ch = getch()
    if ch == "\x1a":
        print("a")
    elif ch == "\x1b":
        print("b")
    elif ch == "\x1c":
        print("c")
    elif ch == "\x1d":
        print("d")

def printSettings():
    #print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    term.clearTerm()
    print("")
    print("   Intervals (focus/break):   25/5   50/10")
    print("")
    print("   Cycles:   1   2   3   4   5   6   7   8   9")
    print("")
    print("   DONE   CANCEL")

def lineIndicator(x, y):
    print("\033[%d;%dH>" % (y, x))