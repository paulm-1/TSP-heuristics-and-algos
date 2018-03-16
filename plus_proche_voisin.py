import time,sys
class Graphe:
    def __init__(self,graphe):
        self.graphe =graphe

    def plusProche(self,nb_sommet,sommet):
        tete=sommet
        parcours=[]
        cycle=[]
        parcours.append(tete)
        while(len(parcours)<nb_sommet):
            minArc=sys.maxint
            minSommet=None
            for i in range(nb_sommet):
                i=i+1
                if i not in parcours:
                    if self.graphe[parcours[-1]][i]<minArc:
                        minArc=self.graphe[parcours[-1]][i]
                        minSommet=i
            parcours.append(minSommet)
        print parcours
                    
                
        
tps1 = time.clock() 

w=[0,[0,0,5,8,4,3,2],
   [0,5,0,4,2,1,3],
   [0,8,4,0,7,5,4],
   [0,4,2,7,0,9,8],
   [0,3,1,5,9,0,4],
   [0,2,3,4,8,4,0]]
g=Graphe(w)
g.plusProche(6,1)
tps2 = time.clock()
print "temps d'execution"
print(tps2 - tps1)
