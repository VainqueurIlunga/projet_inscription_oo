import uuid
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self,categorie_compte):
        super().__init__()
        self.cat_compte = categorie_compte
    
    @abstractmethod
    def seConnecter(self):
        pass

    @abstractmethod
    def Afficher(self):
        pass

class Faculte:
    def __init__(self,nom_fac):
        self.fac_nom = nom_fac

class Departement:
    def __init__(self, nom_depart, fac):
        self.depart_nom = nom_depart
        self.faculte = fac
        

class Promotion:
    def __init__(self, nom_promo):
        self.promo= nom_promo

class Inscription:
    def __init__(self,date_inscri,Anacad, constat, etud):
        self.date_inscrit =date_inscri
        self.anneAcad = Anacad
        self.constat = constat
        self.etudiant = etud
        

class Etudiant(User):
    def __init__(self, categorie_compte, nom, prenom, promotion, departement,faculte):
        super().__init__(categorie_compte)
        self.etud_nom = nom
        self.etud_prenom = prenom
        self.etud_promtion = promotion
        self.etud_departement = departement
        self.etud_faculte = faculte

    def seConnecter(self, comptes, code = 1234,):
        if code == True and comptes == self.etud_nom:
            print(f"{self.etud_nom} bienvenue! ")
        else:
            print(f"mot de passe ou compte erroné")


    def Afficher(self):
        print(f"le compte :{self.cat_compte}")
        print(f"nom etudiant: {self.etud_nom}")
        print(f"la promotion : {self.etud_promtion}")
        print(f"departement :{self.etud_departement}")
        print(f"faculté: :{self.etud_faculte}")
    


promo=Promotion("bac3")
fac= Faculte("informartique")
depart= Departement("genie logiciel",fac)
etudiant1= Etudiant("etudiant","ilunga","vainqueur",promo.promo,depart.depart_nom,fac.fac_nom)
etudiant1.Afficher()


inscription1= Inscription("25-06-2023","2023-2024","tous les documents sont complet",etudiant1)

"""
etud1= Etudiant("etudiant","ilunga","vainqueur","bac3","GL","informatique")
print(etud1.etud_promtion)
etud1.seConnecter("junion")
"""