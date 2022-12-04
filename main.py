LEN_OF_THE_WORD = 5
ACTUAL_WORD = "eagle"

AMOUNTS_OF_ALLOWED_GUESSES = 6

def mark_box_green(currrent_round_number, ind):
    print(ind+1, "green")
def mark_box_yellow(current_round_number, ind):
    print(ind+1, "yellow")

def show_result(found=False):
    if found == True:
        print("congratulations")

found = False 
for current_round_number in range(AMOUNTS_OF_ALLOWED_GUESSES):
    actual_word2 = []
    actual_word2 = list(ACTUAL_WORD)
    
    guessed_word = input("Please enter your guessed_word: ")
    if guessed_word == ACTUAL_WORD:
        show_result(found=True)
        break
    else:
        for ind, letter in enumerate(guessed_word):
            if letter in actual_word2:
                if ind == ACTUAL_WORD.index(letter):
                    mark_box_green(current_round_number, ind)
                else:
                    mark_box_yellow(current_round_number, ind)
                actual_word2.remove(letter)
                
show_result(found=False)