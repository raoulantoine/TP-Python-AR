class Caisse(object):

    def appliquerTVA(self,chiffre):
        self = chiffre * 1.2
        return self



    def appliquerUneRemise(self,chiffre):
            self = chiffre * 0.95
            print("Remise 5% =", round((chiffre - self),2)," €")
            print("Prix HT =", round(self,2) ," €")
            return self
            #sousTotalHT = prixAvecRemise