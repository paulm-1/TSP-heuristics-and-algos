import time
class Graphe:
    def __init__(self,graphe):
        self.graphe =graphe
        self.coutMin=None
        self.cheminMin=None
        self.cpt=0
    def arcExist(self,i,j):
        if self.graphe[i][j]!=None:
            return True
        return False
    def dejaVisite(self,chemin,e):
        return self.estElement(chemin,e)
    
    def genererCircuit(self,chemin,n):
        if self.longueur(chemin)==n and self.arcExist(self.queue(chemin),self.tete(chemin)):
            chemin1=self.cloner(chemin)
            chemin1=self.ajouterEnQueue(chemin1,chemin1[0])
            self.imprimer(chemin1)
            a=self.coutChemin(chemin)
            print 'cout du chemin'
            print a
            self.cpt+=1
        else:  
          for s in range(n):
              s=s+1
              if self.arcExist(self.queue(chemin),s) and self.dejaVisite(chemin,s)==False:
                  ch=self.cloner(chemin)
                  self.ajouterEnQueue(ch,s)
                  self.genererCircuit(ch,n)
    def genererTousLesCircuits(self,sommetDepart,n):
        chemin=self.creer()
        self.ajouterEnQueue(chemin,sommetDepart)
        self.genererCircuit(chemin,n)
        
    def creer(self):
        seq=[]
        return seq
    def longueur(self,seq):
        return len(seq)
    def cloner(self,seq):
        s1=[]
        for i in seq:
            s1.append(i)            
        return s1
    def ajouterEnQueue(self,seq,sommet):
        seq.append(sommet)
        return seq
    def tete(self,seq):
        if seq:
            return seq[0]
    def queue(self,seq):
        if seq:
            return seq[-1]
    def element(self,seq,i):
        if seq[i]:
            return seq[i]
    def estElement(self,seq,s):
        if s in seq:
            return True
        return False
    def imprimer(self,seq):
        print seq
    def coutChemin(self,seq):
        if self.longueur(seq)>1:
            cout=0
            for i in range(self.longueur(seq)-1):
                if self.arcExist(seq[i],seq[i+1]):
                    cout+=self.graphe[seq[i]][seq[i+1]]
            return cout
        else:
            return None
    def explorerCircuits(self,chemin,n):
        if self.longueur(chemin)==n and self.arcExist(self.queue(chemin),self.tete(chemin)):
            cout=self.coutChemin(chemin)+self.graphe[self.queue(chemin)][self.tete(chemin)]
            chemin1=self.cloner(chemin)
            chemin1=self.ajouterEnQueue(chemin1,chemin1[0])
            self.imprimer(chemin1)
            print 'cout du chemin'
            print cout
            self.cpt+=1
            if self.coutMin==None:
                self.coutMin=cout
            if cout<self.coutMin:
                self.cheminMin=chemin
                self.ajouterEnQueue(self.cheminMin,self.cheminMin[0])
                self.coutMin=cout
        else:
            for s in range(n):
              s=s+1
              if self.arcExist(self.queue(chemin),s) and self.dejaVisite(chemin,s)==False:
                  ch=self.cloner(chemin)
                  self.ajouterEnQueue(ch,s)
                  self.explorerCircuits(ch,n)
    def trouverCircuitMin(self,sommetDepart,n):
        chemin=self.creer()
        self.ajouterEnQueue(chemin,sommetDepart)
        self.explorerCircuits(chemin,n)
            
                
        
tps1 = time.clock() 
#w=[None,[None,None,2,9,None],[None,1,None,6,4],[None,None,7,None,8],[None,6,3,None,None]]
#villes=[None,[None,None,27,43,16,30,26],[None,7,None,16,1,30,25],[None,20,13,None,35,5,0],[None,21,16,25,None,18,18],[None,12,46,27,48,None,5],[None,23,5,5,9,5,None]]
#villes1=[None,[None,None,27,43,16,30,26],[None,7,None,16,1,30,25],[None,20,13,None,35,5,0],[None,21,16,25,None,18,18],[None,12,46,27,48,None,5],[None,23,5,5,9,5,None]]
#villes2=[None,[None,None,27,43,16,30,26,75,28,29,90],[None,7,None,16,1,30,25,60,0,41,80],[None,20,13,None,35,5,0,80,90,100,70],[None,21,16,25,None,18,18,55,25,21,60],[None,12,46,27,48,None,5,56,28,15,50],[None,23,5,5,9,5,None,19,18,21,40],[None,23,5,5,9,5,None,19,18,21,40],[None,23,5,5,9,5,None,19,18,21,40],[None,23,5,5,9,5,None,19,18,21,40],[None,23,5,5,9,5,None,19,18,21,40]]
#villes3=[None,[None,None,5,43,16,30,26,75,28,29,90,26,75,28,29,90],[None,5,None,43,16,30,26,75,28,29,90,26,75,28,29,90],[None,8,27,None,16,30,26,75,28,29,90,26,75,28,29,90],[None,1,27,43,None,30,26,75,28,29,90,26,75,28,29,90],[None,1,27,43,16,None,26,75,28,29,90,26,75,28,29,90],[None,5,27,43,16,30,None,75,28,29,90,26,75,28,29,90],[None,1,27,43,16,30,26,None,28,29,90,26,75,28,29,90],[None,2,27,43,16,30,26,75,None,29,90,26,75,28,29,90],[None,1,27,43,16,30,26,75,28,None,90,26,75,28,29,90],[None,1,27,43,16,30,26,75,28,29,None,26,75,28,29,90],[None,1,27,43,16,30,26,75,28,29,90,None,75,28,29,90],[None,1,27,43,16,30,26,75,28,29,90,26,None,28,29,90],[None,1,27,43,16,30,26,75,28,29,90,26,75,None,29,90],[None,1,27,43,16,30,26,75,28,29,90,26,75,28,None,90],[None,1,27,43,16,30,26,75,28,29,90,26,75,28,29,None]]
villes2=[None,[None,None,2,12,6,15,16,20,13,14,16,23,23,29,25,26,27],
         [None,2,None,10,8,17,18,18,15,16,18,25,25,27,27,28,29],
         [None,12,10,None,14,15,14,10,25,26,26,19,23,17,29,28,27],
         [None,6,8,14,None,17,18,16,15,16,18,25,26,23,27,28,29],
         [None,15,17,15,17,None,1,5,16,17,19,16,20,14,26,25,24],
         [None,16,18,14,18,1,None,4,17,18,20,15,19,13,25,24,23],
         [None,20,18,10,16,5,4,None,21,20,18,11,15,9,21,20,19],
         [None,13,15,25,15,16,17,21,None,1,3,10,12,16,14,15,16],
         [None,14,16,26,16,17,18,20,1,None,2,9,13,15,15,16,17],
         [None,16,18,26,18,19,20,18,3,2,None,7,15,13,17,18,19],
         [None,23,25,19,25,16,15,11,10,9,7,None,12,6,18,17,16],
         [None,23,25,23,26,20,19,15,12,13,15,12,None,6,18,17,16],
         [None,29,27,17,23,14,13,9,16,15,13,6,6,None,12,11,10],
         [None,25,27,29,27,26,25,21,14,15,17,18,18,12,None,1,2],
         [None,26,28,28,28,25,24,20,15,16,18,17,17,11,1,None,1],
         [None,27,29,27,29,24,23,23,19,16,17,19,16,16,10,2,1,None]]

w=[None,[None,None,27,43,16,31,26],
   [None,7,None,16,1,30,25],
   [None,20,15,None,35,5,0],
   [None,21,16,25,None,21,18],
   [None,12,16,27,48,None,5],
   [None,23,5,5,9,5,None]]
g=Graphe(w)
print "Tous les ciruits visites pour calculer le chemin min"
#g.genererTousLesCircuits(1,4)
g.trouverCircuitMin(1,6)
print "nombre de chemins"
print g.cpt
print "chemin min"
print g.cheminMin
print "Cout min"
print g.coutMin
tps2 = time.clock()
print "temps d'execution"
print(tps2 - tps1)
