from random import lognormvariate
import discord, os, sys, art, requests 
from pyfade import Fade
from termcolor import colored, cprint
from colorama import Fore, init
from time import sleep
from subprocess import PIPE
import fade

def demarage():
    typo = '''                                            
                                      @,           ▐    ▄▄·       ▄▄▄▄· ▄▄▄   ▄▄▄·   
                                    @@@@           ▐   ▐█ ▌▪▪     ▐█ ▀█▪▀▄ █·▐█ ▀█   
                         @@@@,     @@@@@           ▐   ██ ▄▄ ▄█▀▄ ▐█▀▀█▄▐▀▀▄ ▄█▀▀█   
                      @@@@@@@@@@   @@@             ▐   ▐███▌▐█▌.▐▌██▄▪▐█▐█•█▌▐█ ▪▐▌  
                     @@@@    *@@@@  @@@@@          ▐   ·▀▀▀  ▀█▄▀▪·▀▀▀▀ .▀  ▀ ▀  ▀   
                     @@@@      @@@@    @@@@@@      ▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                      @@@@@      @@@@@    %@@@     ▐
              @@@@@@@@  @@@@@@@@   @@@@@@@@@@      ▐    ▄▄·       • ▌ ▄ ·.  ▄▄▄· ▄▄▄· ▄▄▄   ▄▄▄· ▄▄▄▄▄      ▄▄▄
             @@@@@@@@@@@    @@@@@@@@@              ▐   ▐█ ▌▪▪     ·██ ▐███▪▐█ ▄█▐█ ▀█ ▀▄ █·▐█ ▀█ •██  ▪     ▀▄ █·   
             @@@@   @@@@@@        @@@@@@           ▐   ██ ▄▄ ▄█▀▄ ▐█ ▌▐▌▐█· ██▀·▄█▀▀█ ▐▀▀▄ ▄█▀▀█  ▐█.▪ ▄█▀▄ ▐▀▀▄    
            @ @@@@    @@@@@,         @@@@@         ▐   ▐███▌▐█▌.▐▌██ ██▌▐█▌▐█▪·•▐█ ▪▐▌▐█•█▌▐█ ▪▐▌ ▐█▌·▐█▌.▐▌▐█•█▌ 
               @@@@@    @@@@@@       #@@@@         ▐   ·▀▀▀  ▀█▄▀▪▀▀  █▪▀▀▀.▀    ▀  ▀ .▀  ▀ ▀  ▀  ▀▀▀  ▀█▄▀▪.▀  ▀   
                 @@@@@@   @@@@@@@@@@@@@@@          ▐  
                    #@@@@    @@@@@@@@@@            ▐                   1: Comparer 2 Fichiers                         
            @@@@       @@@                         ▐                   2: Comparer 2 Textes   
                @@@@  &@@@                         ▐                   3: Chercher un Webhooks dans un fichier
                    @@@#                           ▐                   4: Skid tool
    '''

    os.system('mode con lines=30 cols=120')
    

    choix = input(colored("Choisissez votre mode:", 'cyan' ))


    if choix == "1": 
        clear()
        nom1 = input(colored("Nom du fichier 1:  ", 'cyan'))
        nom2 = input(colored("Nom du fichier 2:  ", 'cyan'))
        comparfichier(nom1, nom2)

    if choix == "2": 
        clear()
        compartexte()

    if choix == "3":
        clear()
        Webfinder()
    
    if choix == "4":
        clear()
        skidtool()
    
    tapbacktoreturntomenutotamere = input(colored("Appuyez sur entré pour revenir au menu.", 'cyan')) 

    if len(tapbacktoreturntomenutotamere) == 0:
        demarage()

def clear():
    os.system('cls')
    os.system('mode con lines=30 cols=120')
    print(Fade.Vertical(Fade.green_to_blue, typoclear))

def comparfichier(fichier1, fichier2):
        f1 = 0
        f2 = 0
        with open(fichier1) as f:
            contents = f.read()
            f1 = len(contents)

        with open(fichier2) as f:
            contents = f.read()
            f2 = len(contents)

        if f1 == f2:
            print(colored("▪Les textes sont les même.▪", 'green'))
        else :
            print(colored("▪Les textes ne sont pas les même▪", 'red'))
            print(colored("Votre texte 1 contient ", 'cyan'), f1, "caractères")
            print(colored("Votre texte 2 contient ", 'cyan'), f2, "caractères")
            caractere = [f1, f2]
            result = 0
            if f1 > f2:
                result = caractere[0]-caractere[1]  
            else:
                result = -(caractere[0]-caractere[1])  
                print("Le nombres de caractères de différences est de", result) 
 
def compartexte():
        texte1 = input(str(colored("Entrez votre texte 1: ",'white')))
        longueur1 = len(texte1)

        texte2 = input(str(colored("Entrez votre texte 2: ",'white')))
        longueur2 = len(texte2)

        if texte1 == texte2 :
            print(colored("▪Les textes sont les même.▪", 'green'))
        else :
            print(colored("▪Les textes ne sont pas les même▪", 'red'))
            print(colored("Votre texte 1 contient ", 'cyan'), longueur1, "caractères")
            print(colored("Votre texte 2 contient ", 'cyan'), longueur2, "caractères")
            caractere = [longueur1, longueur2]
            result = 0
            if longueur1 > longueur2 :
                result = caractere[0]-caractere[1]  
            else:
                result = -(caractere[0]-caractere[1])  
            print("Le nombres de caractères de différences est de", result)

def Webfinder():
    filename = input(colored("Nom du fichier :  ", 'cyan'))
    data_input = open(f'{filename}.py', 'r+', encoding="utf8").readlines()
    for line in data_input:
        if '/api/webhooks/' in line:
            hook = (line.split('/api/webhooks/')[1])[:87].split(')')[0]
            webhook = f'https://discord.com/api/webhooks/{hook}'
            r = requests.get(webhook)
            if r.status_code == 200:
                print(webhook)
                print(colored("Le Webhook est valide.", 'green'))
                sup = input(colored("Voulez vous suprimer le WebHook (y/n): "))
                if sup == 'y':
                    requests.delete(webhook)
                if sup == "n":
                    demarage() 
            else:
                print (webhook)
                print(colored("Le WebHook n'est pas valide.", 'red'))
    if not "/api/webhooks/" in data_input:
        print(colored("Il n'y as pas de webhook", 'red'))

def skidtool():
    print(colored("Attention Specifiez l'éxtention du fichier.", 'cyan' ))
    filename = input(colored("Nom du fichier :  " + ' ', 'cyan'))
    pseudo = input(colored("Mots a modifier: ", 'red'))
    name = input(colored("Mot qui modifira: ", 'green'))

    with open(filename, 'r+') as f:

        file_source = f.read()

        replace_string = file_source.replace(pseudo, name)

        f.write(replace_string)
    
    print(colored("Votre fichier a était modifié.", 'green'))


typoclear = '''                                              
                                   @,           ▐
                                 @@@@           ▐
                      @@@@,     @@@@@           ▐
                   @@@@@@@@@@   @@@             ▐
                  @@@@    *@@@@  @@@@@          ▐
                  @@@@      @@@@    @@@@@@      ▐
                   @@@@@      @@@@@    %@@@     ▐
           @@@@@@@@  @@@@@@@@   @@@@@@@@@@      ▐
          @@@@@@@@@@@    @@@@@@@@@              ▐
          @@@@   @@@@@@        @@@@@@           ▐
          @@@@@    @@@@@,         @@@@@         ▐
            @@@@@    @@@@@@       #@@@@         ▐
              @@@@@@   @@@@@@@@@@@@@@@          ▐
                 #@@@@    @@@@@@@@@@            ▐
         @@@@       @@@                         ▐
             @@@@  &@@@                         ▐
                 @@@#                           ▐
'''

demarage()