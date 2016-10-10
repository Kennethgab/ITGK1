antall_kvinner = 0
antall_menn = 0
antall_fag = 0
antall_itgk = 0
antall_timer_lekser = 0
temp_mann = 0
temp_kvinne = 0
spm = 0
kjonn = str


def kjonnsvalg():
    print("Er du mann eller kvinne? tast inn f for kvinne og m for mann ")
    global temp_mann
    global temp_kvinne
    while(temp_mann != 1 or temp_kvinne != 1 ):
        spm=str(input())
        if(spm=="m"):
            temp_mann = 1
            kjonn = "mann"
            return kjonn
            return temp_mann
        elif(spm=="f"):
            temp_kvinne = 1
            kjonn= "kvinne"
            return temp_kvinne
            return kjonn
        else:
            print("Du kan bare taste inn f eller m")

def aldervalg():
    print("hvor gammel er du?")
    while(spm != int):
        spm = input()
        if(spm == int):
            temp_alder = spm
            if(temp_alder <= 25 and temp_alder >= 16):
                return temp_alder
            else:
                print("Du er ikke i den rette aldersgruppen for studien. Avslutter.")
                temp_mann = 0
                temp_kvinne = 0
                kjonn = str
                return temp_mann
                return temp_kvinne
                return kjonn
                return main()



        if(spm== str):
            print("Du må taste inn en alder")









def main():
 while(spm != "hade"):

