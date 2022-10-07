from random import randint

vies_joueur, victoires, defaites, jouer = 20, 0, 0, True

def restart():
    vies_joueur, victoires, defaites = 20, 0, 0


def creer_monstre():
    print("")



def fight():
    fight=True
    while fight:
        global vies_joueur, victoires, defaites, jouer
        vies_monstre = randint(1, 5)
        combattre = int(input(f"Un monstre apparait avec {vies_monstre} vies. Que voulez vous faire. \n\n1-Attaquer\n\n2-Contourner"))
        if combattre == 1:
            dees = randint(1, 6)
            if dees > vies_monstre:
                vies_joueur, victoires, rejouer = vies_joueur + vies_monstre, victoires+1, int(input("Voulez vous rejouer?\n\n1-Rejouer\n\n2-Arreter"))
            else:
                vies_joueur, defaites, rejouer = vies_joueur - vies_monstre, defaites+1, int(input("Voulez vous rejouer?\n\n1-Rejouer\n\n2-Arreter"))
                if vies_joueur<=0:
                    fight=False

        else:
            vies_joueur -= 1
            if vies_joueur<=0:
                fight=False

while jouer:
    restart()
    creer_monstre()
    fight()