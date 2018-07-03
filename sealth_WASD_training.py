
import random
import msvcrt

one_ascii = "1"
two_ascii = "2"
three_ascii = "3"
four_ascii = "4"
five_ascii = "5"
q_ascii = "q"
w_ascii = "w"
w2_ascii = "w"
e_ascii = "e"
r_ascii = "r"
a_ascii = "a"
a2_ascii = "a"
s_ascii = "s"
s2_ascii = "s"
d_ascii = "d"
d2_ascii = "d"
f_ascii = "f"
z_ascii = "z"
x_ascii = "x"
c_ascii = "c"
v_ascii = "v"
space_ascii = " "
space2_ascii = " " 
shift_ascii = "S"
ctrl_ascii = "c"
tab_ascii = "   "

key_list = [one_ascii, two_ascii, three_ascii,four_ascii, five_ascii, q_ascii, w_ascii, w2_ascii, e_ascii, r_ascii, a_ascii, a2_ascii, s_ascii, s2_ascii, d_ascii, d2_ascii, f_ascii, z_ascii, x_ascii, c_ascii, v_ascii, space_ascii, space2_ascii, shift_ascii, ctrl_ascii, tab_ascii]
what_was_typed = 0 
number_correct = 0
total_number = 0
score_count = 0

while what_was_typed != "p":
    n = random.randint(0, len(key_list) - 1)
    print('\n\n')
    print(key_list[n])
    what_was_typed = msvcrt.getche()
    
    if key_list[n][0] == what_was_typed:
        number_correct = number_correct + 1
        print("\n Correct")
    else: 
        print("\n Wrong")
    
    total_number = total_number + 1
    score_count = score_count + 1

    if score_count >= 10:
        percent_right = float(number_correct) / float(total_number)

        print('You got {} right out of {}. That is {} correct!').format(number_correct, total_number, percent_right)

        score_count = 0
percent_right = float(number_correct) / float(total_number)

print('Thanks for playing your final score was {} correct out of {} that is {} correct!').format(number_correct, total_number, percent_right)
