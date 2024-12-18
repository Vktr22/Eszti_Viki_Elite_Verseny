from Jatekos import Jatekos
import utazas
jatekos= Jatekos(10,0,0, False, False,0,1,"Thorodin")

uticel=utazas.hova_utazzunk()

if(uticel="a"):
    jatekos.pozicio="Ydalir"

elif(uticel="b"):
    jatekos.pozicio="Vidar"