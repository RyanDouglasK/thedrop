import random



i = 'yes'

while i == 'yes':
    rolls = []
    print('\n\nEnter your roll. "number of dice"d"number of sides" ')
    roll = raw_input('eg. to roll three, six sided dice you would enter 3d6 --> ')
    roll_list = roll.split("d")

    for i in range(1,int(roll_list[0]) + 1):
        
        dice_sides = int(roll_list[1])
        rolls.append(random.randint(1, dice_sides))
        total = sum(rolls)
    print('\n')
    print('-' * 30 )    
    print('Total:{} rolls: {} ').format(total, rolls)
    print('-' * 30 )
    print('\n\n')

    i = raw_input('\nWould you like to roll again? \n Enter "yes" or "no" --> ')
    


