from FunkResultat import FunkResultat
from datetime import datetime
import os
print("Hello")
f = open("D:\workplace_python\pythonapp\SjekkerResultater\Dntresultatdatoer.txt", "r")
#print(f.read())
Data = [ ]
for lines in f:
    Data.append(lines)
    BaneDato = Data[0]
    print(BaneDato)
    finnsemidato = BaneDato.find(';')
    lenbanedato  =len(BaneDato)
    print(finnsemidato)
    print(lenbanedato)
    utdato = BaneDato[finnsemidato + 1: lenbanedato]
    print(utdato)


