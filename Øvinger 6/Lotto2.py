import random




numbers = list(range(1,35))

myGuess = []

print("Tast inn 7 forskjellige lottotall fra og med 1 til og med 34 ")
while len(myGuess) != 7:


    addNumber = str(input())
    if addNumber.isdigit() == True :

        addNumber = int(addNumber)
        if addNumber > 34 or addNumber < 1:
            print("Tall utenfor grensen 1-34")
        elif addNumber in myGuess:
            print("Tallet er del av listen allerede")
        else:
            myGuess.append(addNumber)

    elif addNumber.isdigit() == False:
        print("Tast inn positivt  heltall fra 1-34")
print("Du gjettet tallene ", myGuess)




def numberPull(amount):
    winnerList = []
    while(len(winnerList) != amount):
        takeNumber = random.randint(1,34)
        if takeNumber not in winnerList:
            winnerList.append(takeNumber)

    return winnerList


def compList(list1,list2):
    intersection = list(set(list1).intersection(set(list2)))
    return len(intersection)

def premie(lottotall,tilleggstall):
    if lottotall == 4 and tilleggstall == 1: return 45
    elif lottotall == 5: return 95
    elif lottotall == 6: return 3385
    elif lottotall == 6 and tilleggstall == 1: return 102110
    elif lottotall == 7: return 2749455
    else: return 0


liste_lottotall = numberPull(7)
liste_tilleggstall = liste_lottotall

while compList(liste_lottotall,liste_tilleggstall) != 0:
    liste_tilleggstall = numberPull(3)

lottotall = compList(liste_lottotall,myGuess)
tilleggstall = compList(liste_tilleggstall,myGuess)
premie = premie(lottotall,tilleggstall)
print("Lottotallene som ble trukket var ",liste_lottotall)
print("Tilleggstallene som ble trukket var " ,liste_tilleggstall)
print("Du har {} lottotall rett" . format(lottotall))
print("Du har {} tilleggstall rett" .format(tilleggstall))
print("Du har vunnet {} kroner!" . format(premie))

