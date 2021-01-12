import InvinciblePython
from InvinciblePython import *

import math

print("[InvinciblePython]")
print("Type VerInfo() InvinciblePythonHelp() for more information. ")

def VerInfo():
    print("[InvinciblePython] Ver Alpha")
    print("Copyright © Hurrieam 2020")

def InvinciblePythonHelp():
    print("[A brief help to InvinciblePython]")
    print("PRINT(str)\tPrint a series of string on screen")
    print("PRINTLN(str)\tPrint a series of string on screen as a line")
    print("MAX(list)\tReturn the maxmimun number in a list")
    print("MIN(list)\tReturn the minimun number in a list")
    print("AVERAGE(list)\tReturn the average number in a list")
    print("DISTANCE(x1, y1, z1, x2, y2, z2)\tReturn the DISTANCE between to points")
    print("SORT_UP(list)\tSort the list from low to high")
    print("SORT_DOWN(list)\tSort the list from high to low")

def PRINT(str):
    try:
        print(str, end = "")
    except:
        return "[InvinciblePython] ERROR: An error has interrupted. "

def PRINTLN(str):
    try:
        print(str)
    except:
        return "[InvinciblePython] ERROR: An error has interrupted. "

def MAX(list):
    try:
        num = list[0]
        for i in range(0, len(list), 1):
            if list[i] > num:
                num = list [i]
                MAX_num = list[i]
        return MAX_num
    except:
        return "[InvinciblePython] ERROR: An error list has interrupted. "

def MIN(list):
    try:
        num = list[0]
        for i in range(0, len(list), 1):
            if list[i] < num:
                num = list [i]
                MAX_num = list[i]
        return MAX_num
    except:
        return "[InvinciblePython] ERROR: An error list has interrupted. "

def AVERAGE(list):
    try:
        return sum(list)/len(list)
    except:
        return "[InvinciblePython] ERROR: An error list has interrupted. "

def DISTANCE(x1, y1, z1, x2, y2, z2):
    try:
        return abs(math.sqrt((x2**2-x1**2)+(y2**2-y1**2)+(z2**2-z1**2)))
    except:
        return "[InvinciblePython] ERROR: An error has interrupted. "

def SORT_UP(list):
    try:
        for i in range(0, len(list) - 1, 1):
            for index in range(0, len(list) - 1, 1):
                if(list[index] > list[index + 1]):
                    temp = list[index + 1]
                    list[index + 1] = list[index]
                    list[index] = temp
        return list
    except:
        return "[InvinciblePython] ERROR: An error has interrupted. "

def SORT_DOWN(list):
    try:
        for i in range(0, len(list) - 1, 1):
            for index in range(0, len(list) - 1, 1):
                if(list[index] < list[index + 1]):
                    temp = list[index + 1]
                    list[index + 1] = list[index]
                    list[index] = temp
        return list
    except:
        return "[InvinciblePython] ERROR: An error has interrupted. "
