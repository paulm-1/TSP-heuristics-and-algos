import time,sys,threading
from threading import Thread 
class Graphe:
    def __init__(self,graphe):
        self.graphe =graphe
        self.coutMin=sys.maxint
        self.cheminMin=None
        self.cpt=0
        self.sem=threading.BoundedSemaphore(value=1)
        
    def arcExist(self,i,j):
        if self.graphe[i][j]!=None:
            return True
        return False
    def dejaVisite(self,chemin,e):
        return self.estElement(chemin,e)
        
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
        cout=0
        if self.longueur(seq)>1:
            for i in range(self.longueur(seq)-1):
                if self.arcExist(seq[i],seq[i+1]):
                    cout+=self.graphe[seq[i]][seq[i+1]]
        return cout
    
    def visiterSommet(self,chemin,n,s):
        ch=self.cloner(chemin)
        self.ajouterEnQueue(ch,s)
        self.explorerCircuits(ch,n)
        
    def explorerCircuits(self,chemin,n):
        if self.longueur(chemin)==n and self.arcExist(self.queue(chemin),self.tete(chemin)):
            cout=self.coutChemin(chemin)+self.graphe[self.queue(chemin)][self.tete(chemin)]
            chemin=self.ajouterEnQueue(chemin,chemin[0])
            self.imprimer(chemin)
            print 'cout du chemin'
            print cout
            self.cpt+=1
            self.majCheminMin(chemin,cout)
        else:
            for s in range(n):
              s=s+1
              if self.arcExist(self.queue(chemin),s) and self.dejaVisite(chemin,s)==False and self.coutEstime(chemin,s,n)<self.coutMin:
                  t = Thread(None,self.visiterSommet,None,(chemin,n,s))
                  t.start()
                  t.join()

    
        
    def trouverCircuitMin(self,sommetDepart,n):
        chemin=self.creer()
        self.ajouterEnQueue(chemin,sommetDepart)
        self.explorerCircuits(chemin,n)
        
    def majCheminMin(self,chemin,cout):
        if cout<self.coutMin:
            self.sem.acquire()
            if cout<self.coutMin:
                self.cheminMin=chemin
                self.coutMin=cout
            self.sem.release()
        return self.coutMin
    
    def coutMinim(self,couts,chemin,aExclure):
        cout=sys.maxint
        for i in range(len(couts)-1):
            i+=1
            if self.dejaVisite(chemin,i)==False or self.element(chemin,0)==i:
                if couts[i] and i!=aExclure :
                    cout=min(couts[i],cout)
        if cout==sys.maxint:
            cout=0
        return cout
    
    def coutEstime(self,chemin,sommet,n):
        cout=self.coutChemin(chemin)
        cout+=self.graphe[self.queue(chemin)][sommet]
        cout+=self.coutMinim(self.graphe[sommet],chemin,self.tete(chemin))
        for s in range(n):
            s+=1
            if s !=sommet and self.dejaVisite(chemin,s)==False:
                cout+=self.coutMinim(self.graphe[s],chemin,sommet)
        return cout
                
        
tps1 = time.clock() 
#w=[None,[None,None,2,9,None],[None,1,None,6,4],[None,None,7,None,8],[None,6,3,None,None]]
#villes=[None,[None,None,27,43,16,30,26],[None,7,None,16,1,30,25],[None,20,13,None,35,5,0],[None,21,16,25,None,18,18],[None,12,46,27,48,None,5],[None,23,5,5,9,5,None]]
#villes2=[None,[None,None,27,43,16,30,26,75,28,29,90],[None,7,None,16,1,30,25,60,0,41,80],[None,20,13,None,35,5,0,80,90,100,70],[None,21,16,25,None,18,18,55,25,21,60],[None,12,46,27,48,None,5,56,28,15,50],[None,23,5,5,9,5,None,19,18,21,40],[None,23,5,5,9,5,None,19,18,21,40],[None,23,5,5,9,5,None,19,18,21,40],[None,23,5,5,9,5,None,19,18,21,40],[None,23,5,5,9,5,None,19,18,21,40]]
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
g.trouverCircuitMin(1,6)
print "nb de circuits"
print g.cpt
print "chemin min"
print g.cheminMin
print "Cout min"
print g.coutMin
tps2 = time.clock()
print "temps d'execution"
print(tps2 - tps1)
