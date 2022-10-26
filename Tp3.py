"""
Fait par : Jeremy Martin Groupe : 403
Ce code represente un combat entre le joueur et des monstres
"""

from random import randint

rejouer, vies_joueur, victoires, defaites, streak = True, 20, 0, 0, 0


def restart():
    """
	Cette definition reset les variables et redit la scene
	"""
    global vies_joueur, victoires, defaites, streak
    regles = input(
        "Vous etes dans une grotte de goblins. Vous essayez de survivre le plus longtemps possible en tuant des "
        "monstre qui vous attaquent. \n\n(Entrez 1 pour voir les regles)\nEntrez quelque chose d'autre pour "
        "continuer\n\n")
    if regles == "1":
        input(
            "Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  "
            "Dans ce cas, le nivea de vie de l’usager est augmenté de la force de l’adversaire. Une défaite a lieu "
            "lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce "
            "cas, le niveau de vie de l’usager est diminué de la force de l’adversaire. La partie se termine lorsque "
            "les points de vie de l’usager tombent sous 0. L’usager peut combattre ou éviter chaque adversaire, "
            "dans le cas de l’évitement, il y a une pénalité de 1 point de vie.\nEntrez quelque chose pour "
            "continuer\n\n")


def fight():
    """
	Cette definition fait le combat entre le joueur et le monstre
	"""
    global vies_joueur, victoires, defaites, rejouer, streak
    fighting = True
    while fighting:
        if streak >= 3:
            vies_monstre, boss = randint(8, 12), "ATTAQUE DU BOSS!!"
        else:
            vies_monstre, boss = randint(4, 8), ""
        combattre = int(input(
            f"Vies : {vies_joueur}\nVictoires : {victoires}\nDefaites : {defaites}\nStreak : {streak}\n\n "
            f"Monstre de {vies_monstre} vies (monstre #{victoires + defaites + 1}) : {boss}\n\n1-Attaquer\n"
            f"2-Contourner\n"
            f"3-Afficher les regles\n"
            f"4-Quitter\n\n"))

        if combattre == 1:
            dees = (randint(1, 6) + randint(1, 6))
            if dees > vies_monstre:
                vies_joueur, victoires, streak = vies_joueur + vies_monstre, victoires + 1, streak + 1
                print(f"VICTOIRE\nVous avez roulee un {dees}\n\n")
            else:
                print(f"VOUS AVEZ PERDU\nVous avez roulee un {dees}\n\n")
                vies_joueur, defaites, streak = vies_joueur - vies_monstre, defaites + 1, 0
                if vies_joueur <= 0:
                    fighting = False
                    print(f"VOUS ETES MORT\n\nStats :\nVies : 0\nVictoires : {victoires}\nDefaites : {defaites}")
                    rejouer = int(input("Voulez vous rejouer?\n\n1-Rejouer\n\n2-Arreter"))

        elif combattre == 2:
            vies_joueur -= 1
            if vies_joueur <= 0:
                fighting = False
                print(f"VOUS ETES MORT\n\nStats :\nVies : 0\nVictoires : {victoires}\nDefaites : {defaites}")
                rejouer = int(input("Voulez vous rejouer?\n\n1-Rejouer\n\n2-Arreter"))

        elif combattre == 3:
            input(
                "Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire. "
                "Dans ce cas, le nivea de vie de l’usager est augmenté de la force de l’adversaire. Une défaite a lieu "
                "lorsque la valeur du dé lancé par l’usager est "
                "inférieure ou égale à la force de l’adversaire.  Dans ce "
                "cas, le niveau de vie de l’usager est diminué de la force"
                " de l’adversaire. La partie se termine lorsque "
                "les points de vie de l’usager tombent sous 0. L’usager peut combattre ou éviter chaque adversaire, "
                "dans le cas de l’évitement, il y a une pénalité de 1 point de vie.\nEntrez quelque chose pour "
                "continuer\n\n")

        else:
            rejouer, fighting = 2, False


while rejouer != 2:
    restart()
    fight()
print("Merci et au revoir...")
