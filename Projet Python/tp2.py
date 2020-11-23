#4.1. Utilisation de données structurées

tabFruitUn = {"Nom":"Banane","Prix": 4,"Quantité": 20,"TotalHT":80}
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
                    # sousTotalHT =+ fruit['TotalHT']

print("Sous-Total HT =", sousTotalHT, " €" )

if sousTotHT > 200:
    prixAvecRemise = sousTotHT * 0.95
    print("Remise 5% =", round((sousTotHT - prixAvecRemise),2)," €")
    print("Prix HT =", round(prixAvecRemise,2) ," €")
    sousTotHT = prixAvecRemise
else: 
    print("Total HT =", round(sousTotHT, 2), " €")

print("TOTAL TTC =", round((sousTotHT * tva),2)," €")




