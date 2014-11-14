##Alec Davidson

import random
import re
import flask

Race = []
Class = []
Spec = []

Hunter = ["Beast_Mastery", "Marksmanship", "Survival"]
Monk = ["Brewmaster", "Mistweaver", "Windwalker"]
Mage = ["Arcane", "Fire", "Frost"]
Rogue = ["Assassination", "Combat", "Subtlety"]
Warrior = ["Arms", "Fury", "Protection"]
Hunter = ["Beast_Mastery", "Marksmanship", "Survival"]
Priest = ["Discipline", "Holy", "Shadow"]
Shaman = ["Elemental", "Enhancement", "Restoration"]
Death_Knight = ["Blood", "Frost", "Unholy"]
Warlock = ["Affliction", "Demonology", "Destruction"]
Druid = ["Balance", "Feral", "Gaurdian", "Restoration"]
Paladin = ["Holy", "Protection", "Retribution"]

hList = ["Horde", "horde", "H", "h"]
aList = ["Alliance", "alliance", "A", "a"]

def getRandomLine(rsv):                 # GetRandomLine code created by David. Those comments were his.
    file_h = open(rsv)                  #a file handle for the .txt in question
    limit = file_h.readline()           #the number of lines to search per the .txt
    limit = limit.replace('\n', '' )    #trim the return character
    limit = int(limit)                  #the number literal converted to int
    line = random.randint(0, limit - 1) #which line to search
    
    for x in range(line):
        file_h.readline()               #parse through that shit until search reached
    phrase = file_h.readline()          #if you gotta big d*** lemme search it. 
    phrase = phrase.replace('\n', '')   #get rid of trailing returns cause those are gross
    
    return(phrase)


def is_number(s):                       # This function will be used to make sure that a number is entered for the party size, any other option defaults to 1
    try:
        int(s)
        return True
    except ValueError:
        return False


def classCheck():
    global Race, Class
    if Race == "Pandaren":
        while(Class not in ["Monk", "Mage", "Rogue", "Warrior", "Hunter", "Priest", "Shaman"]):
            getClass()
    elif Race == "Worgen":
        while(Class not in ["Death_Knight", "Hunter", "Priest", "Warlock", "Druid", "Mage", "Rogue", "Warrior"]):
            getClass()
    elif Race == "Draenei":
        while(Class not in ["Monk", "Hunter", "Paladin", "Shaman", "Death_Knight", "Mage", "Priest", "Warrior"]):
            getClass()
    elif Race == "Dwarf":
        while(Class not in ["Monk", "Hunter", "Paladin", "Rogue", "Warlock", "Death_Knight", "Mage", "Priest", "Shaman", "Warrior"]):
            getClass()
    elif Race == "Gnome":
        while(Class not in ["Monk", "Mage", "Rogue", "Warrior", "Death_Knight", "Priest", "Warlock"]):
            getClass()
    elif Race == "Human":
        while(Class not in ["Monk", "Hunter", "Paladin", "Rogue", "Warrior", "Death_Knight", "Mage", "Priest", "Warlock"]):
            getClass()
    elif Race == "Knight_Elf":
        while(Class not in ["Monk", "Druid", "Mage", "Rogue", "Death_Knight", "Hunter", "Priest", "Warrior"]):
            getClass()
    elif Race == "Goblin":
        while(Class not in ["Death_Knight", "Hunter", "Mage", "Rogue", "Priest", "Shaman", "Warlock", "Warrior"]):
            getClass()
    elif Race == "Blood_Elf":
        while(Class not in ["Monk", "Hunter", "Paladin", "Rogue", "Warrior", "Death_Knight", "Mage", "Priest", "Warlock"]):
            getClass()
    elif Race == "Orc":
        while(Class not in ["Monk", "Hunter", "Rogue", "Warlock", "Death_Knight", "Mage", "Shaman", "Warrior"]):
            getClass()
    elif Race == "Tauren":
        while(Class not in ["Monk", "Druid", "Paladin", "Shaman", "Death_Knight", "Hunter", "Priest", "Warrior"]):
            getClass()
    elif Race == "Troll":
        while(Class not in ["Monk", "Druid", "Mage", "Rogue", "Warlock", "Death_Knight", "Hunter", "Priest", "Shaman", "Warrior"]):
            getClass()
    elif Race == "Undead":
        while(Class not in ["Monk", "Hunter", "Priest", "Warlock", "Death_Knight", "Mage", "Rogue", "Warrior"]):
            getClass()


def getRace(faction):                          # Randomly pick a race from the list
    global Race

    if faction in hList:
        Race = getRandomLine('horde.txt')
    elif faction in aList:
        Race = getRandomLine('alliance.txt')
    else:
        Race = getRandomLine('race.txt')


def getClass():                         # Randomly pick a class from the list
    global Class
    Class = getRandomLine('class.txt')
    classCheck()


def getSpec():                          # Randomly pick an spec from the list
    global Class, Spec
    if Class == "Monk":
        i = random.randint(0, 2)
        Spec = Monk[i]
    elif Class == "Druid":
        i = random.randint(0, 3)
        Spec = Druid[i]
    elif Class == "Warrior":
        i = random.randint(0, 2)
        Spec = Warrior[i]
    elif Class == "Hunter":
        i = random.randint(0, 2)
        Spec = Hunter[i]
    elif Class == "Priest":
        i = random.randint(0, 2)
        Spec = Priest[i]
    elif Class == "Paladin":
        i = random.randint(0, 2)
        Spec = Paladin[i]
    elif Class == "Rouge":
        i = random.randint(0, 2)
        Spec = Rouge[i]
    elif Class == "Death_Knight":
        i = random.randint(0, 2)
        Spec = Death_Knight[i]
    elif Class == "Mage":
        i = random.randint(0, 2)
        Spec = Mage[i]
    elif Class == "Shaman":
        i = random.randint(0, 2)
        Spec = Shaman[i]
    elif Class == "Warlock":
        i = random.randint(0, 2)
        Spec = Warlock[i]


def main(faction, count):
    global Race, Class, Spec

    #faction = raw_input("Horde or Alliance? ")
    #count = raw_input("How big is the party? ")

    if is_number(count):
        count = int(count)
    else:
        count = 1

    for i in range(count):
        getRace(faction)
        getClass()
        getSpec()


        flask.flash("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        flask.flash(Race)
        flask.flash(Spec)
        flask.flash(Class)
        flask.flash("")
        '''
        print ("\n")
        print(Race)
        print(Spec)
        print(Class)
        '''

