from Jatekos import jatekos
from Jatekos import get_pozicio

def hova_utazzunk(jatekos):
    print(f"Hova utazzunk?\n")
    uticel:str=input(f"Ydalir bolygó ='a'  || Vidar bolygó ='b'")

    get_pozicio(jatekos)
    if(uticel="a"):
        set jatekos.pozicio="Ydalir"
    elif(uticel="b"):
        set jatekos.pozicio="Vidar"




    if(jatekos.pozicio="Thorodin"):
        if(uticel="a"):
        
            

