from tkinter import *
import pandas as pd  
import random  

BACKGROUND_COLOR = "#B1DDC6"

#--BUTTON FUNCTIONALITY:

data = pd.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient='records')  # Change parameter:orient = 'records' so I get list of dicts  

def next_card():
    #pick random choice from dictionary:
    current_card = random.choice(to_learn)
    #random french word:
    current_card['French']
    #Pass word to the card (front):
    canvas.itemconfig(card_title, text = "French")
    canvas.itemconfig(card_word, text = current_card['French'])


#--UI:
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)



#add card using canvas widget:
canvas = Canvas(width=800 ,height=526, bg=BACKGROUND_COLOR, highlightthickness=0)#highlightthickness = 0 get rid of border around canvas
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image (400, 263, image=card_front_img) #height and width make a tuple, half of width and heignt (image)
card_title = canvas.create_text(400, 150,text="Title", font=("Arial", 40, "italic"))#font is  atuple, x and y are relative to the canvas
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2) # columnspan=2 to center buttons relative to card

#BUTTONS:
right_image = PhotoImage(file="images/right.png")  
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)




window.mainloop()
