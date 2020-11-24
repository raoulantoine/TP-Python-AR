
from Caisse import Caisse 

c = Caisse()

tabFruitUn = {"Nom":"Banane","Prix": 4.5,"Quantité": 20,"TotalHT":84.6}
tabFruitDeux = {"Nom":"Pomme","Prix": 2,"Quantité": 10,"TotalHT":20}
tabFruitTrois = {"Nom":"Orange","Prix": 1.5, "Quantité":3,"TotalHT":4.5}
tabFruitQuatre = {"Nom":"Poire","Prix":3,"Quantité":50,"TotalHT":150}

tabFruits = [tabFruitUn, tabFruitDeux, tabFruitQuatre]
sousTotalHT = 0
tva = 1.2
print(tabFruits)

# nbIdProduit = int(input('Entrez l'identifiant du produit à afficher : '))

try:
    nbIdProduit = int(input('Entrez un identifiant de produit à afficher : '))
    print(tabFruits[nbIdProduit])
except IndexError:
    print("Oops! Votre saisie est incorrecte")

for fruit in tabFruits:
                    sousTotalHT = sousTotalHT + fruit['TotalHT']
print("Sous-Total HT =", round(sousTotalHT,2), " €" )

if sousTotalHT > 200:
    sousTotalHT = c.appliquerUneRemise(sousTotalHT)
else: 
    print("Total HT =", round(sousTotalHT,2), " €")

print("TOTAL TTC =", round(c.appliquerTVA(sousTotalHT),2)," €")