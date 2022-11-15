from tkinter import *
window = Tk()

#window Dimentions and configurations
window.geometry("840x660")
window.title("Genetics on campus")
headerimg = PhotoImage(file='genetics.png')
window.iconphoto(True, headerimg)

#Menu title & settings
TestLabel = Label(window,text="Main Menu",
                  font=('TimesNewRoman',18,'bold'),
                  relief=RAISED,
                  bd=5,
                  padx=50,
                  pady=5)
TestLabel.pack()

#menu options
'''
add commands to (def click:) and associated code to add
the graphs and such, this is still a WIP so bear with me!
:)

'''
def click():
    print('Good job! you made a working button!!!')


option1 = Button(window,
                 text="selection 1",
                 command=click,
                 font=("TimesNewRoman",14)
                 )
option1.pack()

#allows window to loop and respond to inputs
window.mainloop()
