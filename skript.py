# 5. zadanie: zoznamy
# autor: Tomáš Kozák
# datum: 28.11.2018


def zoznam_prvkov(zoznam):
    if zoznam == []:
        return []
    if type(zoznam[0]) == list:
        return zoznam_prvkov(zoznam[0]) + zoznam_prvkov(zoznam[1:])
    return [zoznam[0]] + zoznam_prvkov(zoznam[1:])

def splosti(zoznam):
    pole = []
    for prvok in zoznam:
        pole.append(prvok)
    zoznam.clear()
    for casti in zoznam_prvkov(pole):
        zoznam.append(casti)


def nahradeny_zoznam(zoznam, hodnota1, hodnota2):
    vysl = []
    for prvok in zoznam:
        if type(prvok) == list and prvok != hodnota1:
            vysl.append(nahradeny_zoznam(prvok, hodnota1, hodnota2))
        elif prvok == hodnota1:
            vysl.append(hodnota2)
        else:
            if prvok == hodnota1:
                vysl.append(hodnota2)
            else:
                vysl.append(prvok)
    return vysl

def nahrad(zoznam, hodnota1, hodnota2):
    pole = []
    for prvok in zoznam:
        pole.append(prvok)
    zoznam.clear()
    for prvky in nahradeny_zoznam(pole, hodnota1, hodnota2):
        zoznam.append(prvky)

print(nahradeny_zoznam([1, 2, 3, [1, 2], 3, [[[1]]], [], 2], 1, 'x'))
print(nahradeny_zoznam([3, [33, [333, [13], 13]], 36], [13], 'm'))








'''
pole = ['a', 8, 9]
print(pole)
hodnota1 = 'p'
for prvok in pole:
    if prvok == 8:
        pole[pole.index(prvok)] = hodnota1
print(pole)

pole = ['a', 8, 9]
'''

    
    

    

