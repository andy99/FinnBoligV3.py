# The pattern
x, y, z = [1, 2, 3]

# also works in loops:
Gunnar = [(28, 'M',"Braveman"), (4, 'a','Tull'), (1990, 'r','kom igjen')]
for x, y, z in Gunnar:
    print(x)  # prints the numbers 28, 4, 1990

# and also
for index, (x, y,z) in enumerate(Gunnar):
    print(x)  # prints the numbers 28, 4, 1990


    
table = {'Gunnar Andresen': 4127, 'Nikolai Andresen': 4098, 'Elisabeth Andresen': 7678}
for name, phone in table.items():
    print('{0:1} ==> {1:10d}'.format(name, phone))
    
def hello(name):
    print( "Hello, %s!" % name)
 
hello("Gunnar Andresen og Nikloai Andresen") 

class navn(object):  
    def __init__(self,navn):
        self.navn =navn
        print(navn)
        
        
dette = "Dette er bra"
gunnar = navn(dette)        
         
# weight = float(input("How many pounds does your suitcase weigh? "))
# if weight > 50:
#     print("There is a $25 charge for luggage that heavy.")
# elif    
#     print("Thank you for your business.")         
    