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

def wordle():
    gw = WordleGWindow()
    i = 0
    for i, letter in enumerate(Solution):
        gw.set_square_letter((N_ROWS - N_ROWS), (N_COLS - (N_COLS - i)), Solution[i])
        i += 1

    def enter_action(s):
        i = 0
        
        current_row = gw.get_current_row()
        typed_word = "".join([gw.get_square_letter(current_row, i) for i in range(N_COLS)])

        # Initialize lists to keep track of correctly guessed letters and their positions
        correct_letters = []
        correct_positions = []
        guessed_words = []
        correct_position = 0
        correct_letter = 0
        # Check each letter in the typed word against the random word
        
        for i in range(N_COLS):
            typed_letter = typed_word[i]
            random_letter = Solution[i]
            if typed_letter == random_letter:
                correct_position += 1
                # Letter is correct and in the correct position
                correct_letters.append(typed_letter)
                correct_positions.append(i)
            elif typed_letter in Solution and typed_word.count(typed_letter) <= Solution.count(typed_letter):
                correct_letter += 1
                # Letter is correct but in the wrong position
                correct_letters.append(typed_letter)
        
        # # Color the boxes based on correctness
        # for i in range(N_COLS):
        #     if i in correct_positions:
        #         window.set_square_color(0, i, CORRECT_COLOR)
        #     elif typed_word[i] in correct_letters:
        #         window.set_square_color(0, i, PRESENT_COLOR)
        #     else:
        #         window.set_square_color(0, i, MISSING_COLOR)
        
        # Check if the player has correctly guessed all five letters
        if typed_word == Solution:
            gw.show_message("Congratulations! You guessed the word correctly!")
        else:
            # Check if the typed word is a legitimate English word
            if typed_word.lower() in FIVE_LETTER_WORDS:
                gw.show_message(str(correct_position) + " correct position " + '\n' + str(correct_letter) + " in word.")
                # Move to the next row
                guessed_words.append(typed_word)
                current_row = gw.get_current_row()
                
                if current_row < N_ROWS - 1:
                    gw.set_current_row(current_row + 1)
            elif len(typed_word) != 4:
                gw.show_message("Not enough letters")
                gw.set_current_row(current_row)
            else:
                gw.show_message("Not in word list")
                gw.set_current_row(current_row)
            
        if current_row == N_ROWS - 1:
            gw.show_message("Game over! The word was " + Solution)
            gw.exit_on_close()


    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()

