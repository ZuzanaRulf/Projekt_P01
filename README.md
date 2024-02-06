Projekt P01
Textový analyzátor

Program obsahuje následující:

1.	Úvod - hlavička.
2.	Vyžádá si od uživatele přihlašovací jméno a heslo 
3.	Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů 
4.	Pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty
5.	Pokud není registrovaný, upozorni jej a ukonči program.**
    
Registrováni jsou následující uživatelé:
+------+-------------+
| user |   password  |
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   |
+------+-------------+

6.	Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS:
    o	Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí,
    o	pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.
7.	Pro vybraný text spočítá následující statistiky:
    o	počet slov,
    o	počet slov začínajících velkým písmenem,
    o	počet slov psaných velkými písmeny,
    o	počet slov psaných malými písmeny,
    o	počet čísel (ne cifer),
    o	sumu všech čísel (ne cifer) v textu.
8.	Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu.
