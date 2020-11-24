class Produit(object):

    nom=""
    prix=0
    qte=0
    totalHT=0

    def init (self, proNom, proPrix, proQte, 
    proTotalHT):
        self.nom = proNom
        self.prix = proPrix
        self.qte = proQte
        self.totalHT = proTotalHT

    def showNom(self):
        print(self.nom)

    def showPrix(self):
        print(self.prix)

    def showQte(self):
        print(self.qte)

    def showTotalHT(self):
        print(self.totalHT)