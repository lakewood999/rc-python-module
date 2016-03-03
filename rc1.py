#PR Toolkit(WorkEnvironment Part 1) Module
#This is a module meant to add new commands to python, as an available resource
#This is not meant to handle tasks as part of a seperate script

#The help function for this module is "prhelp()"

#Imports
import hashlib
import os
import math
'''
#Science tool--WIP
def sat():
    nums = [1,2,3]
    out = ["This is for outliers"]
    average = ((sum(nums))/(len(nums)))
    global nums
    global out
    global average
    print("Type help for help...")
    action = input()
    salt = action[:1]
    print(salt)
    if salt == "i":
        action = action.replace("i","")
        add = [action]
        nums += add
        average = (float((sum(nums)))/int((len(nums))))
        print(average)
'''
#Dec-Hex--stop supported
def dh():
    num = input("Number: ")
    if num == "stop":
        return
    else:
        out = hex(int(num))
        out = str(out)
        out = out[2:]
        print("Hexadecimal number: "+out)
        dh()

#Dec-Binary--stop supported
def db():
    num = input("Number: ")
    if num == "stop":
        return
    else:
        out = bin(int(num))
        out = str(out)
        out = out[2:]
        print("Binary number: "+out)
        db()

#Average tool--stop supported
def average():
    global total
    global numbers
    global display
    global tp
    def averagep():
        global total
        global numbers
        global display
        global tp
        total = total
        numbers = numbers
        tp = input("Add a number to the total: ")
        if str(tp) == "stop":
            return
        else:
            total = float(tp) + total
            numbers = 1 + numbers
            display = int(total)/int(numbers)
            print ("Here is your average: " + str(display))
            averagep()
    total= 0
    numbers = 0
    tp = input("Add a number to the total: ")
    if str(tp) == "stop":
        return
    else:
        total = float(tp) + total
        numbers = numbers + 1
        display = int(total)/int(numbers)
        print ("Here is your average: " + str(display))
        averagep()

#Compares 2 equations--stop supported
def comparenum():
    stop = "stop"
    x= eval(input("Equation 1: "))
    if str(x) == "stop":
        return
    y= eval(input("Equation 2: "))
    if str(y) == "stop":
        return
    elif x == y:
        print("Match!")
    else:
        print("No match!")
    comparenum()

#Comparing two items--stop supported
def comparew():
    p1 = input("Comparing item 1: ")
    if p1 == "stop":
        return
    p2 = input("Comparing item 2: ")
    if p2 == "stop":
        return
    elif p1 == p2:
        print("Match!")
    else:
        print("No match!")
    comparew()

#Non-hex digest of sha-256--stop supported
def sha256():
    word = input("Word/Phrase/Sentence: ").encode('utf-8')
    if word == ("stop").encode('utf-8'):
        return
    else:
        hashed = hashlib.sha256()
        hashed.update(word)
        hashed.digest()
        print (hashed.digest())
    sha256()
    
#Hex-digest of sha-256--stop supported
def sha256hex():
    word = input("Word/Phrase/Sentence: ").encode('utf-8')
    if word== ("stop").encode('utf-8'):
        return
    else:
        hashed = hashlib.sha256()
        hashed.update(word)
        hashed.hexdigest()
        print (hashed.hexdigest())
        sha256hex()

#Square root--stop supported
def sqrt():
    x= input("#: ")
    if x=="stop":
        return
    else:
        print(float(x) ** (0.5))
        sqrt()

#Squares Numbers--stop supported
def sqr():
    x= input("#: ")
    if x=="stop":
        return
    else:
        print(float(x)*float(x))
        sqr()

#Name of mod
def name():
    print("PR Toolkit(WorkEnvironment Part 1) Module...")

#Version
def version():
    print("Version 3.1---13 commands---1 WIP")

#Dev info
def dev():
    print("Developed by ProgramRandom")
    print("Open-sourced")
    print("ProgramRandom and Random Corporations are registered names...")
    print("Visit Random Corporations at www.randomcorporations.tk")
    
#Help command
def prhelp():
    print("Here are youyr available commands:")
    print("Note: For some programs, entering stop will allow you tooo exit the program")
    print("Scripts supporting this are: average(), comparew(), comparenum()")
    print("sha256(), sha256hex()")
    print("")
    print("1=>help() -- Dsiplays a list of commands")
    print("2=>name() -- Tells the program name")
    print("3=>version() -- Tells the version info on the module")
    print("4=>sqr(x) -- Returns the square of input x")
    print("5=>sqrt(x) -- Returns the square root of input x")
    print("6=>sha256hex() -- Output a hashed(normal) value of a given phrase or sentence")
    print("7=>sha256() -- Output a hashed(abnormal) value of a given phrase or sentence")
    print("8=>comparew() -- Compares two given word sets and determines match/or not")
    print("9=>comparenum() -- Compares two given equations and determines match/or not")
    print("10=>dev() -- Developer information")
    print("11=>average() -- A tool for averaging items")
    print("12=>db() -- A conversion tool between decimal numbers to binary")
    print("12=>dh() -- A conversion tool between decimal numbers to hexadecimal")
    print("13=>sat() -- WIP, science data tool")
    print("14=>test() -- \"Shell\" tool with implmented tools---NOTE: This environment is full of tools, probably un-needed by the average user. You can type \'help\' for the available commands in that tool")
    
    
    
    
    
    
