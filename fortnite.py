import random

location_list = ['Anarchy Acres','Dusty Divot','Fatal Fields','Flush Factory','Greasy Grove','Haunted Hills','Junk Junction','Lonely Lodge','Loot Lake','Lucky Landing','Moisty Mire','Pleasant Park','Retail Row','Risky Reels','Salty Springs','Shifty Shafts','Snobby Shores','Tilted Towers','Tomato Town','Wailing Woods']
i = '0'
while i != 'q':
    print('Do you need a "drop" location? ')
    n = random.randint(0, len(key_list) - 1)
    print('\n\n')
    print(key_list[n])