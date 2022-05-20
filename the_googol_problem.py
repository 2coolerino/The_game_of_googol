from math import e
from math import ceil
from random import randrange

num_of_options = ((int(input("How many options would you like to have?\n"))))
#Feel free to change the power to change the range of the numbers generated.
list_of_generated_numbers = [randrange(1, 10**10) for x in range(0, num_of_options)]

chosen_num = -1
largest_num_seen = -1
print(f"The optimal sample size is {(int(ceil(num_of_options/e)))}.")
for x in range(0, num_of_options):
    print(f"Choice #{x+1}:")
    if(list_of_generated_numbers[x] > largest_num_seen):
        largest_num_seen = list_of_generated_numbers[x]
    print(f"Largest number so far {largest_num_seen:,}")
    print("{:,}".format(list_of_generated_numbers[x]))
    user_option = input("Would you like to keep this number, type y for yes, type anything else to keep going.\n")
    if(user_option == "y"):
        chosen_num = list_of_generated_numbers[x]
        break
del largest_num_seen

if (chosen_num == -1):
    print("You did not stick with a number, defaulting to the last choice.")
    chosen_num = list_of_generated_numbers[len(list_of_generated_numbers)-1]

print(f"Your chosen number was: {chosen_num:,}")
max_num_in_list = max(list_of_generated_numbers)
print(f"The largest number in the list was {max_num_in_list:,} at position {list_of_generated_numbers.index(max_num_in_list)+1}")
print("This was the full list of the numbers:")
print(['{:,}'.format(x) for x in list_of_generated_numbers])
if(chosen_num == max_num_in_list):
    print("Good job, you got pretty lucky!")
else:
    print("You didn't get the largest number, better luck next time.")