#4.1. Utilisation de données structurées

fruitbanane = {"nom":"banane", "Prix":4, "Quantité":2,"Total HT":8}
fruitpomme = {"nom":"pomme", "Prix":2, "Quantité":1,"Total HT":2}
fruitorange = {"nom":"orange", "Prix":1.5, "Quantité":1,"Total HT": 1.5}
fruitpoire= {"nom":"poire", "Prix":3, "Quantité":5, "Total HT": 15}
tableauFruit = [fruitbanane, fruitpomme, fruitpoire]
print(tableauFruit)
try:
    nbId = int(input('Entrez l ID du produit :'))
    print(tableauFruit[nbId])
except IndexError:
    print("L ID n'est pas présent dans le tableau")





