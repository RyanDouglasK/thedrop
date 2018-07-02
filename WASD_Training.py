
import random

key_list = {'1':one_ascii,}
what_was_typed = 0 
number_correct = 0
total_number = 0
score_count = 0


while what_was_typed != "p":
    n = random.randint(0, 27)
    print(key_list[n])
    what_was_typed = raw_input('----> ')
    
    if key_list.keys(n) == what_was_typed:
        number_correct = number_correct + 1
        print('You got it right!!')
    else: 
        print('You got it wrong...')
    
    total_number = total_number = 1
    score_count = score_count + 1

    if score_count >= 10:
        percent_right_decimal = number_correct / total_number 
        percent_right = percent_right_decimal * 100

        print('You have gotten {} right out of {}. That is a {}%').format(number_correct, total_number, percent_right)

        score_count = 0

print('Thanks for playing your final score was {} correct out of {} that is a {}%.').format(number_correct, total_number, percent_right)


one_ascii
two
three
four
five
