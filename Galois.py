import utilities
import QR
class CorpsGalois(object):
    global Tools
    
    Tools = utilities.utilities(QR.img)
    def __init__(self, p): # p polynome primitif représenté par un entier
        # Initialisation des champs.
        self.degre_max = (2 ** Tools.degre(p)) - 1
        self.exps = [0] * self.degre_max
        self.logs = [0] * (self.degre_max + 1)

        # À compléter.
        # Remplir les listes self.exps et self.logs

        p_x = 1

        for i in range(self.degre_max):
            self.exps[i] = p_x
            self.logs[p_x] = i

            p_x <<=1 #Mutliplier par x^1 puis 2 puis 3 puis etc///
            p_x = Tools.modulo(p_x,285)


    def plus(self, a, b):
        return a ^ b
       
    def moins(self, a, b):
        return a ^ b

    def fois(self, a, b):
        if (a ==0 or b == 0):
            return 0
        exposant = self.logs[a]+self.logs[b]
        exposant%=self.degre_max 

        return self.exps[exposant]
        
        

    def division(self, a, b):
        if b == 0:
            raise ZeroDivisionError()
        if (a == 0):
            return 0
        exposant = self.logs[a]-self.logs[b]
        exposant%=self.degre_max

        return self.exps[exposant]
        
        

    
    def puissance(self, a, n):
        if a == 0:
            return 0
        P =  self.logs[a]
        P = P*n
        P = P%self.degre_max

        return self.exps[P]
    

class AnneauPolynome(object):

    
    def __init__(self, corps):
        self.corps = corps

    def fois(self, p, q):
        r = [0] * (len(p) + len(q) - 1) # len(r) est le degré max du polynôme
        for i in range(len(p)):
            for j in range(len(q)):
                r[i+j] = self.corps.plus(r[i+j],self.corps.fois(p[i],q[j]))

        return r

        

    def reste_division(self, p, q):
        if len(q) == 0:
            raise ZeroDivisionError()
        while (len(q) <= len(p)):
            factor = self.corps.division(p[0],q[0])
            for i in range(len(q)):
                p[i] = self.corps.moins(p[i],self.corps.fois(q[i],factor))
            p.pop(0)
        return p

                
                    

                
        

    def generateur(self, n):
        Res = [1]
        for i in range(n):
            Res = self.fois(Res,[1,self.corps.puissance(2,i)])
        
        return Res
        

class Correcteur(object):

    def __init__(self, n_extra, p):
        self.anneau = AnneauPolynome(CorpsGalois(p))
        self.generateur = self.anneau.generateur(n_extra)

    def encode(self, donnees):
        avec_extra = donnees + [0] * (len(self.generateur) - 1)
        return self.anneau.reste_division(avec_extra, self.generateur)