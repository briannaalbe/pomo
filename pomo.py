from turtle import delay
import larry3d
import settings
import term
import time

# Pomo display example
#############################################################
#         111111111122222222223333333333444444444455555555556
#123456789012345678901234567890123456789012345678901234567890
#############################################################
#    ___       ______                 __           __      
#  /'___`\    /\  ___\      __      /'__`\       /'__`\    
# /\_\ /\ \   \ \ \__/     /\_\    /\ \/\ \     /\ \/\ \   
# \/_/// /__   \ \___``\   \/_/_   \ \ \ \ \    \ \ \ \ \  
#    // /_\ \   \/\ \L\ \    /\_\   \ \ \_\ \    \ \ \_\ \ 
#   /\______/    \ \____/    \/_/    \ \____/     \ \____/ 
#   \/_____/      \/___/              \/___/       \/___/  
#
#    [g]o   [p]ause   [r]estart   [m]ute   [s]ettings
#
#    > 
#
#############################################################

# Timer constants
DIGIT1_X = 0
DIGIT2_X = 13
COLON_X  = 26
DIGIT3_X = 34
DIGIT4_X = 47
DIGIT_Y  = 1
COLON_Y  = 1

# Prompt constants
PROMPT_X = 0
PROMPT_Y = 9

# Fonts
fonts = {"larry3d", "chunky"}

# Globals
muted = False
minutes = 25
seconds = 0

#
#
def printMinutes(mins):
    if (mins > 99) or (mins < 0):
        print("Invalid minutes value")

    minsTensDigit = int(mins / 10)
    minsOnesDigit = mins % 10

    larry3d.printDigit(minsTensDigit, DIGIT1_X, DIGIT_Y)
    larry3d.printDigit(minsOnesDigit, DIGIT2_X, DIGIT_Y)
    larry3d.printColon(COLON_X, COLON_Y)

#
#
# Write a printSeconds

#
#
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
        userSettings()

#
#
def go():
    while (minutes > 0) and (seconds > 0):
        time.sleep(1)

#
#
def pause():
    print("pause")

#
#
def restart():
    print("restart")

#
#
def mute():
    print("mute")
    muted = True

#
#
def unmute():
    print("unmute")
    muted = False

#
#
def userSettings():
    settings.printSettings()

term.clearTerm() 

printMinutes(minutes)
prompt()