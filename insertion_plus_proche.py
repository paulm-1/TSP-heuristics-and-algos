import time,sys
class Graphe:
    def __init__(self,graphe):
        self.graphe =graphe
    
    def insertionPlusProche(self,nb_sommet):
        parcours=[]
        parcours.append(1)
        parcours.append(2)
        parcours.append(3)
        parcours.append(1)
        for i in range(nb_sommet):
            i=i+1
            if i not in parcours:
                dist=sys.maxint
                position=None
                for j in range(len(parcours)):
                    if dist>self.graphe[i][parcours[j]]:
                        dist=self.graphe[i][parcours[j]]
                        position=j
                p=[]
                for k in range(len(parcours)):
                    p.append(parcours[k])
                    if k==position:
                        p.append(i)
                parcours=p
        print parcours
                    
     
tps1 = time.clock() 

w=[0,[0,0,5,8,4,3,2],
   [0,5,0,4,2,1,3],
   [0,8,4,0,7,5,4],
   [0,4,2,7,0,9,8],
   [0,3,1,5,9,0,4],
   [0,2,3,4,8,4,0]]
g=Graphe(w)
g.insertionPlusProche(6)
tps2 = time.clock()
print "temps d'execution"
print(tps2 - tps1)
