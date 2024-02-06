"""

projekt_1.py: první projekt do Engeto Online Python Akademie

author: Zuzana Rulfová

email: rulfova.zuzana@gmail.com

discord: zuzana576

"""



###### VSTUPNI DATA ################################################

userList = {"bob" : "123", "ann" : "pass123", "mike" : "pasword123", "liz" : "pass123"}
oddelovaciCara = "-" * 40

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
pocetTextu = len(TEXTS)

####################################################################

# Vyžádání uživatelského jména
user = input("username:")

# Vyžádání hesla
password = input("password:")

# Ověření přihlašovacích údajů

# Registrovaný uživatel
if password == userList[user]:
    # Uvítání uživatele
    print("Welcome to the app,", user)
    print("We have",pocetTextu,"texts to be analyzed.")
    print(oddelovaciCara)
        
# NEregistrovaný uživatel    
else:
    print("unregistered user, terminating the program...")
    quit() # ukončit program!!!  
        

#################################################################### 

# Výběr textu pro analýzu
vyberTextu = str(pocetTextu)
hlaska = "Enter a number btw. 1 and " + vyberTextu + " to select:"
cisloTextu = input(hlaska)
print(oddelovaciCara)


# Oveření, zda je zadané číslo, popř. převede str na int
if cisloTextu.isnumeric():
    cisloTextuInt = int(cisloTextu)
else:
    print("This is not a number.")
    quit() # ukončit program!!!


# Ověření výběru textu
povolenyVyber = range(1,pocetTextu+1)
if cisloTextuInt not in povolenyVyber:
    print("Wrong number selected.")
    quit() # ukončit program!!!


####################################################################

# Analýza textu

vysledek = {
    "words" : 0,
    "titlecase" : 0,
    "uppercase" : 0,
    "lowercase" : 0,
    "numeric" : 0,
    "sum" : 0,
    }
    
counts = {}

# Vstup
text = TEXTS[cisloTextuInt-1]

slova = [] 

# Odstranění čárek, teček, atd. v textu
for ocisteneSlovo in text.split():
    slova.append(ocisteneSlovo.strip(".,:;!?")) 

# Počet všech slov
vysledek["words"] = len(slova)


# Jednotliva slova projdi
for slovo in slova:

    # Analýza délek slov
    # .. pokud daná délka slova není uložená, eviduj ji jako první hodnotu
    if len(slovo) not in counts:
        counts[len(slovo)] = 1
        
    # .. pokud číslo je uložené, inkrementuj původní hodnotu
    else:
        counts[len(slovo)] = counts[len(slovo)] + 1

    # Počítání různých druhů "slov"
    # ... slovo pouze z písmen
    if slovo.isalpha():
        # ... slovo s velkým prvním písmenem
        if slovo.istitle():
            vysledek["titlecase"] += 1
        # ... slovo z velkých písmen
        if slovo.isupper():
            vysledek["uppercase"] += 1 
        # ... slovo z malých písmen
        if slovo.islower():
            vysledek["lowercase"] += 1
    # ... slovo obsahující pouze číslice
    if slovo.isnumeric():
        vysledek["numeric"] += 1
        vysledek["sum"] += int(slovo)

# Vypsaný výstup pro jednotlivé druhy slov
print("There are",vysledek["words"],"words in the selected text.")
print("There are",vysledek["titlecase"],"titlecase words.")
print("There are",vysledek["uppercase"],"uppercase words.")
print("There are",vysledek["lowercase"],"lowercase words.")
print("There are",vysledek["numeric"],"numeric strings.")
print("The sum of all the numbers",vysledek["sum"])
print(oddelovaciCara)


# Graf délky slov
maximum = max(sorted(counts.values()))

print("LEN|  OCCURENCES "," " * (maximum - 13)," |NR.", sep="")
print(oddelovaciCara)

for i in sorted(counts):
    if i < 10:
        print("  ",i,"|","*" * counts[i]," " * (maximum - counts[i])," |", counts[i], sep="")
    else:
        print(" ",i,"|","*" * counts[i]," " * (maximum - counts[i])," |", counts[i], sep="")
