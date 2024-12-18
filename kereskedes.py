import random


def eladas(jatekos, max, min):  #létreh -> arres_max + arres_min ---> paraméternek adni
    arres:int=int(random.random()*(max-min+1)+min)
    jatekos.kredit = int(jatekos.kredit+(jatekos.aru/100*(arres+100)))
    jatekos.aru=0   #???? nem lesz fentebb is 0? vagy csak ebben a sorban változik az értéke

def vasarol_valaszt(jatekos):  #mainben akk hívjuk, ha vasarolE input értéke True
    vasarol_lista=[]
    valsztKerdes:str=input("Mit szeretnél vásárolni?"
                           "\nHa:"
                           "\n\tüzemanyagot - a + enter,"
                           "\n\tárut - b + enter,"
                           "\n\tfelszerelést - c +enter,"
                           "\nválasztásod:")
    if(valsztKerdes=="a"):
        uzemVasar:str=input("Fél tank ára 1 kredit (írj:fél), teljes tank ára 2 kredit (írj:egész):")
        while(uzemVasar!="fél" or uzemVasar!="egész")
            uzemVasar: str = input("Nem jó!\nFél tank ára 1 kredit (írj:fél), teljes tank ára 2 kredit (írj:egész):")
        if(uzemVasar=="fél"):
            jatekos.tank+=0,5
        else:
            jatekos.tank+=1
    elif(valsztKerdes=="b"):
        mennyiArut:int=int(input())
        '''valsztKerdes="dokkoló"
        vasarol_lista=vasarol_lista.append(valsztKerdes)'''
    while(valsztKerdes!=@):
        i=0
        while(i<=len(vasarol_lista[])):
            if(vasarol_lista[i]==)
        valsztKerdes=input("Kérsz még valamit?"
                           "\nHa nem írj egy @ jelet!"
                           "\nHa igen,"
                           "\n\tdokkolót - a + enter,"
                           "\n\ttolmácsgépet - b + enter,"
                           "\n\tkonténert - c +enter,"
                           "\n\tárut - d + enter!"
                           "\nválasztásod:")
        vasarol_lista=vasarol_lista.append(valsztKerdes)
        '''i=0
        while(i<=len(vasarol_lista)):
            if(vasarol_lista[i])
                valsztKerdes = input()'''
        vasarol_lista=vasarol_lista.append(valsztKerdes)
def vasarol(jatekos, valasztas):

