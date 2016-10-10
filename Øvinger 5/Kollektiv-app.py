def billettpris(alder):
    if(alder<5):
        pris=0
    elif(alder<=20 and alder>=5):
        pris=20
    elif(alder<=25 and alder>=21):
        pris=50
    elif(alder<=60 and alder>=26):
        pris=80
    elif(alder > 60):
        pris=0
    return pris
Småbarn =billettpris(3)
Barn = billettpris(7)
Student = billettpris(23)
Voksen = billettpris(30)
Honør = billettpris(80)

print(Småbarn,Barn,Student,Voksen,Honør)

