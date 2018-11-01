# setup
numPlayers = 4

# Number of establishments in supply
# Note that major establishments are not tracked in supply, because there will always be enough for all players
WF = 6  # Wheat Field
R = 6  # Ranch
B = 6  # Bakery
C = 6  # Cafe
CS = 6  # Convenience Store
F = 6  # Forest
CF = 6  # Cheese Factory
FF = 6  # Furniture Factory
M = 6  # Mine
FR = 6  # Family Restaurant
AO = 6  # Apple Orchard
FV = 6  # Fruit and Vegetable Market

# Cost to buy an establishment
WFCost = 1
RCost = 1
BCost = 1
CCost = 2
CSCost = 2
FCost = 3
SCost = 6  # Stadium
TVCost = 7  # TV Station
BCCost = 8  # Business Center
CFCost = 5
FFCost = 3
MCost = 6
FRCost = 3
AOCost = 3
FVCost = 2

# Establishments/Landmarks/Money owned by player 1
player1 = {
	"WF": 1,
	"R": 1,
	"B": 0,
	"C": 0,
	"CS": 0,
	"F": 0,
	"S": 0,
	"TV": 0,
	"BC": 0,
	"CF": 0,
	"FF": 0,
	"M": 0,
	"FR": 0,
	"AO": 0,
	"FV": 0,
	"AP": 0, # Amusement Park
	"TS": 0, # Train Station
	"SM": 0, # Shopping Mall
	"RT": 0, # Radio Tower
	"Money": 3
}

# Establishments owned by player 2
player2 = {
	"WF": 1,
	"R": 1,
	"B": 0,
	"C": 0,
	"CS": 0,
	"F": 0,
	"S": 0,
	"TV": 0,
	"BC": 0,
	"CF": 0,
	"FF": 0,
	"M": 0,
	"FR": 0,
	"AO": 0,
	"FV": 0,
	"AP": 0,
	"TS": 0,
	"SM": 0,
	"RT": 0,
	"Money": 3
}

# Establishments owned by player 3
player3 = {
	"WF": 1,
	"R": 1,
	"B": 0,
	"C": 0,
	"CS": 0,
	"F": 0,
	"S": 0,
	"TV": 0,
	"BC": 0,
	"CF": 0,
	"FF": 0,
	"M": 0,
	"FR": 0,
	"AO": 0,
	"FV": 0,
	"AP": 0,
	"TS": 0,
	"SM": 0,
	"RT": 0,
	"Money": 3
}

# Establishments owned by player 4
player4 = {
	"WF": 1,
	"R": 1,
	"B": 0,
	"C": 0,
	"CS": 0,
	"F": 0,
	"S": 0,
	"TV": 0,
	"BC": 0,
	"CF": 0,
	"FF": 0,
	"M": 0,
	"FR": 0,
	"AO": 0,
	"FV": 0,
	"AP": 0,
	"TS": 0,
	"SM": 0,
	"RT": 0,
	"Money": 3
}

#list containing players
players = [player1, player2, player3, player4]

#Expected delta of money from rolling 1d6
def d1Delta(player:int) -> float:
	if player == 1:
		thisplayer = players[0]
		otherplayer1 = players[1]
		otherplayer2 = players[2]
		otherplayer3 = players[3]
	elif player == 2:
		otherplayer1 = players[0]
		thisplayer = players[1]
		otherplayer2 = players[2]
		otherplayer3 = players[3]
	elif player == 3:
		otherplayer1 = players[0]
		otherplayer2 = players[1]
		thisplayer = players[2]
		otherplayer3 = players[3]
	else:
		otherplayer1 = players[0]
		otherplayer2 = players[1]
		otherplayer3 = players[2]
		thisplayer = players[3]

	otherplayers = [otherplayer1, otherplayer2, otherplayer3]

	roll1 = thisplayer["WF"]
	roll2 = thisplayer["R"] + thisplayer["B"]
	roll3 = thisplayer["B"]
	for x in range(numPlayers-1):
		roll3 = roll3 - otherplayers[x]["C"]
	roll4 = thisplayer["CS"] * 3
	roll5 = thisplayer["F"]
	roll6 = thisplayer["S"] * 2 * (numPlayers - 1) + thisplayer["TV"]*5 #TODO Business Center
	return (roll1 + roll2 + roll3 + roll4 + roll5 + roll6) / 6

#Expected delta of money from someone else rolling 1d6
def otherd1Delta(rollingPlayer:int, player:int) -> float:
	thisplayer = players[player - 1]
	otherPlayer = players[rollingPlayer - 1]
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
		thisplayer = players[0]
		otherplayer1 = players[1]
		otherplayer2 = players[2]
		otherplayer3 = players[3]
	elif player == 2:
		otherplayer1 = players[0]
		thisplayer = players[1]
		otherplayer2 = players[2]
		otherplayer3 = players[3]
	elif player == 3:
		otherplayer1 = players[0]
		otherplayer2 = players[1]
		thisplayer = players[2]
		otherplayer3 = players[3]
	else:
		otherplayer1 = players[0]
		otherplayer2 = players[1]
		otherplayer3 = players[2]
		thisplayer = players[3]

#Expected delta of money of everyone else from someone else rolling 1d6
def otherd1OtherDelta(player:int) -> float:
	pass

def playerScore(player:int) -> float:
	thisPlayer = players[player - 1]
	establishments = thisPlayer["AP"] + thisPlayer["TS"] + thisPlayer["SM"] + thisPlayer["RT"]
	score = establishments * 1000
	score = incomePerTurn(player) * 100
	score += thisPlayer["Money"]

def incomePerTurn(player:int) -> int:
	pass

