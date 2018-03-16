import time,random,sys
class Graphe:
    def __init__(self,graphe):
        self.graphe =graphe         
    def arcExist(self,i,j):
        if self.graphe[i][j]!=None:
            return True
    def longueur(self,seq):
        return len(seq)
    def distance_parcours(self,seq):
        if self.longueur(seq)>1:
            cout=0
            for i in range(self.longueur(seq)-1):
                if self.arcExist(seq[i],seq[i+1]):
                    cout+=self.graphe[seq[i]][seq[i+1]]
            return cout
        else:
            return None            
    def glouton(self,nb_sommet):
        pos1=None
        pos2=None
        minArc=sys.maxint
        parcours=[]
        for i in range(nb_sommet):
            i=i+1
            for j in range(nb_sommet):
                j=j+1
                if i!=j and self.graphe[i][j]<minArc:
                    pos1=i
                    pos2=j
                    minArc=self.graphe[i][j]
        parcours.append(pos1)
        parcours.append(pos2)
        while len(parcours)!=nb_sommet:
            pos1=None
            minArc=sys.maxint
            for i in parcours:
                for j in range(nb_sommet):
                    j=j+1
                    if j not in parcours and self.graphe[i][j]<minArc:
                        pos1=j
                        minArc=self.graphe[i][j]
            parcours.append(pos1)
        parcours.append(parcours[0])
        print parcours
        print self.distance_parcours(parcours)
                        
        
                
        
tps1 = time.clock()
w1=[0,[0,0,2,12,6,15,16,20,13,14,16,23,23,29,25,26,27],
   [0,2,0,10,8,17,18,18,15,16,18,25,25,27,27,28,29],
[0,12,10,0,14,15,14,10,25,26,26,19,23,17,29,28,27],
[0,6,8,14,0,17,18,16,15,16,18,25,126,23,27,20,29],
[0,15,17,15,17,0,1,5,16,17,19,16,20,14,26,25,24],
[0,16,18,14,18,1,0,4,17,18,20,15,19,13,25,24,23],
[0,20,18,10,16,5,4,0,21,20,18,11,15,9,21,20,19],
[0,13,15,25,15,16,17,21,0,1,3,10,12,16,14,15,16],
[0,14,16,26,16,17,18,20,1,0,2,9,13,15,15,16,17],
[0,16,18,26,18,19,20,18,3,2,0,7,15,13,17,18,19],
[0,23,25,19,25,16,15,11,10,9,7,0,12,6,18,17,16],
[0,23,25,23,26,20,19,15,12,13,15,12,0,6,18,17,16],
[0,29,27,17,23,14,13,9,16,15,13,6,6,0,12,11,10],
[0,25,27,29,27,26,25,21,14,15,17,18,18,12,0,1,2],
[0,26,28,28,28,25,24,20,15,16,18,17,17,11,1,0,1],
[0,27,29,27,29,24,23,19,16,17,19,16,16,10,2,1,0] ]
w=[0,[0,0,5,8,4,3,2],
   [0,5,0,4,2,1,3],
   [0,8,4,0,7,5,4],
   [0,4,2,7,0,9,8],
   [0,3,1,5,9,0,4],
   [0,2,3,4,8,4,0]]
g=Graphe(w1)
g.glouton(16)
tps2 = time.clock()
print "temps d'execution"
print(tps2 - tps1)
