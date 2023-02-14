import json
import random

AHORCADO = ['''
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
        l = input("guess a letter").lower()
        if len(l) != 1:
            print("give me only one letter")
        elif l in letterb:
            print("you already gave me that letter")
        elif l not in 'abcdefghijklmnñopqrstuvwxyz':
            print("pls give a letter")
        else:
            return l


def UserGenerate():
    name_user = str(input("Hello! pls give us your name\n")).capitalize()
    return name_user
 

def WelcomeToUser(a):
    print(f'Hello, {a}!, welcome to the game')
 

name_user_a = UserGenerate()
WelcomeToUser(name_user_a)
  
WrongLetter = ''  
CorrectLetter = ''
def start_program():
    print('[1] Low Level\n[2] Medium Level\n[3] High Level\n[S] Exit')
    n = input('Select the level you want to play\n').lower()
    if n == '1': 
        SecretWord = SearchWordRandom(datos_array_level_1)
        letter1 = ChooseLetter(WrongLetter + CorrectLetter)  
        if letter1 in SecretWord: 
            CorrectLetter = CorrectLetter + letter1
            letter_search = True
            for i in range(len(SecretWord)):
                if SecretWord[i] not in CorrectLetter:
                    letter_search = False
                    break
            if letter_search:
                print(f"Good you guess the word {SecretWord}")
        else:
            WrongLetter = WrongLetter + letter1
            if len(WrongLetter) == 6:
                print("Ha perdido") 
    elif n == '2': 
        SecretWord = SearchWordRandom(datos_array_level_2)
        print("Medium Level! We think on a word, pls guess that")
        print("_ "*6)
    elif n == '3': 
        SecretWord = SearchWordRandom(datos_array_level_3)
        print("High Level! We think on a word, pls guess that")
        print("_ "*10)
    elif n == 's':
        print("Thank you ;)")
        exit
    else:
        print('I don\'t understand the command, try again: ')
        start_program()
 
start_program()
 