class ErreurSaisie(Exception):
    pass

class ErrorCalcul(Exception):
    pass

# fonction de saisie
class Calcul:
    def __init__(self,message):
        self.mes=message
    
    def saisi_nombre(self):
        try:
            nombre = int(input("entrer une valeure :"))
            if nombre < 0:
                raise ErreurSaisie("le nombre doit etre positif")# il stop une condition et renvoie une erreur et afficher une classe
            return nombre
        except ValueError:
            raise ErreurSaisie("entrer un nombre entier!")
    
    
    def Division(self,nbr1, nbr2):
        try:
            resultat= nbr1/nbr2
            #if resultat == float("int"):
                #raise ErrorCalcul("errerur division par zero")
            return resultat
        except ZeroDivisionError:
            raise ErrorCalcul ("division par zero")

    


try:
    nombre1= Calcul("saisi de valeur").saisi_nombre()
    nombre2 = Calcul("saisie de valeur").saisi_nombre()
    result= Calcul("calculer").Division(nombre1,nombre2)
    print("le resultat de la division est :", result)
except (ErreurSaisie, ErrorCalcul) as e:
    print("une erreure est survenue: ",e)

    

