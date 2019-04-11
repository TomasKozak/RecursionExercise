Napíšte pythonovský skript, v ktorom zadefinujete štyri funkcie na prácu so zoznamami. Vstupom pre všetky tieto funkcie bude zoznam, ktorý môže obsahovať čísla, reťazce, ale aj ďalšie podzoznamy. Tieto podzoznamy môžu opäť obsahovať ďalšie podzoznamy, atď. Napríklad aj takýto zoznam ['a', ['dom', [2], 3], [], [[[2]]], 'b'] môže byť vstupom do vašich funkcií.

zoznam_prvkov()
Funkcia zoznam_prvkov(zoznam) vráti sploštený zoznam prvkov daného zoznamu, teda taký, ktorý už neobsahuje žiadne podzoznamy.
Pôvodný zoznam pri tom ostane bez zmeny.

splosti()
Funkcia splosti(zoznam) sploští daný vstupný zoznam. Na rozdiel od predchádzajúcej funkcie táto nič nevracia, len modifikuje vstupný zoznam. Napr.

nahradeny_zoznam()
Funkcia nahradeny_zoznam(zoznam, hodnota1, hodnota2) vráti kópiu pôvodného zoznamu, v ktorom budú všetky prvky vstupného zoznamu s hodnotou hodnota1 nahradené hodnotou hodnota2. Ak sú nejakými prvkami opäť zoznamy, tak bude hodnota1 nahradená hodnotou2 aj v týchto zoznamoch, aj ich podzoznamoch atď. 

nahrad()
Funkcia nahrad(zoznam, hodnota1, hodnota2) nahradí v danom zozname zoznam všetky prvky s hodnotou hodnota1 hodnotou hodnota2. Ak sú nejakými prvkami opäť zoznamy, tak nahrádza aj v týchto zoznamoch, aj v ich podzoznamoch atď. Funkcia nič nevracia, len modifikuje vstupný zoznam. 
