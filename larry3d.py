import os

# larry3d
#    _        ___        __      __ __       ______      ____     ________    __        __         __
#  /' \     /'___`\    /'__`\   /\ \\ \     /\  ___\    /'___\   /\_____  \ /'_ `\    /'_ `\     /'__`\
# /\_, \   /\_\ /\ \  /\_\L\ \  \ \ \\ \    \ \ \__/   /\ \__/   \/___//'/'/\ \L\ \  /\ \L\ \   /\ \/\ \
# \/_/\ \  \/_/// /__ \/_/_\_<_  \ \ \\ \_   \ \___``\ \ \  _``\     /' /' \/_> _ <_ \ \___, \  \ \ \ \ \
#    \ \ \    // /_\ \  /\ \L\ \  \ \__ ,__\  \/\ \L\ \ \ \ \L\ \  /' /'     /\ \L\ \ \/__,/\ \  \ \ \_\ \
#     \ \_\  /\______/  \ \____/   \/_/\_\_/   \ \____/  \ \____/ /\_/       \ \____/      \ \_\  \ \____/
#      \/_/  \/_____/    \/___/       \/_/      \/___/    \/___/  \//         \/___/        \/_/   \/___/
# https://rosettacode.org/wiki/Terminal_control/Cursor_positioning#Python

def move (x, y):
    print("\033[%d;%dHtest" % (y, x))

def clearTerm():
    os.system('cls' if os.name == 'nt' else 'clear')

def print0(x, y):
    print("\033[%d;%dH    __      " % (y, x))
    print("\033[%d;%dH  /'__`\    " % (y + 1, x))
    print("\033[%d;%dH /\ \/\ \   " % (y + 2, x))
    print("\033[%d;%dH \ \ \ \ \  " % (y + 3, x))
    print("\033[%d;%dH  \ \ \_\ \ " % (y + 4, x))
    print("\033[%d;%dH   \ \____/ " % (y + 5, x))
    print("\033[%d;%dH    \/___/  " % (y + 6, x))

def print1(x, y):
    print("\033[%d;%dH     _      " % (y, x))
    print("\033[%d;%dH   /' \     " % (y + 1, x))
    print("\033[%d;%dH  /\_, \    " % (y + 2, x))
    print("\033[%d;%dH  \/_/\ \   " % (y + 3, x))
    print("\033[%d;%dH     \ \ \  " % (y + 4, x))
    print("\033[%d;%dH      \ \_\ " % (y + 5, x))
    print("\033[%d;%dH       \/_/ " % (y + 6, x))

def print2(x, y):
    print("\033[%d;%dH    ___     " % (y, x))
    print("\033[%d;%dH  /'___`\   " % (y + 1, x))
    print("\033[%d;%dH /\_\ /\ \  " % (y + 2, x))
    print("\033[%d;%dH \/_/// /__ " % (y + 3, x))
    print("\033[%d;%dH    // /_\ \\" % (y + 4, x))
    print("\033[%d;%dH   /\______/" % (y + 5, x))
    print("\033[%d;%dH   \/_____/ " % (y + 6, x))

def print3(x, y):
    print("\033[%d;%dH    __      " % (y, x))
    print("\033[%d;%dH  /'__`\    " % (y + 1, x))
    print("\033[%d;%dH /\_\L\ \   " % (y + 2, x))
    print("\033[%d;%dH \/_/_\_<_  " % (y + 3, x))
    print("\033[%d;%dH   /\ \L\ \ " % (y + 4, x))
    print("\033[%d;%dH   \ \____/ " % (y + 5, x))
    print("\033[%d;%dH    \/___/  " % (y + 6, x))

def print4(x, y):
    print("\033[%d;%dH __ __      " % (y, x))
    print("\033[%d;%dH/\ \\\\ \     " % (y + 1, x))
    print("\033[%d;%dH\ \ \\\\ \    " % (y + 2, x))
    print("\033[%d;%dH \ \ \\\\ \_  " % (y + 3, x))
    print("\033[%d;%dH  \ \__ ,__\\" % (y + 4, x))
    print("\033[%d;%dH   \/_/\_\_/" % (y + 5, x))
    print("\033[%d;%dH      \/_/  " % (y + 6, x))

def print5(x, y):
    print("\033[%d;%dH  ______    " % (y, x))
    print("\033[%d;%dH /\  ___\   " % (y + 1, x))
    print("\033[%d;%dH \ \ \__/   " % (y + 2, x))
    print("\033[%d;%dH  \ \___``\ " % (y + 3, x))
    print("\033[%d;%dH   \/\ \L\ \\" % (y + 4, x))
    print("\033[%d;%dH    \ \____/" % (y + 5, x))
    print("\033[%d;%dH     \/___/ " % (y + 6, x))

def print6(x, y):
    print("\033[%d;%dH   ____     " % (y, x))
    print("\033[%d;%dH  /'___\    " % (y + 1, x))
    print("\033[%d;%dH /\ \__/    " % (y + 2, x))
    print("\033[%d;%dH \ \  _``\  " % (y + 3, x))
    print("\033[%d;%dH  \ \ \L\ \ " % (y + 4, x))
    print("\033[%d;%dH   \ \____/ " % (y + 5, x))
    print("\033[%d;%dH    \/___/  " % (y + 6, x))

def print7(x, y):
    print("\033[%d;%dH  ________  " % (y, x))
    print("\033[%d;%dH /\_____  \ " % (y + 1, x))
    print("\033[%d;%dH \/___//'/' " % (y + 2, x))
    print("\033[%d;%dH     /' /'  " % (y + 3, x))
    print("\033[%d;%dH   /' /'    " % (y + 4, x))
    print("\033[%d;%dH  /\_/      " % (y + 5, x))
    print("\033[%d;%dH  \//       " % (y + 6, x))

def print8(x, y):
    print("\033[%d;%dH    __      " % (y, x))
    print("\033[%d;%dH  /'_ `\    " % (y + 1, x))
    print("\033[%d;%dH /\ \L\ \   " % (y + 2, x))
    print("\033[%d;%dH \/_> _ <_  " % (y + 3, x))
    print("\033[%d;%dH   /\ \L\ \ " % (y + 4, x))
    print("\033[%d;%dH   \ \____/ " % (y + 5, x))
    print("\033[%d;%dH    \/___/  " % (y + 6, x))

def print9(x, y):
    print("\033[%d;%dH    __      " % (y, x))
    print("\033[%d;%dH  /'_ `\    " % (y + 1, x))
    print("\033[%d;%dH /\ \L\ \   " % (y + 2, x))
    print("\033[%d;%dH \ \___, \  " % (y + 3, x))
    print("\033[%d;%dH  \/__,/\ \ " % (y + 4, x))
    print("\033[%d;%dH       \ \_\\" % (y + 5, x))
    print("\033[%d;%dH        \/_/" % (y + 6, x))

def printColon(x, y):
    print("\033[%d;%dH        " % (y, x))
    print("\033[%d;%dH  __    " % (y + 1, x))
    print("\033[%d;%dH /\_\   " % (y + 2, x))
    print("\033[%d;%dH \/_/_  " % (y + 3, x))
    print("\033[%d;%dH   /\_\ " % (y + 4, x))
    print("\033[%d;%dH   \/_/ " % (y + 5, x))
    print("\033[%d;%dH        " % (y + 6, x))