from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

#--UI--
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)



#add card using canvas widget:
canvas = Canvas(width=800 ,height=526, bg=BACKGROUND_COLOR, highlightthickness=0)#highlightthickness = 0 get rid of border around canvas
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image (400, 263, image=card_front_img) #height and width make a tuple, half of width and heignt (image)
canvas.grid(column=0, row=0) 



#BUTTONS:
# right_image = PhotoImage(file="images/right.png")  
# right_button = Button(image=right_image, highlightthickness=0)
#right_button.grid(column=0, row=2)

#wrong_image = PhotoImage(file="images/wrong.png")
# wrong_button = Button(image=wrong_image, highlightthickness=0, )
# wrong_button.grid(column=2, row=2)




window.mainloop()
