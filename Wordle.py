# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
from tkinter import *
from tkinter import Label
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS
from WordleGraphics import (
    CORRECT_COLOR_DEFAULT, PRESENT_COLOR_DEFAULT, MISSING_COLOR_DEFAULT,
    CORRECT_COLOR_ALT, PRESENT_COLOR_ALT, MISSING_COLOR_ALT
)

# Opens playing window
gw = WordleGWindow()

#Create toggle button
def hard_mode_toggle_button():
    
    # Add Title
    gw._root.title('On/Off Switch!')
    # # Add Geometry
    # gw._root.geometry("300x200")
    global is_on
    is_on = False
    global hard_mode
    hard_mode = False
    # Create Label
    hard_mode_label = Label(gw._root,
        text = "Hard mode Is Off!",
        fg = "grey",
        font = ("Helvetica", 12))
    
    hard_mode_label.pack(side="right", pady=10, anchor="e")
    
    # Define our switch function
    def switch():
        global hard_mode
        global is_on
        # Determine is on or off
        if is_on:
            hard_mode_button.config(image = off)
            hard_mode_label.config(text = "Hard mode is Off",
                            fg = "grey")
            is_on = False
            hard_mode = False
        else:
            hard_mode_button.config(image = on)
            hard_mode_label.config(text = "Hard mode is On", fg = "green")
            is_on = True
            hard_mode = True
    
    # Define Our Images
    on = PhotoImage(file = "on.png")
    off = PhotoImage(file = "off.png")
    
    # Create A Button
    hard_mode_button = Button(gw._root, image = off, bd = 0,
                    command = switch)
    hard_mode_button.pack(side="right", pady=10, anchor="e")
    
def color_toggle_button():
    
    # Add Title
    gw._root.title('On/Off Switch!')
    
    # Keep track of the button state on/off
    global default
    default = True
    
    # Create Label
    my_label = Label(gw._root,
        text = "Default Color Scheme!",
        fg = "grey",
        font = ("Helvetica", 12))
    
    my_label.pack(side="left", padx= 5)
    
    # Define our switch function
    def switch():
        global default
        
        # Determine is on or off
        if default:
            color_button.config(image = on)
            my_label.config(text = "Alternative Color Scheme",
                            fg = "green")
            default = False
        else:
        
            color_button.config(image = off)
            my_label.config(text = "Default Color Scheme", fg = "grey")
            default = True
    
    # Define Our Images
    on = PhotoImage(file = "on.png")
    off = PhotoImage(file = "off.png")
    
    # Create A Button
    color_button = Button(gw._root, image = off, bd = 0,
                    command = switch)
    color_button.pack(side="left", padx=5)

# Default color scheme
current_color_scheme = "default"  # Initial color scheme
# Sets the solution word
Solution = random.choice(FIVE_LETTER_WORDS).upper()
# Just shows the solution in the terminal
if __name__ == "__main__":
    print("Solution:", Solution)  # Print the value of the Solution variable

# Function to toggle between Color Schemes
# def toggle_color_scheme():
#     global default

#     if current_color_scheme == "default":
#         current_color_scheme = "alternate"
#     else:
#         current_color_scheme = "default"

# Displays the color scheme instruction messeage
def display_instruction_message():
    instruction_message = "Press the '1' key at the start of the game to change your color scheme. \n Blue: correct position(s), Pink: present letter(s), Tan: missing letter(s)"
    instruction_label = Label(
        gw._root, text=instruction_message, font=("Helvetica Neue", -14))
    instruction_label.pack(side="top", pady=10)

global correct_positions_dict
correct_positions_dict = {0: '', 1: '', 2: '', 3: '', 4: ''}
global correct_letters_list
correct_letters_list = []  # For correct letters in wrong positions
def wordle():
    i = 0
    for i, letter in enumerate(Solution):
        #gw.set_square_letter((N_ROWS - N_ROWS), (N_COLS - (N_COLS - i)), Solution[i])
        i += 1
    
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
            for i in range(N_COLS):
                    # Correct position
                    if default == True:
                        # Green
                        gw.set_square_color(
                            current_row, i, CORRECT_COLOR_DEFAULT)
                    elif default == False:
                        # Blue
                        gw.set_square_color(current_row, i, CORRECT_COLOR_ALT)
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
                            
                # Use a set for efficient membership checking
                used_indices_solution = set()
                used_indices_guessed = set()

                correct_letters_list.clear()
                i = 0
                correct_letter_positions = []
                for i in range(N_COLS):
                    typed_letter = typed_word[i]
                    random_letter = Solution[i]
                    if typed_letter == random_letter:
                        # Letter is correct and in the correct position
                        correct_positions.append(i)
                        correct_positions_dict[i] = typed_letter
                        used_indices_solution.add(i)
                        used_indices_guessed.add(i)
                    elif typed_letter in Solution and Solution.index(typed_letter) not in used_indices_solution:
                        correct_letter_positions.append(i)
                        correct_letters_list.append(typed_letter)
                        used_indices_solution.add(Solution.index(typed_letter))
                        used_indices_guessed.add(i)
                    
                # Color the boxes based on correctness
                for i in range(N_COLS):
                    if i in correct_positions:
                        # Correct position
                        if default == True:
                            # Green
                            gw.set_square_color(
                                current_row, i, CORRECT_COLOR_DEFAULT)
                        elif default == False:
                            # Blue
                            gw.set_square_color(current_row, i, CORRECT_COLOR_ALT)
                    elif i in correct_letter_positions:
                        # Correct letter in wrong position
                        if default == True:
                            # Brownish yellow
                            gw.set_square_color(
                                current_row, i, PRESENT_COLOR_DEFAULT)
                        elif default == False:
                            # Light pink
                            gw.set_square_color(current_row, i, PRESENT_COLOR_ALT)
                    else:
                        # Incorrect
                        if default == True:
                            # Grey
                            gw.set_square_color(
                                current_row, i, MISSING_COLOR_DEFAULT)
                        elif default == False:
                            # Tan/grey
                            gw.set_square_color(current_row, i, MISSING_COLOR_ALT)

                # Move to the next row
                if current_row < N_ROWS - 1:
                    gw.set_current_row(current_row + 1)
                else:
                    gw.show_message("Game over! The word was " + Solution)
            elif len(typed_word) <= 4:
                gw.show_message("Not enough letters")
                gw.set_current_row(current_row)
            else:
                gw.show_message("Not in word list")
                gw.set_current_row(current_row)
            

        
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    # Bind the '1' key to toggle the color scheme
    # gw._root.bind("1", lambda event: toggle_color_scheme())

    hard_mode_toggle_button()
    color_toggle_button()
    # display_instruction_message()
    wordle()