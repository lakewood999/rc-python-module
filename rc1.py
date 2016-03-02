#PR Toolkit(WorkEnvironment Part 1) Module
#This is a module meant to add new commands to python, as an available resource
#This is not meant to handle tasks as part of a seperate script

#The help function for this module is "prhelp()"

#Imports
import hashlib
import os
import math
def shell():
    #Below is a WIP, put everything under the internal shell to reutrn after command execution
    import string
    import random
    global user
    global ac
    global rel
        
    def internal():
        action = input(user+"@testshell:~$")
        if action == "ctoss":
            global total
            global hamt
            global hprc
            total = 0
            hamt = 0
            hprc = 0
            tamt = 0
            tprc = 0 
            while total < 1000001:
                ran = random.choice("h" "t")
                total += 1
                if ran == "h":
                    hamt += 1
                    hprc = hamt/total
                elif ran == "t":
                    tamt += 1
                    tprc = tamt/total
                if total == 10:
                    print("Total: " + str(total))
                    print("Amt of Tails: " + str(tamt))
                    print("Amt of Heads: " + str(hamt))
                    print("Perc of Tails: " + str("%.2f"%((tprc)*100)) + "%")
                    print("Perc of Heads: " + str("%.2f"%((hprc)*100)) + "%")
                if total == 100:
                    print("Total: " + str(total))
                    print("Amt of Tails :" + str(tamt))
                    print("Amt of Heads :" + str(hamt))
                    print("Perc of Tails :" + str("%.2f"%((tprc)*100)) + "%")
                    print("Perc of Heads :" + str("%.2f"%((hprc)*100)) + "%")
                if total == 1000:
                    print("Total: " + str(total))
                    print("Amt of Tails :" + str(tamt))
                    print("Amt of Heads :" + str(hamt))
                    print("Perc of Tails :" + str("%.2f"%((tprc)*100)) + "%")
                    print("Perc of Heads :" + str("%.2f"%((hprc)*100)) + "%")
                if total == 10000:
                    print("Total: " + str(total))
                    print("Amt of Tails :" + str(tamt))
                    print("Amt ofHeads :" + str(hamt))
                    print("Perc of Tails :" + str("%.2f"%((tprc)*100)) + "%")
                    print("Perc of Heads :" + str("%.2f"%((hprc)*100)) + "%")
                if total == 100000:
                    print("Total: " + str(total))
                    print("Amt of Tails :" + str(tamt))
                    print("Amt ofHeads :" + str(hamt))
                    print("Perc of Tails :" + str("%.2f"%((tprc)*100)) + "%")
                    print("Perc of Heads :" + str("%.2f"%((hprc)*100)) + "%")
                if total == 1000000:
                    print("Total: " + str(total))
                    print("Amt of Tails :" + str(tamt))
                    print("Amt ofHeads :" + str(hamt))
                    print("Perc of Tails :" + str("%.2f"%((tprc)*100)) + "%")
                    print("Perc of Heads :" + str("%.2f"%((hprc)*100)) + "%")
                    
        #WIP: numguess
        if action == "numguess":#WIP
            ran = random.choice(string.digits)+random.choice(string.digits)
            ran = int(ran)
            moves = 0
            def main():
                guess = input("Guess a number from 1-99:")
                moves = move+1
                guess = int(guess)
                if guess > ran:
                    print("Smaller")
                    main()
                elif guess < ran:
                    print("Bigger")
                    main()
                elif guess == ran:
                    print("You got it!!")
                    internal()
            main()
        if action == "help":
            print("Type \"exit\" to exit...")
            print("Your available commands are:")
            print("\"schoolpsswd\", \"lc\", \"1l\", \"mp\" -- Makes a list of values--Parameters vary on command")
            internal()
    
        if action == "exit":
            return
        if action == "schoolpasswd":
            list = []
            item = random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)
            global list
            while len(list) != 308915776:
                item = random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)
                if item in list:
                    item = random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)
                elif len(list) != 308915776:
                    list.append(item)
                #print(sorted(list))
                    if len(list) == 308915776:
                        print("Done!!")
                        print("------------------------------------------------")
                    #print(sorted(list))
                        print (', '.join(sorted(list)))
                        internal()
        if action == "lc":
            list = []
            item = random.choice(string.ascii_lowercase)
            global list
            while len(list) != 26:
                item = random.choice(string.ascii_lowercase)
                if item in list:
                    item = random.choice(string.ascii_lowercase)
                elif len(list) != 26:
                    list.append(item)
                #print(sorted(list))
                    if len(list) == 26:
                        print("Done!!")
                        print("------------------------------------------------")
                    #print(sorted(list))
                        print (', '.join(sorted(list)))
                        internal()
        if action == "1l":
            list = []
            item = random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)
            counter = 0
            global list
            global counter
            while len(list) != 676:
                item = random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)
                counter = counter + 1
                if item in list:
                    item = random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)
                    counter = counter + 1
                elif len(list) != 676:
                    list.append(item)
                #print(sorted(list))
                    if len(list) == 676:
                        print("Done!!")
                        print("------------------------------------------------")
                    #print(sorted(list))
                        print (', '.join(sorted(list)))
                        counter = str(counter)
                        print("Random Counts:"+ counter)
                        internal()
        if action == "mp":#finished in ~15 minutes
            list = []
            item = random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.digits)
            counter = 0
            global counter
            global list
            while len(list) != 67600:
                item = random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.digits)
                counter = counter + 1
                if item in list:
                    item = random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.digits)
                    counter = counter + 1
                elif len(list) != 67600:
                    list.append(item)
                #print(sorted(list))
                    if len(list) == 67600:
                        print("Done!!")
                        print("------------------------------------------------")
                    #print(sorted(list))
                        print (', '.join(sorted(list)))
                        print(counter)
                        internal()
    '''
    rel = "test"
    if afsfasfaf == rel:
        internal()
    else:
        return
    '''
'''
        def testfor():
            def ds1():
                item = random.choice(string.ascii_lowercase)
                testfor()
            if item in list:
                ds1()
            elif len(list) < 27:
                list.append(item)
                ds1()
            else:
                print("Done!!")
                print(sort(list))
                return
        testfor()
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
    
    
    
    
    
    
