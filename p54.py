__author__ = "Janna Timmer"

file = open("p054_poker.txt")
file_str = file.read()
hands = file_str.splitlines()

#converts T J Q K A to 10, 11, 12, 13, 14
def convert_hand(hand):
	for i in range(5):
		if hand[i][0] == 'T':
			hand[i] = "10" + hand[i][1]
		elif hand[i][0] == 'J':
			hand[i] = "11" + hand[i][1]
		elif hand[i][0] == 'Q':
			hand[i] = "12" + hand[i][1]
		elif hand[i][0] == 'K':
			hand[i] = "13" + hand[i][1]
		elif hand[i][0] == 'A':
			hand[i] = "14" + hand[i][1]
	
			
def rank_hand(hand):
	numbers = []
	suits = []
	ranking = 0
	
	convert_hand(hand)
	
	#create list of card numbers and list of card suits
	for i in range(5):
		if len(hand[i]) > 2:
			numbers.append(int(hand[i][0:2]))
			suits.append(hand[i][2])
		else: 
			numbers.append(int(hand[i][0]))
			suits.append(hand[i][1])
			
	numbers = sorted(numbers)
	suits = sorted(suits)
	
	#highest number of a kind
	two = 0
	twos1 = 0
	twos2 = 0
	three = 0
	four = 0
	
	#find pairings and rearrange cards accordingly
	for num in numbers:
		if numbers.count(num) == 4:
			four += 1
			fours = num
			for rem in range(4): #place 4 of a kinds at end of list
				numbers.remove(num)
				numbers.append(num)
		if numbers.count(num) == 3:
			three += 1
			threes = num
			for rem in range(3): #place 3 of a kinds at end of list
				numbers.remove(num)
				numbers.append(num)
				
	for num in numbers:
		if numbers.count(num) == 2:
			if twos1 > 0 and twos1 != num:
				twos2 = num
				two += 1
				if three == 0: #if not full house
					for rem in range(2): #place pairs at end of list
						numbers.remove(num)
						numbers.append(num)
			elif twos1 == 0:
				twos1 = num
				two += 1
				if three == 0: #if not full house
					for rem in range(2): #place pairs at end of list
						numbers.remove(num)
						numbers.append(num)
		
	check_straight = min(numbers)
	is_straight = check_straight + 1 in numbers and check_straight + 2 in numbers and check_straight + 3 in numbers and check_straight + 4 in numbers
	
	#rankings
	if suits.count(suits[0]) == 5: #if hand is a flush
		if numbers[0] == 10 and numbers[1] == 11 and numbers[2] == 12 and numbers[3] == 13 and numbers[4] == 14:
			ranking = 10 #10 royal flush
			return [ranking, numbers]
		elif is_straight:
			ranking = 9 #9 straight flush
			return [ranking, numbers]
		else:
			ranking = 6 #6 flush
			result = [numbers[4]]
	elif is_straight:
		ranking = 5 #5 straight
	elif three > 0:
		ranking = 4 #4 three of a kind
	elif two > 1:
		ranking = 3 #3 two pairs
	elif two > 0:
		ranking = 2 #2 one pair
	
	#put as "if" to override regular flush
	if three > 0 and two > 0:
		ranking = 7 #7 full house
	if four > 0:
		ranking = 8 #8 four of a kind
		
	# print [ranking, numbers]
	return [ranking, numbers] #rank and cards ordered by importance
	
#end of method
	
	

p1_wins = 0
rank_names = ["High Card?", "", "One Pair", "Two Pairs", "Three of a Kind", "Straight", "Flush", "Full House", "Four of a Kind", "Straight Flush", "Royal Flush"]

for hand in hands:
	player1 = []
	player2 = []
	cards_line = hand.split(" ")
	for i in range(10):
		if i < 5:
			player1.append(cards_line[i])
		else:
			player2.append(cards_line[i])
		
	p1 = rank_hand(player1)
	p2 = rank_hand(player2)
	
	p1_high = p1[1] 
	p2_high = p2[1] #result
		
	p1_is_winner = False
	if p1[0] > p2[0]: #if p1 has higher ranking
		p1_is_winner = True
	elif p1[0] == p2[0]: #if p1 and p2 have same ranking
		for check in range(len(p1_high) - 1, -1, -1): #compare cards
			if check >= len(p2_high):
				break
			if p1_high[check] > p2_high[check]:
				p1_is_winner = True
			elif p1_high[check] < p2_high[check]:
				break
			
	if p1_is_winner:
		p1_wins += 1

print p1_wins