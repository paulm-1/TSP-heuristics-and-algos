import time,sys
from random import *
from math import *
class Graphe:
    def __init__(self,graphe):
        self.graphe =graphe
    def arcExist(self,i,j):
        if self.graphe[i][j]!=None:
            return True
        return False
    def longueur(self,seq):
        return len(seq)
    def distance(self,seq):
        cout=0
        if self.longueur(seq)>1:
            for i in range(self.longueur(seq)-1):
                if self.arcExist(seq[i],seq[i+1]):
                    cout+=self.graphe[seq[i]][seq[i+1]]
        return cout

    def arcParcour(self, a,b,p):
        c=p.index(a)
        d=p.index(b)
        #makhassch a tkon lass9a f b donc makhassch ykon lindex dyalhom lass9 x-1 x et x x+1
        if fabs(c-d)==1:
            return True # lass9ine
        else:
            return False

    def petit_three(self, parcours):
        print 'parcours initial'
        print parcours
        print 'cout parcours initial'
        print self.distance(parcours)
        p=[]
        for i in parcours:
            p.append(i) # {1,2,3,4,5,6}
        cout_init = self.distance(parcours)
        while (len(p)>0):#tant que non vide
            x=choice(p)# choix random dyla chi l3ba exemple 2
            p.remove(x) #suprresion de la liste p {1,3,4,5,6}
            noeuds_ncident = []
            for i in parcours:
                if self.arcParcour(x,i,parcours):
                    noeuds_ncident.append(i)# noeuds lass9ine f X jbdnahom    
            non_adja=[]       
            for i in parcours:
                if i not in noeuds_ncident and i != x:
                    non_adja.append(i)  # o 7tinahom f had la liste  {4 5 6} 
            y=choice(non_adja) # wa7d au hasard mnhadok ngolo 7na 5
            
            
            ind_y=parcours.index(y) # index dyal 5 hwa 4
            e=ind_y+1 # e katwli hya 5
            parcours.remove(x) # nkhwiw hadak li tkhtar f lawal
            parcours[e:e] = [x] # 1,3,4,5,2,6  wnkhchiwh apres lindex dyal 5 li hwa 4+1 (e)
           
            
        if self.distance(parcours) < cout_init: # salinaaa
            print("parcours final")
            print parcours
            print 'cout parcours final'
            print self.distance(parcours)
        else:
            self.petit_three(parcours)





        
tps1 = time.clock() 
y=[0,[0,0,2,12,6,15,16,20,13,14,16,23,23,29,25,26,27],
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


g=Graphe(y)
g.petit_three([5, 6, 7, 13, 11, 12, 10, 9, 8, 3, 16, 15, 14, 2, 1, 4])
tps2 = time.clock()
print "temps d'execution"
print(tps2 - tps1)

