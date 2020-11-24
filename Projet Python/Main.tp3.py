
from Caisse import Caisse 
from Produit import Produit

c = Caisse()

p1 = Produit("Banane",4,20,80)
p2 = Produit("Pomme",2,10,20)
p3 = Produit("Orange",2,3,6)
p4 = Produit("Poire",3,5,15)

listeFruits = [p1, p3, p2, p4]

sousTotalHT = 0

for fruit in range(len(listeFruits)): 
    print(listeFruits[fruit].nom)

# nbIdProduit = int(input('Entrez l'identifiant du produit à afficher : '))

try:
    nbIdProduit = int(input('Entrez un identifiant de produit à afficher : '))
    print(listeFruits[nbIdProduit])
except IndexError:
    print("Oops! Votre saisie est incorrecte")

for fruit in range(len(listeFruits)):
                    sousTotalHT = sousTotalHT + listeFruits[fruit].totalHT
print("TOTAL HT =", round(sousTotalHT,2), " €" )

if sousTotalHT > 200:
    sousTotalHT = c.appliquerUneRemise(sousTotalHT)
#else: 
    #print("Total HT =", round(sousTotalHT,2), " €")

print("TOTAL TTC =", round(c.appliquerTVA(sousTotalHT),2)," €")