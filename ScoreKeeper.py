scores = {}
players = []
i = 'yes'

print('\n \n')
while i == 'yes':

    players.append(raw_input("Enter players name. --> "))
    i = raw_input('\n Would you like to add another player? \n Enter "yes" or "no" --> ')

for i in players:
    #print("Enter {}'s score.--> ").format(i)
    scores[i] = int(raw_input("\n Enter {}'s score.--> ".format(i)))

print('\n \n The players scores are: \n ----------------------- \n')

for i in scores.keys():
    print("{}'s score is {}").format(i, scores[i])

print('\n \n')
