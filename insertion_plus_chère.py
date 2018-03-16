import time,sys
class Graphe:
    def __init__(self,graphe):
        self.graphe =graphe
    
    def insertionMoindreCout(self,nb_sommet):
        parcours=[]
        parcours.append(1)
        parcours.append(2)
        parcours.append(3)
        parcours.append(1)
        for i in range(nb_sommet):
            i=i+1
            if i not in parcours:
                ind=None
                dist=-sys.maxint
                for j in range(len(parcours)-1):
                    if dist<self.graphe[parcours[j]][i]+self.graphe[i][parcours[j+1]]-self.graphe[parcours[j]][parcours[j+1]]:
                        dist=self.graphe[parcours[j]][i]+self.graphe[i][parcours[j+1]]-self.graphe[parcours[j]][parcours[j+1]]
                        ind=j
                p=[]
                for k in range(len(parcours)):
                    p.append(parcours[k])
                    if k==ind:
                        p.append(i)
                parcours=p
        print parcours
                        
             
        
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
g.insertionMoindreCout(16)
tps2 = time.clock()
print "temps d'execution"
print(tps2 - tps1)
