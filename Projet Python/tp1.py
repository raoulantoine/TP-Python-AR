#3.1. Mise en place de notre programme de caisse

#Demander à l’utilisateur de saisir un prix hors taxe (HT) ainsi qu’une quantité
prixHT = int(input('Entrez un prix hors taxe :'))
quantite = int(input('Entrez une quantité :'))

#calcul
import sys
prixHT = int(input('Entrez un prix hors taxe :'))
if  prixHT<=0:
    print('Désolé recommence')
    sys.exit()
quantite = int(input('Entrez une quantité :'))
if quantite<=0:
    print('Désolé recommence')
    sys.exit()
calculTVA = (prixHT * quantite) * 1.2
if calculTVA > 200:
    remise = calculTVA * 0.95
    print("Le prix TTC avec remise", remise)
else :
    print("Le prix TTC sans remise", calculTVA)

#3.2 Gestion de plusieurs produits

nbProduits = int(input('Entrez le nombre de produits à renseigner'))
prixBoucle = 0

for i in range(nbProduits):

    prixHT = int(input('Entrez un prix hors taxe :'))
    quantite = int(input('Entrez une quantité :'))

    prixAvecTva = (prixHT * quantite) * 1.2

    if prixAvecTva > 200:
        prixAvecRemise = prixAvecTva * 0.95
        print("Votre remise est de ", prixAvecTva - prixAvecRemise)
        print("(if) Le prix total est de ", prixAvecRemise)
        prixAvecTva = prixAvecRemise
    else: 
        print("(else) Le prix total est de ", prixAvecTva)

    prixBoucle = prixBoucle + prixAvecTva

print("Le prix total de votre commande s'élève : ", prixBoucle)
