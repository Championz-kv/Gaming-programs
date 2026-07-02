import random
players = ['Shadow','looooooviii','GUTS','Hahmax','Sam0Bahadur','Shinobu','angah']  # name/id of participants
no_of_matches = 4      # the no. of matches a participant should play

duel = players*no_of_matches  # make sure at least either of no_of_matches or no. of participants in the players list should be even
tournament = []

while duel != []:
    player1 = random.choice(duel)
    duel.remove(player1)
    while True:
        player2 = random.choice(duel)
        if player2 != player1:
            if [player1,player2] not in tournament and [player2,player1] not in tournament:   ## 'do not allow repititions' (put # before 'if' to disable)(may cause code to not work sometimes when enabled- rerun the code and try again in that case.)
                break
    duel.remove(player2)
    tournament.append([player1,player2])

print(f"\n{len(tournament)} matches scheduled\n")
for i in tournament: 
    print('match',tournament.index(i)+1,' : ',i[0],"vs",i[1])
print()