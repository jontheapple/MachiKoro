import setup

def buyWF(player:map):
	if setup.WF > 0:
		if player["Money"] > setup.WFCost:
			player["WF"] += 1
			setup.WF -= 1
		else:
			print("Not enough money")
	else:
		print("Not enough WF")

def buyR(player:map):
	if setup.R > 0:
		if player["Money"] > setup.RCost:
			player["R"] += 1
			setup.R -= 1
		else:
			print("Not enough money")
	else:
		print("Not enough R")

def buyB(player:map):
	if setup.B > 0:
		if player["Money"] > setup.BCost:
			player["B"] += 1
			setup.B -= 1
		else:
			print("Not enough money")
	else:
		print("Not enough B")

def buyC(player:map):
	if setup.C > 0:
		if player["Money"] > setup.CCost:
			player["C"] += 1
			setup.C -= 1
		else:
			print("Not enough money")
	else:
		print("Not enough C")

def buyCS(player:map):
	if setup.CS > 0:
		if player["Money"] > setup.CSCost:
			player["CS"] += 1
			setup.CS -= 1
		else:
			print("Not enough money")
	else:
		print("Not enough CS")

def buyF(player:map):
	if setup.F > 0:
		if player["Money"] > setup.FCost:
			player["F"] += 1
			setup.F -= 1
		else:
			print("Not enough money")
	else:
		print("Not enough F")

