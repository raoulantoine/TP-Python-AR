#4.1. Utilisation de données structurées

tabFruitUn = {"Nom":"Banane","Prix": 4,"Quantité": 2,"TotalHT":8}
tabFruitDeux = {"Nom":"Pomme","Prix": 2,"Quantité": 1,"TotalHT":2}
tabFruitTrois = {"Nom":"Orange","Prix": 1.5, "Quantité":3,"TotalHT":4.5}
tabFruitQuatre = {"Nom":"Poire","Prix":3,"Quantité":5,"TotalHT":15}

tabFruits = [tabFruitUn, tabFruitDeux, tabFruitQuatre]
sousTotalHT = 0
print(tabFruits)

# nbIdProduit = int(input('Entrez l'identifiant du produit à afficher : '))

try:
    nbIdProduit = int(input('Entrez un identifiant de produit à afficher : '))
    print(tabFruits[nbIdProduit])
except IndexError:
    print("Oops! Votre saisie est incorrecte")

for fruit in tabFruits:
                    sousTotalHT = sousTotalHT + fruit['TotalHT']
                    # sousTotalHT =+ fruit['TotalHT']

print("Sous Total HT = ", sousTotalHT)






