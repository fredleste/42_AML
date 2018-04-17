#!/sgoinfre/goinfre/Perso/42-ai/anaconda3/bin/python

import math
import random

gain = 0

mise = input("Faites vos jeux...$\n")
mise = int(mise)
jeu = input("Rien ne va plus...0 à 49\n")
jeu = int(jeu)
input("...")
if jeu % 2 == 0:
	col_jeu = 'Noir'
else:
	col_jeu = 'Rouge'
res = random.randrange(50)
res = int(res)
if res % 2 == 0:
	col_res = 'Noir'
else:
	col_res = 'Rouge'
print("Le", res, col_res, "gagne")
if col_res == col_jeu:
	gain = math.ceil(mise / 2)
elif res == jeu:
	gain = gain + 3 * mise
mise = 0
if gain > 0:
	print("Vous gagnez", gain, "$")
else:
	print("Vous perdez")
