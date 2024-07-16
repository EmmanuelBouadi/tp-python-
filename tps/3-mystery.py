print("***** Petit jeu permettant de deviner un nombre entre 1   et 100 en 5 essais *****")

import random
n = random.randint(1,100)

variable = input("saisir un nombre entre 1 et 100: ")
    
while not variable.isdigit(): 
    variable = input("saisir un nombre entre 1 et 100: ")

for i in range ( 1 , 5) : 
      if int(variable) > n : 
            print ("Très grand! choisir un autre plus petit")
            variable = input("saisir un nombre entre 1 et 100: ")
            while not variable.isdigit(): 
                  variable = input("saisir un nombre entre 1 et 100: ")
      elif int(variable) < n :
            print ( "Très petit! choisir un autre plus grand")
            variable = input("saisir un nombre entre 1 et 100: ")
            while not variable.isdigit(): 
                  variable = input("saisir un nombre entre 1 et 100: ")
      else :
          break
      
if  i < 6 and int(variable) == n : 
 print ( "Bravo!!!! vous avez trouvé le bon nombre!!!","en",i,"essais")
else :  
 print( "Game over!!! le nombre etait :",n)