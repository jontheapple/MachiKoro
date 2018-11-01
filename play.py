import setup

#Expected delta of money from rolling 1d6
def d1Delta(player:int) -> float:
	if player == 1:
		thisplayer = setup.players[0]
		otherplayer1 = setup.players[1]
		otherplayer2 = setup.players[2]
		otherplayer3 = setup.players[3]
	elif player == 2:
		otherplayer1 = setup.players[0]
		thisplayer = setup.players[1]
		otherplayer2 = setup.players[2]
		otherplayer3 = setup.players[3]
	elif player == 3:
		otherplayer1 = setup.players[0]
		otherplayer2 = setup.players[1]
		thisplayer = setup.players[2]
		otherplayer3 = setup.players[3]
	else:
		otherplayer1 = setup.players[0]
		otherplayer2 = setup.players[1]
		otherplayer3 = setup.players[2]
		thisplayer = setup.players[3]

	otherplayers = [otherplayer1, otherplayer2, otherplayer3]

	roll1 = thisplayer["WF"]
	roll2 = thisplayer["R"] + thisplayer["B"]
	roll3 = thisplayer["B"]
	for x in range(setup.numPlayers-1):
		roll3 = roll3 - otherplayers[x]["C"]
	roll4 = thisplayer["CS"] * 3
	roll5 = thisplayer["F"]
	roll6 = thisplayer["S"] * 2 * (setup.numPlayers - 1) + thisplayer["TV"]*5 #TODO Business Center
	return (roll1 + roll2 + roll3 + roll4 + roll5 + roll6) / 6

#Expected delta of money from someone else rolling 1d6
def otherd1Delta(rollingPlayer:int, player:int) -> float:
	thisplayer = setup.players[player - 1]
	otherPlayer = setup.players[rollingPlayer - 1]
	roll1 = thisplayer["WF"]
	roll2 = thisplayer["R"]
	roll3 = thisplayer["C"]
	roll4 = 0
	roll5 = thisplayer["F"]
	roll6 = otherPlayer["S"] * 2 * -1 #TODO Business Center and TV Station
	return (roll1 + roll2 + roll3 + roll4 + roll5 + roll6) / 6

#Expected delta of money of everyone else from rolling 1d6
def d1OtherDelta(player:int) -> float:
	if player == 1:
		thisplayer = setup.players[0]
		otherplayer1 = setup.players[1]
		otherplayer2 = setup.players[2]
		otherplayer3 = setup.players[3]
	elif player == 2:
		otherplayer1 = setup.players[0]
		thisplayer = setup.players[1]
		otherplayer2 = setup.players[2]
		otherplayer3 = setup.players[3]
	elif player == 3:
		otherplayer1 = setup.players[0]
		otherplayer2 = setup.players[1]
		thisplayer = setup.players[2]
		otherplayer3 = setup.players[3]
	else:
		otherplayer1 = setup.players[0]
		otherplayer2 = setup.players[1]
		otherplayer3 = setup.players[2]
		thisplayer = setup.players[3]

#Expected delta of money of everyone else from someone else rolling 1d6
def otherd1OtherDelta(player:int) -> float:
	pass

def playerScore(player:map) -> float:
	establishments = player["AP"] + player["TS"] + player["SM"] + player["RT"]
	score = establishments * 1000
	score += deltaPerTurn(player) * 100
	score += player["Money"]
	return score

def deltaPerTurn(player:map) -> int:
	pass

# Takes player number as input, returns optimal target player number
def tvChoice(player:int) -> int:
	# The other players
	other1 = {}
	other2 = {}
	other3 = {}
	others = [other1, other2, other3]
	n = 0
	for i in range(4):
		if i == player:
			continue
		others[n] = setup.players[i]
		n+=1
	other1Establishments = other1["AP"] + other1["TS"] + other1["SM"] + other1["RT"]
	other2Establishments = other2["AP"] + other2["TS"] + other2["SM"] + other2["RT"]
	other3Establishments = other3["AP"] + other3["TS"] + other3["SM"] + other3["RT"]

	#other players with 4 establishments go in this list
	establish4 = []
	if other1Establishments == 4:
		establish4.append(other1)
	if other2Establishments == 4:
		establish4.append(other2)
	if other3Establishments == 4:
		establish4.append(other3)

