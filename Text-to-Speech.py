## import libraries

from tkinter import *
from gtts import gTTS
from playsound import playsound



################### Initialized window####################

root = Tk()
root.geometry('350x300')
root.resizable(0,0)
root.config(bg = 'Yellow')
root.title('Swarnamythili - TEXT_TO_SPEECH')


##heading
Label(root, text = 'TEXT TO SPEECH' , font='algerian' , bg ='Yellow').pack()
Label(root, text ='Swarnamythili' , font ='algerian', bg = 'Yellow').pack(side = BOTTOM)




#label
Label(root, text ='Enter Text', font ='algerian', bg ='Yellow').place(x=20,y=60)


##text variable
Msg = StringVar()


#Entry
entry_field = Entry(root,textvariable =Msg, width ='50')
entry_field.place(x=20 , y=100)


###################define function##############################

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('swarnamythili.mp3')
    playsound('swarnamythili.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

#Button
Button(root, text = "PLAY" , font = 'algerian', command = Text_to_speech, width =4).place(x=25, y=140)
Button(root,text = 'EXIT',font = 'algerian' , command = Exit, bg = 'Green').place(x=100,y=140)
Button(root, text = 'RESET', font='algerian', command = Reset).place(x=175 , y =140)


#infinite loop to run program
root.mainloop()
