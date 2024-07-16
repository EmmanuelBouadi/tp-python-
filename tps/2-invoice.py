print("****Bienvenue sur JUMIO S.A.R.L****")
print("Votre facture: ")

while True:
    PU = input("P.U : ")
    if PU.isdigit():
        break
while True:
    Quantité = input("Quantité : ")
    if Quantité.isdigit():
        break

Montant = int(PU)*int(Quantité)
TVA= 0.18*int(Montant)
TTC=int(Montant)+int(TVA)

print(f"""Votre facture:
       
P.U : {PU} CFA 
Quantité :  {Quantité}

Montant HT :  {Montant} CFA 
TVA :  {TVA} CFA

Montant TTC : {TTC} CFA
""")

print("JUMIO vous Merci pour votre achat et vous souhaites de   Joyeuses fetes !!!!!!!")