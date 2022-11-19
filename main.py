from tkinter import *
from PIL import Image,ImageTk

counter = -1
task = None

def start_typing():
    global counter, task
    textentry.config(bg="#F6962C", highlightbackground = "#21181B", highlightcolor= "#21181B", highlightthickness=12)
    textentry.focus()
    input = textentry.get("1.0", 'end-1c').split(' ')
    input_words = len(input) - 1

    original_sentence = canvas.itemcget(sentence, 'text').split(' ')
    total_words = len(original_sentence)


    counter += 1
    print(f"counter:{counter}")

    if input_words >= total_words:
        window.after_cancel(task)

    if counter % 10 == 0 and counter != 0:
        original_sentence = [word.lower() for word in original_sentence]
        correct_words = len([word for word in input if word.lower() in original_sentence])
        print(f"correct_words:{correct_words} and total_words: {total_words}")
        text = f"{int(correct_words * 60 / counter)} WPM"
        canvas.itemconfig(speed, text=text)
        task = window.after(1000, start_typing)
    else:
        task = window.after(1000, start_typing)







window = Tk()
window.geometry("700x700")
window.title("Typing Speed Test")

canvas = Canvas(window, width=700, height=700)
img= ImageTk.PhotoImage(Image.open("images/background.png"))
canvas.create_image(350, 350, image=img)


sentence = canvas.create_text(350, 200,width=700, text="I got some good news and some bad news. The bad news is that your father "
                                            "has bought a condo in Flip City and the good news is that he is about to win the Civil War.",
                   font=("Helvetica", 20, "normal"), fill="#484D51")

speed = canvas.create_text(160, 30, text="", fill="#E5A510", font=("Helvetica", 16, "bold"))


textentry = Text(canvas, font=("Helvetica", 20, "normal"), bg="#EDF1F2", highlightthickness=0,borderwidth=0, highlightbackground = "#EDF1F2", highlightcolor= "#EDF1F2")
canvas.create_window(350, 420, window=textentry, height=200, width=700)


button = Button(canvas, text='START', command=start_typing, width=13, height=1, bg="#F6962C", highlightthickness=0, borderwidth=0, font=("ariel", "17","bold"), fg="white")
button.place(x=258, y=650)



canvas.place(x=0, y=0)









window.mainloop()