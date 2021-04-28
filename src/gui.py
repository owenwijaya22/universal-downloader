from tkinter import *
root = Tk()

canvas = Canvas(root, height=350, width=700)
canvas.pack()

background_image = ImageTk.PhotoImage(file=r"C:\Users\owenw\Downloads\image.png")
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

button = Button(frame, text='Hack', font=40, command=lambda: test_button()) 
button.place(relx=0.5, relheight=1, relwidth=0.1, anchor='n')
button.counter = 0

lower_frame = Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75,
                  relheight=0.6, anchor='n')

button1 = Button(lower_frame, text='Quit', font=40,
                 command=lambda: root.quit())
button1.pack(side='bottom')

label = Label(lower_frame, text='Not Started')
label.place(relx=0.50, rely=0.10, relwidth=0.2, relheight=0.2, anchor='n')

label1 = Label(lower_frame, text='No error message')
label1.place(relx=0.50, rely=0.50, relwidth=0.7, relheight=0.16, anchor='n')
root.eval('tk::PlaceWindow . center')
root.mainloop()