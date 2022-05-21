import random
import time

def nombre(n,mise):
    win = 0
    loss = 0
    argent = n * mise
    print("mise de depart : ",argent)
    A_match_nul = 1
    B_equipe_fav = 2
    C_outsider_pas_fav = 3
    cote_fav = 0
    cote_pas_fav = 0
    for i in range(0,n):
        cote_fav = random.randrange(1,2)
        cote_pas_fav = random.randrange(3,15)
        resultat = random.randrange(1,4)
        if resultat == A_match_nul:
            argent += cote_fav * mise
            win += 1
        elif resultat == B_equipe_fav:
            argent += cote_fav * mise
            win += 1
        elif resultat == C_outsider_pas_fav:
            argent -= mise
            loss += 1
    print("win : ",win,"\nloss : ",loss)
    print("argent gagné : ",argent,"\n---------------------------------------------")
while True:
    time.sleep(1)
    nombre(10, 1)