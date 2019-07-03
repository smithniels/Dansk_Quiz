##    ø   æ    å
##       Dansk
'''
CURRENTELY NOT WORKING

TODO: def add_word(key,value):

'''

import string
import random
# import sys
# import io

#sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

allowed = string.ascii_letters ,'æøå' #this will be printed later to see if those 3 char's are working

dict = {'Adgangskode':'Password',
'Aldrig':'Never',
'Blev':'Became',
'Ansøg':'Apply',
'Begivenhed':'Event',
'Del':'Share',
'Delte':'Shared',
'Fjerne':'Remove',
'Forsæt':'Continue',
'Forskelle':'Difference/Distinction',
'Galt':'Wrong',
'Gentag':'Repeat',
'Heriblandt':'Including',
'Hvert':'Each',
'Hvor som helst':'Anywhere',
'I for':'Last year',      # this only returns I. Hvorfor det?
'Indstillinger':'Settings',
'Mest':'Most',
'Mil':'Mile',
'Mindst':'Worst/Least',
'Nyttig':'Helpful',
'Oplysinger':'Information',
'Parat':'Ready',
'Prøve':'Try',
'Rusted':'Prepare',
'Ryd':'Remove',
'Seneste':'Latest',
'Sikre':'Cloudy',
'Skyet':'Slet',
'Slet':'Delete',
'Slå':'Beat/Hit',
'Sleder':'Sites/Locations',
'Stilling':'Position',
'Svaer':'Hard',
'Søg(niner)':'Search(es)',
'Tilgaenglig':'Accessible',
'Tillad':'Allow',
'Udnytte':'Exploit',
'Ugentlig':'Weekly',
'Understøt(ter)':'Support(s)',
'Varet':'Warning',
'Vaelg':'Choose',
'Vaere':'Be'}

# class questions: Unnecessary thingie
#     def __init__(self,prompt,answer):
#         self.prompt = prompt
#         self.answer = answer

print("These are the characters. I bet they don't all load... \n",allowed)
# print(dict)


# def quiz1():
#     score = 0
#     for i in question_prompt:
#         if input() == answer:
#             score ,= 1
#         else:
#             print("hvad")
def start():
    print("welcome to the Danish quiz")
    print("Intast 'y' for at begynde nu")
    if input() == 'y':
        print("Led os begynde!")
        quiz()
    else:
        print("okay Dokay, Partner")


def quiz():
    #score = 0 # need to figure out what to do with this bad boy. It's currently reseting to zero every time it's return
              # probably need to ...
    # print(random.choice(dict[2]))
    key,value = random.choice(list(dict.items()))
    print("Hvad oversætter ", key ," til?")
    question = input()
    print(question)
    if question == value:
        score += 1
        print("Ja!")
    else:
        print("Nej...")
        print("Dit ord var: ", value)
    print("Din score er ", score)
    print(input("Egen?"))
    if input() == 'y':
        quiz()
    else: #need  to figure out what to do with this bad boy. It's currently reseting to zero every time it's return
              # probably need to ...
        print("Farvel!")
    question_prompt = [print("Hvad oversætter ", key ," til?")]



if __name__ == '__main__':
    score = 0
    start()
