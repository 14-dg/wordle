import pygame as pg
#*pygame init
pg.init()
window_width, window_height = 800, 600
window = pg.display.set_mode((window_width, window_height))
pg.display.set_caption("Wordle for free")

#*colors
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

window.fill(WHITE)

LEN_OF_THE_WORD = 5
ACTUAL_WORD = "eagle"

AMOUNTS_OF_ALLOWED_GUESSES = 6

def draw_gamefield():
    x_len, y_len = int(window_width/LEN_OF_THE_WORD), int(window_height/AMOUNTS_OF_ALLOWED_GUESSES)
    for x_row in range(int(LEN_OF_THE_WORD/x_len)):
        for y_row in range(int(AMOUNTS_OF_ALLOWED_GUESSES/y_len)):
            pg.draw.rect(window, GRAY, (x_row*x_len, y_row*y_len, x_len, y_len))

def draw_box_green(currrent_round_number, ind):
    print(ind+1, "green")
def draw_box_yellow(current_round_number, ind):
    print(ind+1, "yellow")

def show_result(found=False):
    if found == True:
        print("congratulations")
        
draw_gamefield()
pg.display.flip()

found = False 
for current_round_number in range(AMOUNTS_OF_ALLOWED_GUESSES):
    actual_word2 = []
    actual_word2 = list(ACTUAL_WORD)
    
    guessed_word = input("Please enter your guessed_word: ")
    assert len(list(guessed_word)) == LEN_OF_THE_WORD
    if guessed_word == ACTUAL_WORD:
        show_result(found=True)
        break
    else:
        for ind, letter in enumerate(guessed_word):
            if letter in actual_word2:
                if ind == ACTUAL_WORD.index(letter):
                    draw_box_green(current_round_number, ind)
                else:
                    draw_box_yellow(current_round_number, ind)
                actual_word2.remove(letter)
                
show_result(found=False)