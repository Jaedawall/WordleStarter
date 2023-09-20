# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random


from pandas import concat

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

Solution = random.choice(FIVE_LETTER_WORDS).upper()
global correct_positions_dict
correct_positions_dict = {0: '', 1: '', 2: '', 3: '', 4: ''}
global correct_letters_list
correct_letters_list = []
def wordle():
    gw = WordleGWindow()
    i = 0
    for i, letter in enumerate(Solution):
        gw.set_square_letter((N_ROWS - N_ROWS), (N_COLS - (N_COLS - i)), Solution[i])
        i += 1
    # correct_positions_dict = {0: '', 1: '', 2: '', 3: '', 4: ''}
    # correct_letters_list = []
    hard_mode = True
    def enter_action(s):
        i = 0
        g = 0
        current_row = gw.get_current_row()
        typed_word = "".join([gw.get_square_letter(current_row, i) for i in range(N_COLS)])
                

        # Initialize lists to keep track of correctly guessed letters and their positions
        correct_positions = []
        unused_letter = []
        # Check each letter in the typed word against the random word
        if typed_word == Solution:
            gw.show_message("Congratulations! You guessed the word correctly!")
        else:
            # Check if the typed word is a legitimate English word
            if typed_word.lower() in FIVE_LETTER_WORDS:
                g = 0
                current_row = gw.get_current_row()
                if hard_mode == True:
                    while g < len(correct_letters_list):
                        if correct_letters_list[g] not in typed_word:
                            unused_letter.append(correct_letters_list[g])
                            g += 1
                        else:
                            g += 1

                    if len(unused_letter) > 0:
                        gw.show_message("You have to put " + str(unused_letter) + " in word")
                        gw.set_current_row(current_row)
                        return

                    for i in range(N_COLS):
                        typed_letter = typed_word[i]
                        random_letter = Solution[i]
                        
                        if correct_positions_dict[i] != '':
                            if typed_letter != correct_positions_dict[i]:
                                gw.show_message("You have to put " + correct_positions_dict[i] + " in position " + str(i + 1))
                                gw.set_current_row(current_row)
                                return

                correct_letters_list.clear()
                i = 0
                for i in range(N_COLS):
                    typed_letter = typed_word[i]
                    random_letter = Solution[i]
                    if typed_letter == random_letter:
                        # Letter is correct and in the correct position
                        correct_positions.append(i)
                        correct_positions_dict[i] = typed_letter
                    elif typed_letter in Solution and typed_word.count(typed_letter) <= Solution.count(typed_letter):
                        # Letter is correct but in the wrong position
                        correct_letters_list.append(typed_letter)
                    

                # Move to the next row
                if current_row < N_ROWS - 1:
                    gw.set_current_row(current_row + 1)
                else:
                    gw.show_message("Game over! The word was " + Solution)
            elif len(typed_word) < 4:
                gw.show_message("Not enough letters")
                gw.set_current_row(current_row)
            else:
                gw.show_message("Not in word list")
                gw.set_current_row(current_row)
            

        
        # # Color the boxes based on correctness
        # for i in range(N_COLS):
        #     if i in correct_positions:
        #         window.set_square_color(0, i, CORRECT_COLOR)
        #     elif typed_word[i] in correct_letters:
        #         window.set_square_color(0, i, PRESENT_COLOR)
        #     else:
        #         window.set_square_color(0, i, MISSING_COLOR)
        
        # Check if the player has correctly guessed all five letters
        

    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
