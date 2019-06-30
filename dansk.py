##    ø   æ    å
## Dansk
'''
Start page
"Intast "y" for at begynde nu"
if input() == 'y':
    print("Led os begynde!")
    else:
        ##    ø   æ    å
        print("okay Dokay, Partner")
'''
import string
import random
#reload(sys)


allowed = string.ascii_letters +'æøå'
print(allowed)
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
# print(dict)
def quiz():
    print("welcome to the Danish quiz")
    print("Intast 'y' for at begynde nu")
    if input() == 'y':
        print("Led os begynde!")
    else:
        print("okay Dokay, Partner")
    # print(random.choice(dict[2]))
    key,value = random.choice(list(dict.items()))
    score = 0
    print("hvad oversætter "+ key +" til?")

    quest = input()
    print(quest)
    if quest == value:
        print("ja!")
    else:
        print("nej...")
    print(value)
    print(input("egen?"))
    if input() == 'y':
        quiz()
    else:
        print("Farvel!")
quiz()
