## This program was made just to test the results and how many rounds the game takes as well as card shifting behaviours. It is wholly automated and user has no role in the game. Everything is rule based.
## Game Logic - 13 players get 4 card each from a deck of 52 cards + 2 jokers. the cards are represented by (number,colour) numbers from 1 to 13 as for A to K and colours r and b for red and black. there is no difference between clubs and spades or hearts or diamonds in this game. Players pass one of their cards, which is least useful to them to the next player, and recieve one card from the previous player, all do the same, simultaneously (irl). Aim of the game is to get a set of consecutive numbers in same colour that can be like 4,5,6,7 in red or like 12,13,1,2 in black. Jokers represented by (99,'j') are totally useless. One player can't see the card of any other player. 
## All you have to do is press enter and watch all the 13 players play (all computer haha you can bet on which one will win after seeing their cards on first round maybe). The cards will be distributed automatically, and the players will discard their and accept one from their previous player on their own according to the best possible solution to get their own victories.
totalset = [(1, 'b'), (2, 'b'), (3, 'b'), (4, 'b'), (5, 'b'), (6, 'b'), (7, 'b'), (8, 'b'), (9, 'b'), (10, 'b'), (11, 'b'), (12, 'b'), (13, 'b'), (1, 'b'), (2, 'b'), (3, 'b'), (4, 'b'), (5, 'b'), (6, 'b'), (7, 'b'), (8, 'b'), (9, 'b'), (10, 'b'), (11, 'b'), (12, 'b'), (13, 'b'), (1, 'r'), (2, 'r'), (3, 'r'), (4, 'r'), (5, 'r'), (6, 'r'), (7, 'r'), (8, 'r'), (9, 'r'), (10, 'r'), (11, 'r'), (12, 'r'), (13, 'r'), (1, 'r'), (2, 'r'), (3, 'r'), (4, 'r'), (5, 'r'), (6, 'r'), (7, 'r'), (8, 'r'), (9, 'r'), (10, 'r'), (11, 'r'), (12, 'r'), (13, 'r'),(99, 'j'),(99, 'j')] #the total deck of cards with jokers

from itertools import combinations
import random

def remove_worst_card(card_set, discard):  # updated for color logic
    for i, card in enumerate(card_set):
        if card == (99, 'j'):
            discard.append(card)
            return [card_set[j] for j in range(4) if j != i], discard
        
    def normalize(nums):
        normalized_sets = []
        for offset in range(13):
            shifted = sorted([(n - offset) % 13 for n in nums])
            max_gap = max(shifted[i+1] - shifted[i] for i in range(len(shifted)-1))
            normalized_sets.append((max_gap, shifted, offset))
        normalized_sets.sort()
        return normalized_sets[0]

    best_score = (float('inf'), float('inf'))  # (gap_score, color_mismatch)
    best_combo = None

    for combo_indices in combinations(range(4), 3):
        selected = [card_set[i] for i in combo_indices]
        nums = [card[0] for card in selected]
        colors = [card[1] for card in selected]
        if len(set(nums)) < 3:  # skip if duplicate numbers
            continue
        norm = normalize(nums)
        color_mismatch = len(set(colors))
        score = (norm[0], color_mismatch)  # prioritize number closeness, then color match
        if score < best_score:
            best_score = score
            best_combo = combo_indices

    if best_combo is None:  # fallback
        seen = set()
        for i, card in enumerate(card_set):
            if card[0] in seen:
                discard.append(card_set[i])
                return [card_set[j] for j in range(4) if j != i], discard
            seen.add(card[0])
        discard.append(card_set[3])
        return card_set[:3], discard

    worst_index = list(set(range(4)) - set(best_combo))[0]
    discard.append(card_set[worst_index])
    return [card_set[i] for i in range(4) if i != worst_index], discard


def is_consecutive_four(cards):
    if len(cards) != 4:
        return False

    nums = [c[0] for c in cards]
    colors = [c[1] for c in cards]

    # ✅ All cards must be of same color
    if len(set(colors)) != 1:
        return False

    # 🌀 Try all 13 starting points to handle circular wrap-around
    nums_mod = [n % 13 for n in nums]
    nums_mod = sorted(set(nums_mod))  # remove duplicates and sort
    if len(nums_mod) != 4:
        return False

    for start in range(13):
        target = [(start + i) % 13 for i in range(4)]
        if sorted(nums_mod) == sorted(target):
            return True
    return False

p1set,p2set,p3set,p4set,p5set,p6set,p7set,p8set,p9set,p10set,p11set,p12set,p13set = [],[],[],[],[],[],[],[],[],[],[],[],[] # sets of cards for each player
p1dis,p2dis,p3dis,p4dis,p5dis,p6dis,p7dis,p8dis,p9dis,p10dis,p11dis,p12dis,p13dis = [],[],[],[],[],[],[],[],[],[],[],[],[] # discarded card holders
playersset = [p1set,p2set,p3set,p4set,p5set,p6set,p7set,p8set,p9set,p10set,p11set,p12set,p13set]
playersdis = [p1dis,p2dis,p3dis,p4dis,p5dis,p6dis,p7dis,p8dis,p9dis,p10dis,p11dis,p12dis,p13dis]

for n in range(0,13):  # this loop distibutes the cards randomly, it works totally fine so do not touch it
    for i in range(0,4):
        a = random.randint(0,len(totalset)-1)
        playersset[n].append(totalset.pop(a))
print(f"\n deck (with jokers) has been distributed into 13 players, 4 each and the two cards that remain are {totalset}.")
input("Press any key to begin the automated game.\n")
gameround = 0

while True:
    gameround += 1
    print(f"\nROUND {gameround}\n")

    # 🧠 Step 1: If not round 1, collect the discarded card from previous round
    if gameround != 1:
        for i in range(13):
            j = 12 if i == 0 else i - 1
            if playersdis[j]:
                playersset[i].append(playersdis[j][-1])  # copy, not pop yet

    # ✅ Check for winning condition
    for i in range(13):
        if (99, 'j') in playersset[i]:
            continue  # skip win check if joker is present
        if is_consecutive_four(playersset[i]):
            values = [card[0] for card in playersset[i]]
            color = playersset[i][0][1]
            print(f"✅ Player {i+1} has made a 4-card straight of same color '{color}': {sorted(values)}")


    # 🗑️ Step 2: Now remove worst cards and record discards for this round
    new_discards = []  # temporary discard list
    for i in range(13):
        print(f"player {i+1} has {playersset[i]}")
        playersset[i], temp_discard = remove_worst_card(playersset[i], [])
        new_discards.append(temp_discard[0])  # exactly one discarded

    # 🔄 Step 3: Update actual playersdis now
    for i in range(13):
        playersdis[i].append(new_discards[i])

    input("\nPress Enter")
