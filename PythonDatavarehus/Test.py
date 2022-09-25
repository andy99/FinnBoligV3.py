import random
coding='utf-8'
from matplotlib import pyplot
x = [] # oppretter en liste x, som skal inneholde treningene 1-2-3-4-5-6 på x-akesn i diagrammet.
y = [] # oppretter en liste y, som skal inneholde frekvensen til de ulike terningsverdiene.
res = []
print(x,"X har verien"
for i in range(100):
  terning = random.randint(1,6)
  res.append(terning)
for j in range(1,7):
  x.append(j) # legger verdiene 1,2,3,4,5,6 i lista x.
  y.append(res.count(j)) # teller hvor mange det er av hver verdi i lista res, og legger antallaet i lista y.
  print((j),": " + str(res.count(j)))
  pyplot.bar(x,y) # viser stolpadiagram over dataene i x og y
#
pyplot.show() # aktiverer funksjonen pyplot