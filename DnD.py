from ran_name import nameGen
from random import randint
from openpyxl import load_workbook
import random, datetime
import os
from colorama import Fore, Back, Style, init

init(autoreset=True)
book = load_workbook('C:/Users/hp/dnd/DnD.xlsx')
sheet1 = book['nameGen']

class Mob:
    def __init__(self, name, hp, ac, turn):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.turn = turn

def getTurn(x):
    return x.turn

money = []
experience = []
play = []
adventure = ''

def SelectAdventure():
    global adventure

    answer = input('Write the name of your adventure\n')
    adventure = answer
    file0 = open(f'C:/users/hp/dnd/{adventure}_player.txt', 'a')
    file0.close()
    file1 = open(f'C:/users/hp/dnd/{adventure}_register.txt', 'a')
    file1.close()

def AcquirePlayers():

    menu0 = False
    menu1 = False
    menu2 = False 

    print('Want to add Characters?\n1. Add\n2. Show saved Characters\n3. Continue')
    x = input('...')
    if x == '1':
        menu1, menu0 = True, True

    if x == '2':
        file1 = open(f'C:/users/hp/dnd/{adventure}_player.txt', 'r')
        p = []
        for line in file1.readlines():
            p.append(line)
            n, h, a = line.split(',')
            print(f'Name: {n}\nHP: {h}\nAC: {a}')

        x = input('Type the name to add to the group. Type done to quit.\n...')

        menu2, menu0 = True, True

    if x == '3':
        pass

    while menu0:
        while menu1:
            p = []
            y = input('Name: ')
            p.append(y)
            y = input('HP: ')
            p.append(int(y))
            y = input('AC: ')
            p.append(int(y))

            play.append(Mob(p[0], p[1], p[2], 0))

            y = input('Save the Character? y/n\n...')
            if y == 'y':
                file1 = open(f'C:/Users/hp/DnD/{adventure}_player.txt', 'a')
                file1.write(f'{p[0]},{p[1]},{p[2]}' + '\n')
                file1.close()

            y = input('Another? y/n\n...')

            if y == 'y':
                pass
            if y == 'n':
                menu1, menu0 = False, False
                break

        while menu2:
            for char in p:
                stat = char.split(',')
                if x in stat[0]:
                    play.append(Mob(stat[0], stat[1], stat[2], 0))

            if x == 'done':
                x = input('Do you want to Register another Character? y/n\n...')
                if x == 'y':
                    file1.close()
                    menu2 = False
                    menu1 = True
                    break
                if x == 'n':
                    file1.close()
                    menu2, menu0 = False, False
                    break

            x = input('...')

def Gold(s, file):
    if s[0] == 'g' or s[0] == 'G':
        g = 0
        for x in range(len(s)):
            if s[x] == 'g':
                g += random.randint(1, 6)
            if s[x] == 'G':
                g += random.randint(1, 10)
            if s[x] == '+':
                g += int(s[x:])
                break
        
        money.append(g)
        answer = now.strftime('%H:%M ') + ' ' + str(g) + 'g'
        file.write(answer + '\n')
        print(Fore.YELLOW + Style.BRIGHT + answer)
 
def Experience(s, file):
    if s[0] == 'E' or s[0] == 'e':
        answer = now.strftime('%H:%M ') + ' ' + s[1:] + 'xp'
        experience.append(int(s[1:]))
        file.write(answer + '\n')
        print(Fore.CYAN + answer)

def Note(s, file):
    if s[0] == '#':
        file.write(s + '\n')
        print(Style.DIM + '(Saved)')

def showMobs(s):
    if s == 'mobs':
        for x in play:
            print(x.name)

def help(s):
    if s == '!help':
        r = open('C:/Users/hp/dnd/help.txt', 'r')
        for line in r.readlines():
            print(line)

def addMobs(s):
    if s == '!add':
        print('Adding Mob...')
        p = []
        y = input('Name: ')
        p.append(y)
        y = input('HP: ')
        p.append(int(y))
        y = input('AC: ')
        p.append(int(y))

        x = input('Add?\n')
        if x == 'y':
            play.append(Mob(p[0] + ' (E)', p[1], p[2], 0))
        if x == 'n':
            p.clear()

def setInitiative(s):
    if s == 'combat':
        print('Set Initiatives:')
        for x in play:
            r = input(x.name + ': ')
            x.turn = int(r)

        x = input('Confirm? y/n\n...')
        if x == 'y':
            play.sort(reverse=True, key=getTurn)
            for x in play:
                print(x.name, end=', ')
            print('\n')
        if x == 'n':
            for x in play:
                x.turn = 0


def Quit(x, file):
    global run, money, experience

    if x == 'quit' or x == 'end' or x == 'out' or x == 'done':
  
        file.write('Gained for now:' + '\n')
        m_gen = 'Total Gold Gained: ' + Fore.YELLOW + Style.BRIGHT + str(sum(money)) + 'g'
        file.write('Total Gold Gained: ' + str(sum(money)) + 'g' + '\n')
        xp_gen = 'Total Experience Gained: ' + Fore.CYAN + str(sum(experience)) + 'xp'
        file.write('Total Experience Gained: ' + str(sum(experience)) + 'xp' + '\n')
        print(m_gen + Style.RESET_ALL + '\n' + xp_gen)
  
        q = input('Do you want to quit? y/n\n...')
  
        if q == 'y':
            run = False
            print('Bye')
        if q == 'n':
            pass    

#### Started program here

SelectAdventure()

file = open(f"C:/Users/hp/DnD/{adventure}_register.txt", "a")
now = datetime.datetime.now()
file.write(now.strftime('%Y %m %d :: %H:%M') + '\n')
print(now.strftime('%Y %m %d :: %H:%M'))
file.close()

AcquirePlayers()

os.system('cls')

print(Fore.BLACK + Back.WHITE + Style.DIM + 'Program Started')
print('Characters: ', end='')
for x in play:
    print(x.name, end=' ')
print('\n')

run = True    
while run:

    file = open(f"C:/Users/hp/DnD/{adventure}_register.txt", "a")
    
    x = input('...')

    try:
        Gold(x, file)
        Note(x, file)        
        Experience(x, file)
        Quit(x, file)
        showMobs(x)
        addMobs(x)
        nameGen(x, sheet1)
        setInitiative(x)
        help(x)
    except IndexError:
        pass

    file.close()
