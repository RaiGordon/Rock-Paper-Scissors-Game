#TODO change emojis

from tkinter import *
from tkinter import ttk
import random
from PIL import Image, ImageTk
from hdpitkinter import HdpiTk
import webbrowser

#brings frame to the front
def raise_frame(frame):
    frame.tkraise()

#Constants for configuration
HEIGHT = 540
WIDTH = 540
BG_COLOUR = "#151515"

# variables /constanats for game play
CENTER = WIDTH / 2
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
button_clicked = []
empty = ""
rock_wins = "Rock smashed scissors. "
paper_wins = "Paper covered rock. "
scissors_wins = "Scissors cut paper. "
players_round = "You won!"
comps_round = "You lost!"
GAME_PLAYS = {"rounds": 0}
SCORES = {"player": 0, "computer": 0}

rounds_played = "Round {} / 5".format(str(GAME_PLAYS['rounds']))
increment_score = "Player: {} {:^80} Computer: {}".format(str(SCORES['player']), empty, str(SCORES['computer']))

# create window
root = HdpiTk()

#########################SCREEN CONFIGURATIONS#########################

root.geometry('540x540')
root.resizable(0, 0)

# set a fixed game size and title
root.title("Rock Paper Scissors Game")

# game icon and name details
icon = PhotoImage(file='media/cfg-rps-icon.png')
root.iconphoto(True, icon)
root.title('Rock, Paper, Scissors Game')

# game height and width based on user screensize
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# game movement on x and y axis
x = int((screen_width / 2) - (WIDTH / 2))
y = int((screen_height / 2) - (HEIGHT / 2))

# centralise game to screen
root.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, x, y))

#########################PAGES AND PAGE DIMENSIONS#########################

#//////INSTRUCTIONS PAGE
# instructions frame page
instructions_frame = Frame(root)
instructions_frame.place(x=0, y=0, width=WIDTH, height=HEIGHT)
# canvas // instructions
instructions_canvas = Canvas(instructions_frame, width=WIDTH, height=HEIGHT)
instructions_canvas.grid(columnspan=12, rowspan=15)
instructions_canvas.config(bg=BG_COLOUR)

#//////GAME PAGE
# game frame page
game_frame = Frame(root)
game_frame.place(width=WIDTH, height=HEIGHT)
# canvas // game
game_canvas = Canvas(game_frame, width=WIDTH, height=HEIGHT)
game_canvas.grid(columnspan=12, rowspan=15)
game_canvas.config(bg=BG_COLOUR)

#//////SCORE PAGE
# score frame page
score_frame = Frame(root)
score_frame.place( width=WIDTH, height=HEIGHT)
# canvas // game
score_canvas = Canvas(score_frame, width=WIDTH, height=HEIGHT)
score_canvas.grid(columnspan=12, rowspan=15)
score_canvas.config(bg=BG_COLOUR)

#//////SPLASH PAGE
# splash page frame page
splash_frame = Frame(root)
splash_frame.place( width=WIDTH, height=HEIGHT)
# canvas // splash
splash_canvas = Canvas(splash_frame, width=WIDTH, height=HEIGHT)
splash_canvas.grid(columnspan=8, rowspan=5)
splash_canvas.config(bg=BG_COLOUR)

####Buttons Styles####
rps_button_style = ttk.Style(root)
rps_button_style.theme_use('alt')
rps_button_style.configure('TButton',
                           background='#42A65E',
                           foreground='black',
                           font=("Arial", 18, 'bold'),
                           borderwidth=0, )
rps_button_style.map('TButton', background=[('active', '#29663A')])

####Labels####

# make your choice label = LABEL1
label1 = Label(game_frame, text="")
label1.config(background='#151515', foreground='white', font=("Arial", 18, ), )
game_canvas.create_window(CENTER, 130, window=label1)

# ***Game page*** label to ask user to make a choice.
def make_choice_label():
    if GAME_PLAYS['rounds'] == 0:
        label1.config(text="Let's settle this!")
    elif GAME_PLAYS['rounds'] >= 1:
        label1.config(text="Make your choice.")

# ***Game page*** displaying score at top of game = LABEL2
label2 = Label(game_frame, text=increment_score)
label2.config(background='#593E3E', foreground='white', font=("Arial", 14), pady=5, padx=WIDTH)
game_canvas.create_window(CENTER, 20, window=label2)

# ***Game page*** dissplaying amount of games played at top of game = LABEL3
label3 = Label(game_frame, text=rounds_played)
label3.config(background='#593E3E', foreground='white', font=("Arial", 14), )
game_canvas.create_window(CENTER, 20, window=label3)

#Function to allow make your choice text to change depending on result
make_choice = make_choice_label()

# ***Score page***displaying score label = LABEL4
label4 = Label(score_frame, text="scores")
label4.config( background = '#151515', foreground = 'white',font=("Arial", 24),)
score_canvas.create_window(CENTER, 300, window=label4)

#########################/////////////////////SPLASH PAGE/////////////////////#######################

####Images####

# rock image ///splash page
rock_hand=Image.open('media/buttons/alts/rock-alt2.png')
rock_image_resized=rock_hand.resize((230, 190))
new_rock_hand = ImageTk.PhotoImage(rock_image_resized)
splash_canvas.create_image(-60,30, image=new_rock_hand, anchor=NW)

# paper image ///splash page
paper_hand=Image.open('media/buttons/alts/paper-alt.png')
paper_image_resized=paper_hand.resize((140, 260))
new_paper_hand = ImageTk.PhotoImage(paper_image_resized)
splash_canvas.create_image(190,-40, image=new_paper_hand, anchor=NW)

# scissors image ///splash page
scissors_hand=Image.open('media/buttons/alts/scissors-alt.png')
scissors_image_resized=scissors_hand.resize((240, 260))
new_scissors_hand = ImageTk.PhotoImage(scissors_image_resized)
splash_canvas.create_image(360,-10, image=new_scissors_hand, anchor=NW)

# title of game image ///splash page
title_image = Image.open('media/game_title-alt.png')
title_image_resized = title_image.resize((350, 50))
new_title_image = ImageTk.PhotoImage(title_image_resized)
splash_canvas.create_image(85, 290, image=new_title_image, anchor=NW)

####Buttons####

# start game button
start_game = ttk.Button(
    splash_frame,
    text="Start",
    width=15,
    command=lambda: raise_frame(game_frame))
start_game.grid(column=2, row=4, ipadx=10, ipady=20)

# instructions button
instructions_btn = ttk.Button(
    splash_frame,
    text='Instructions',
    width=15,
    command=lambda: raise_frame(instructions_frame))
instructions_btn.grid(column=5, row=4, ipadx=10, ipady=20)

#########################/////////////////////GAME PAGE/////////////////////#######################

####Images####

# rock image ///game page
rock_hand2 = Image.open('media/rock.png')
rock_image_resized2 = rock_hand2.resize((160, 280))
new_rock_hand2 = ImageTk.PhotoImage(rock_image_resized2)
game_canvas.create_image(10, 150, image=new_rock_hand2, anchor=NW)

# paper image ///game page
paper_hand2 = Image.open('media/paper.png')
paper_image_resized2 = paper_hand2.resize((160, 190))
new_paper_hand2 = ImageTk.PhotoImage(paper_image_resized2)
game_canvas.create_image(200, 190, image=new_paper_hand2, anchor=NW)

# scissors image ///game page
scissors_hand2 = Image.open('media/scissors.png')
scissors_image_resized2 = scissors_hand2.resize((180, 220))
new_scissors_hand2 = ImageTk.PhotoImage(scissors_image_resized2)
game_canvas.create_image(340, 190, image=new_scissors_hand2, anchor=NW)

####Emoji Images####

# TIE EMOJI
game_tie_emoji = Image.open('media/buttons/meh.png')
tie_emoji_img = game_tie_emoji.resize((50, 50))
tie_emoji = ImageTk.PhotoImage(tie_emoji_img)

# HAPPY WINS EMOJI
game_happy_emoji = Image.open('media/buttons/happy.png')
happy_emoji_img = game_happy_emoji.resize((50, 50))
happy_emoji = ImageTk.PhotoImage(happy_emoji_img)

# SAD EMOJI
game_sad_emoji = Image.open('media/buttons/sad.png')
sad_emoji_img = game_sad_emoji.resize((50, 50))
sad_emoji = ImageTk.PhotoImage(sad_emoji_img)

####Emoji Images####

# Make computers choice a function for later use
def computers_turn():
    global computer
    computer = random.choice(choices)

# Display a label showing who won and why at the end of each round
def display_choices_func():
    if computer == button_clicked:
        label1.config(text="It's a tie! \n You both chose " + button_clicked, image=tie_emoji, compound='top')
    if "rock" in computer:
        if "paper" in button_clicked:
            label1.config(text=players_round + "\n " + paper_wins, image=happy_emoji, compound='top')
        elif "scissors" in button_clicked:
            label1.config(text=comps_round + "\n " + rock_wins, image=sad_emoji, compound='top')
    if "paper" in computer:
        if "rock" in button_clicked:
            label1.config(text=comps_round + "\n " + paper_wins, image=sad_emoji, compound='top')
        elif "scissors" in button_clicked:
            label1.config(text=players_round + "\n " + scissors_wins, image=happy_emoji, compound='top')
    if "scissors" in computer:
        if "rock" in button_clicked:
            label1.config(text=players_round + "\n " + rock_wins, image=happy_emoji, compound='top')
        elif "paper" in button_clicked:
            label1.config(text=comps_round + "\n " + scissors_wins, image=sad_emoji, compound='top')

# Function to make scores go back to 0 if game plays restarts
def zero_scores():
    if GAME_PLAYS["rounds"] == 0:
        SCORES["player"] = 0
        SCORES["computer"] = 0

####Display scores on score page####

def who_wins():
    global SCORES
    if SCORES["player"] > SCORES["computer"]:
        label4.config(text="You win " + str(SCORES["player"]) + " / " + str(SCORES["computer"]))
    elif SCORES["player"] < SCORES["computer"]:
        label4.config(text="Computer wins " + str(SCORES["computer"]) + " / " + str(SCORES["player"]))
    elif SCORES["player"] == SCORES["computer"]:
        label4.config(text="You tie. " + str(SCORES["computer"]) + " / " + str(SCORES["player"]))


####What happens if useer presses a rock, paper, scissors button####

# **TIE GAME**
def tie_game():
    global GAME_PLAYS
    global SCORES
    if GAME_PLAYS["rounds"] ==5:
        zero_scores()
        GAME_PLAYS["rounds"] -= 5
        label3.config(text="Round {} / 5".format(str(GAME_PLAYS['rounds'])))
        raise_frame(score_frame)
    elif GAME_PLAYS["rounds"] <= 4:
        zero_scores()
        GAME_PLAYS["rounds"] += 1
        label2.config(text="Player: {} {:^80} Computer: {}".format(str(SCORES['player']), empty, str(SCORES['computer'])))
        label3.config(text="Round {} / 5".format(str(GAME_PLAYS['rounds'])))
        who_wins()
        display_choices_func()
        label1.after(2000, make_choice)
        make_choice_label()

# **PLAYER WINS**
def you_won():
    global GAME_PLAYS
    global SCORES
    if GAME_PLAYS["rounds"] ==5:
        zero_scores()
        GAME_PLAYS["rounds"] -= 5
        zero_scores()
        label3.config(text="Round {} / 5".format(str(GAME_PLAYS['rounds'])))
        raise_frame(score_frame)
    elif GAME_PLAYS["rounds"] <= 4:
        zero_scores()
        GAME_PLAYS["rounds"] += 1
        global player_wins
        SCORES["player"] += 1
        label2.config(text="Player: {} {:^80} Computer: {}".format(str(SCORES['player']), empty, str(SCORES['computer'])))
        label3.config(text="Round {} / 5".format(str(GAME_PLAYS['rounds'])))
        who_wins()
        display_choices_func()
        label1.after(2000, make_choice)
        make_choice_label()

# **PLAYER LOSES**
def you_lost():
    global SCORES
    global GAME_PLAYS
    if GAME_PLAYS["rounds"] ==5:
        zero_scores()
        GAME_PLAYS["rounds"] -=5
        zero_scores()
        label3.config(text="Round {} / 5".format(str(GAME_PLAYS['rounds'])))
        raise_frame(score_frame)
    elif GAME_PLAYS["rounds"] <= 4:
        zero_scores()
        GAME_PLAYS["rounds"] += 1
        global comp_wins
        SCORES["computer"] += 1
        label2.config(text="Player: {} {:^80} Computer: {}".format(str(SCORES['player']), empty, str(SCORES['computer'])))
        label3.config(text="Round {} / 5".format(str(GAME_PLAYS['rounds'])))
        who_wins()
        display_choices_func()
        label1.after(2000, make_choice)
        make_choice_label()
        root.update_idletasks()

####Button Functions####

# What will be displayed if each button is clicked
def rock_button():
    global button_clicked
    button_clicked = choices[0]
    computers_turn()
    if computer == button_clicked:
        tie_game()
    elif computer == choices[1]:
        you_lost()
    elif computer == choices[2]:
        you_won()

def paper_button():
    global button_clicked
    button_clicked = choices[1]
    computers_turn()
    if computer == button_clicked:
        tie_game()
    elif computer == choices[2]:
        you_lost()
    elif computer == choices[0]:
        you_won()

def scissors_button():
    global button_clicked
    button_clicked = choices[2]
    computers_turn()
    if computer == button_clicked:
        tie_game()
    elif computer == choices[0]:
        you_lost()
    elif computer == choices[1]:
        you_won()

####Buttons####

# rock button
rk_button = ttk.Button(game_frame, text="ROCK", command=rock_button, )
rk_button.grid(column=3, row=13, ipadx=17, ipady=60, )

# paper button
ppr_button = ttk.Button(game_frame, text="PAPER", command=paper_button)
ppr_button.grid(column=5, row=13, ipadx=17, ipady=60)

# scissors button
scs_button = ttk.Button(game_frame, text="SCISSORS", command=scissors_button)
scs_button.grid(column=7, row=13, ipadx=17, ipady=60, )

#########################/////////////////////SCORE PAGE/////////////////////#######################

####Background Images####

# rock image ///score page
rock_hand3=Image.open('media/buttons/alts/rock-alt2.png')
rock_image_resized3=rock_hand3.resize((230, 190)) #alt = 220,300
new_rock_hand3 = ImageTk.PhotoImage(rock_image_resized3)
score_canvas.create_image(-70,30, image=new_rock_hand3, anchor=NW) #alt = -45, 30

# paper image ///score page
paper_hand3=Image.open('media/buttons/alts/paper-alt.png')
paper_image_resized3=paper_hand3.resize((140, 260))
new_paper_hand3 = ImageTk.PhotoImage(paper_image_resized3)
score_canvas.create_image(170,-40, image=new_paper_hand3, anchor=NW)

# scissors image ///score page
scissors_hand3=Image.open('media/buttons/alts/scissors-alt.png')
scissors_image_resized3=scissors_hand3.resize((240, 260))
new_scissors_hand3 = ImageTk.PhotoImage(scissors_image_resized3)
score_canvas.create_image(330,-10, image=new_scissors_hand3, anchor=NW)

####Buttons####

# Play again button
play_again_button = ttk.Button(score_frame, text="Play again", width=15, command=lambda: raise_frame(game_frame))
play_again_button.grid(column=3, row=13,ipadx=10, ipady=20)

# Exit game button
quit_btn = ttk.Button(score_frame, text='Exit', width=15, command=root.destroy)
quit_btn.grid(column=8, row=13,ipadx=10, ipady=20 )

#########################/////////////////////INSTRUCTIONS PAGE/////////////////////#######################
####Buttons####

# back to Play game
instr_play_game_button = ttk.Button(instructions_frame, text="Play Game", width=15, command=lambda: raise_frame(game_frame))
instr_play_game_button.grid(column=4, columnspan=4, row=13,ipadx=10, ipady=20)


####Labels####

# Title label
inst_title = Label(instructions_frame, text="How to play")
inst_title.config(background='#151515', foreground='white', font=("Arial", 26, 'bold'), )
instructions_canvas.create_window(CENTER, 50, window=inst_title)

#Text to go onto instructions page
instructions = "Two players will each randomly choose one of three hand signs: \n\n" \
               "► ROCK (made by making a fist)\n" \
               "► PAPER (made by laying your hand flat)\n" \
               "► SCISSORS (made by holding out two fingers to look like scissors)\n \n" \
               "Both players show their signs at the same time to see who will win. \n \n" \
               "Here are the rules that determine which sign beats another: \n\n" \
               "► ROCK wins over scissors (because rock smashes scissors) \n" \
               "► PAPER wins over rock (because paper covers rock)\n" \
               "► SCISSORS wins over paper (because scissors cut paper)\n\n" \
               "If both players show the same sign, it’s a tie. \n\n" \
               "Good Luck!"



# Main instructions
inst_main = Label(instructions_frame, text=instructions, anchor="e", justify=LEFT)
inst_main.config(background='#151515', foreground='#DAD2D8', font=("Arial", 16,))
instructions_canvas.create_window(CENTER, 250, window=inst_main)

mainloop()