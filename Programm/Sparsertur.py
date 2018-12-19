# Tilfeldig sparsertur monte carlo simulation
import random
# coding=utf8
def random_walk(n):
  x,y = 0,0
  for i in range(n):
    (dx,dy) = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
    x += dx
    y += dy  
  return(x,y)  

number_of_walks = 1  

for walk_length in range(1,31):
    no_transport = 0
    for i in range(number_of_walks):
        (x,y) = random_walk(walk_length)
        distance = abs(x)  + abs(y)  
#         print(distance,"Distanse gatt")  
        if distance <= 4:
            no_transport += 1
#             print(no_transport,"Ingen transport")
    no_transport_prosent = float(no_transport) / number_of_walks 
    print("Tur nr = ", walk_length, "/%  Taxi tur hjem igjen = ", 100 * no_transport_prosent)                 