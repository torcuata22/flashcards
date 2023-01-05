from tkinter import *
import pandas as pd  
import random  
import time


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn= {}

#--BUTTON FUNCTIONALITY (handle exceptions):

try:
    data = pd.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient='records')

else:
    to_learn = data.to_dict(orient='records')  # Change parameter:orient = 'records' so I get list of dicts  
   

def next_card():
    global current_card, flip_timer, to_learn
    window.after_cancel(flip_timer)
    #pick random choice from dictionary:
    current_card = random.choice(to_learn)
    #random french word:
    current_card['French']
    #Pass word to the card (front):
    canvas.itemconfig(card_title, text = "French", fill="black")
    canvas.itemconfig(card_word, text = current_card['French'], fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)
    flip_timer = window.after(3000, flip_card) #new flip timer, needs to happen every time we have new card

#FUNCTION TO FLIP THE CARD AND SHOW ENGLISH WORD:
def flip_card():
    current_card["English"]
    canvas.itemconfig(card_title, text="English", fill="white") #element to modify, new text
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)

#removes current card from stack becasue user knows it
def is_known():
    to_learn.remove(current_card)
    next_card()
    #To save progress, create new list (start with pd DF)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index = False)

#--UI:
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#FLIP THE CARD (show English word):
flip_timer = window.after(3000, flip_card)


#add card using canvas widget:
canvas = Canvas(width=800 ,height=526, bg=BACKGROUND_COLOR, highlightthickness=0)#highlightthickness = 0 get rid of border around canvas
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image (400, 263, image=card_front_img) #height and width make a tuple, half of width and heignt (image)
card_title = canvas.create_text(400, 150,text="Title", font=("Arial", 40, "italic"))#font is  atuple, x and y are relative to the canvas
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2) # columnspan=2 to center buttons relative to card


#BUTTONS:
right_image = PhotoImage(file="images/right.png")  
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)



next_card()




window.mainloop()
