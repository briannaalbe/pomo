import larry3d

DIGIT1_X = 0
DIGIT2_X = 13
COLON_X  = 26
DIGIT3_X = 34
DIGIT4_X = 47
DIGIT_Y  = 1
COLON_Y  = 1
PROMPT_X = 0
PROMPT_Y = 9

fonts = {"larry3d", "chunky"}

muted = False

def prompt():
    if not muted:
        print("\033[%d;%dH    [g]o   [p]ause   [r]estart   [m]ute   [s]ettings" % (PROMPT_Y, PROMPT_X))
    else:
        print("\033[%d;%dH   [g]o   [p]ause   [r]estart   [u]nmute   [s]ettings" % (PROMPT_Y, PROMPT_X))

    print("")
    command = input("    > ")
    command = command.lower()
    if (command == "g") or (command == "go"):
        go()
    elif (command == "p") or (command == "pause"):
        pause()
    elif (command == "r") or (command == "restart"):
        restart()
    elif ((command == "m") or (command == "mute")) and not muted:
        mute()
    elif ((command == "u") or (command == "unmute")) and muted:
        unmute()
    elif (command == "s") or (command == "settings"):
        settings()

def go():
    print("go")

def pause():
    print("pause")

def restart():
    print("restart")

def mute():
    print("mute")
    muted = True

def unmute():
    print("unmute")
    muted = False

def settings():
    print("settings")

larry3d.clearTerm()

larry3d.print2(DIGIT1_X, DIGIT_Y)
larry3d.print5(DIGIT2_X, DIGIT_Y)
larry3d.printColon(COLON_X, COLON_Y)
larry3d.print0(DIGIT3_X, DIGIT_Y)
larry3d.print0(DIGIT4_X, DIGIT_Y)

prompt()
