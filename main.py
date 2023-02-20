import json
import random

HANGED = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
     /   |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
     / \  |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
     / \_  |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
     /_ \_|
    =========''']

datos_json = """{
  "data": [
    "abcsd",
    "abcsd2",
    "abc34sd",
    "abc2323sd",
    "abc1sDd",
    "abcsdDDs2",
    "abcsDSd",
    "AabAcAsd"
  ]
}"""
 
datos_diccionario = json.loads(datos_json)
datos_array = datos_diccionario["data"]
 

datos_array_level_1 = []
for i in datos_array:
    if len(i) >= 1 and len(i)<= 5:
        datos_array_level_1.append(i)

datos_array_level_2 = []
for i in datos_array:
    if len(i) >= 6 and len(i)<= 8:
        datos_array_level_2.append(i)

datos_array_level_3 = []
for i in datos_array:
    if len(i) >= 9 and len(i)<= 100:
        datos_array_level_3.append(i)
'''
print(datos_array_level_1)
print(datos_array_level_2)
print(datos_array_level_3)
print(datos_array)
'''

def SearchWordRandom(a):
    w = random.randint(0,len(a)-1)
    ##return print(a[wordr])
    return a[w]

def ChooseLetter(letterb):
    while True:
        l = input("guess a letter\n").lower()
        if len(l) != 1:
            print("give me only one letter")
        elif l in letterb:
            print("you already gave me that letter")
        elif l not in 'abcdefghijklmnñopqrstuvwxyz0123456789':
            print("pls give a letter or number")
        else:
            return l


def UserGenerate():
    name_user = str(input("Hello! pls give us your name\n")).capitalize()
    return name_user
 

def WelcomeToUser(a):
    print(f'Hello, {a}!, welcome to the game')
 
def PrintHanged(i):
        print(HANGED[i])
        
name_user_a = UserGenerate()
WelcomeToUser(name_user_a)
  
WrongLetter = ''  
CorrectLetter = ''
def start_program():
    print('[1] Low Level\n[2] Medium Level\n[3] High Level\n[S] Exit')
    n = input('Select the level you want to play\n').lower()
    if n == '1': 
        WrongLetter = ''  
        CorrectLetter = ''
        SecretWord = SearchWordRandom(datos_array_level_1)
        k = 0
        r = len(SecretWord)+3
        while k <= r: 
                PrintHanged(k)
                print(f'vas {k} turnos')
                letter1 = ChooseLetter(WrongLetter + CorrectLetter)  
                if letter1 in SecretWord: 
                        CorrectLetter = CorrectLetter + letter1
                        letter_search = True
                        ##k = k + 1
                        for i in range(len(SecretWord)):
                                if SecretWord[i] not in CorrectLetter:
                                        letter_search = False
                                        break
                        if letter_search:
                                print(f"Good job! you guess the word \'{SecretWord}\'")
                                k = k + r
                        print(f'you are guessing untin now these words: {CorrectLetter}')
                else:
                        WrongLetter = WrongLetter + letter1
                        if k == r:
                                print(f"you have lost, the secret word was: {SecretWord} and your word was {CorrectLetter}") 
                k = k + 1

    elif n == '2': 
        WrongLetter = ''  
        CorrectLetter = ''
        SecretWord = SearchWordRandom(datos_array_level_2)
        k = 0
        r = len(SecretWord)+2
        while k <= r: 
                PrintHanged(k)
                print(f'vas {k} turnos')
                letter1 = ChooseLetter(WrongLetter + CorrectLetter)  
                if letter1 in SecretWord: 
                        CorrectLetter = CorrectLetter + letter1
                        letter_search = True
                        ##k = k + 1
                        for i in range(len(SecretWord)):
                                if SecretWord[i] not in CorrectLetter:
                                        letter_search = False
                                        break
                        if letter_search:
                                print(f"Good job! you guess the word \'{SecretWord}\'")
                                k = k + r
                        print(f'you are guessing untin now these words: {CorrectLetter}')
                else:
                        WrongLetter = WrongLetter + letter1
                        if k == r:
                                print(f"you have lost, the secret word was: {SecretWord} and your word was {CorrectLetter}") 
                k = k + 1
                
    elif n == '3': 
        WrongLetter = ''  
        CorrectLetter = ''
        SecretWord = SearchWordRandom(datos_array_level_3)
        k = 0
        r = len(SecretWord)
        while k <= r: 
                PrintHanged(k)
                print(f'vas {k} turnos')
                letter1 = ChooseLetter(WrongLetter + CorrectLetter)  
                if letter1 in SecretWord: 
                        CorrectLetter = CorrectLetter + letter1
                        letter_search = True
                        ##k = k + 1
                        for i in range(len(SecretWord)):
                                if SecretWord[i] not in CorrectLetter:
                                        letter_search = False
                                        break
                        if letter_search:
                                print(f"Good job! you guess the word \'{SecretWord}\'")
                                k = k + r
                        print(f'you are guessing untin now these words: {CorrectLetter}')
                else:
                        WrongLetter = WrongLetter + letter1
                        if k == r:
                                print(f"you have lost, the secret word was: {SecretWord} and your word was {CorrectLetter}") 
                k = k + 1
    elif n == 's':
        print("Thank you ;)")
        exit
    else:
        print('I don\'t understand the command, try again: ')
        start_program()
 
start_program()
 