from pyknon.genmidi import Midi
from pyknon.music import NoteSeq
import random
from tkinter import *
import pygame
# from PIL import Image


pygame.init()
top = Tk()
top.configure(background='#5DADE2')
top.geometry('400x450')
top.title("MIDI generator")

def helloCallBack3():
    pygame.mixer.music.pause()


def helloCallBack2():

    ccc= int(message_entry.get())
    # print(ccc)
    ccc2= int(message_entry2.get())
    # print(ccc2)
    ccc3= int(message_entry3.get())
    # print(ccc3)
    ccc4= int(message_entry4.get())
    # print(ccc4)

    list_note = ["G B D", "E", "D", "G", "C", "C E G", "E G B", "D F A",
                "A C F#", "F A C",
                "G E C A", "D B G E", "C A F D",
                "E C A", "D B G", "C A F"
                ]


    gh = 0
    chord = []
    while gh <=16:

        ggf = random.randint(0,15)

        chord.append(NoteSeq(list_note[ggf]))
        gh=gh+1

    seqlist = []
    h = 0
    while h <= 15:

        h = h + 1

        seqlist.append(chord[h])


    midi3 = Midi(ccc3, tempo=ccc, instrument=ccc2)
    midi3.seq_chords(seqlist, track=ccc4)  # можно добавить time=3 или равное чему ещё угодно
    midi3.write('sad.mid')
    pygame.mixer.music.load("sad.mid")
    pygame.mixer.music.play()

def helloCallBack1():
    ccc = int(message_entry.get())
    print(ccc)
    ccc2= int(message_entry2.get())
    print(ccc2)
    ccc3= int(message_entry3.get())
    print(ccc3)
    ccc4= int(message_entry4.get())
    print(ccc4)

    i = 0
    ass = []
    ass2 = []
    while i <= 23:

        i = i + 1
        ass.append(random.randint(0, 23))

    # print(ass)




    minor=["C E G", "C E# G", "C D G", "C F G", "C G", "C E G B", "C E# G B#", "C E G B#", "C E G D", "C E G A", "C E G A D"]
    chord2 = []
    gh2=0
    while gh2 <=10:
        ggf = random.randint(0, 10)
        chord2.append(NoteSeq(minor[ggf]))
        gh2= gh2+1


    seqlist = []

    h = 0
    while h <= 9:
        h = h + 1
        print(h)
        seqlist.append(chord2[h])




    print('lol')
    print(seqlist)
    midi3 = Midi(ccc3, tempo=ccc, instrument=ccc2)
    midi3.seq_chords(seqlist, track=ccc4)
    midi3.write('happy.mid')

    pygame.mixer.music.load("happy.mid")
    pygame.mixer.music.play()
    pygame.mixer.music.stop()






pos = Label(text="", fg="#eee", bg="#333", width=7, height=7)
pos.place()






sms = Button(top, text ="happy", command = helloCallBack1, width=10, height=1, background="#D0ECE7", relief="flat")
sms2 = Button(top, text ="sad", command = helloCallBack2, width=10, height=1, background="#D0ECE7", relief="flat")
sms3 = Button(top, text ="pause", command = helloCallBack3, width=10, height=1, background="#D0ECE7", relief="flat")
message_entry = Entry(top, width=10)
message_entry.place(x=50, y=70)
message_entry2 = Entry(top, width=10)
message_entry2.place(x=130, y=70)
message_entry3 = Entry(top, width=10)
message_entry3.place(x=210, y=70)
message_entry4 = Entry(top, width=10)
message_entry4.place(x=290, y=70)


label1 = Label(text="tempo:", fg="#eee", bg="#333")
label2 = Label(text="instrument:", fg="#eee", bg="#333")
label3 = Label(text="repeats:", fg="#eee", bg="#333")
label4 = Label(text="track:", fg="#eee", bg="#333")
label1.place(x=60, y=30)
label2.place(x=130, y=30)
label3.place(x=220, y=30)
label4.place(x=300, y=30)







sms.place(x=120, y=150)
sms2.place(x=210, y=150)
sms3.place(x=165, y=200)


# img = ImageTk.PhotoImage(Image.open("logo.png"))
# panel = Label(root, image = img)
# panel.pack(side = "bottom", fill = "both", expand = "yes")



# img = Image.open("logo.jpg")
# resized_img = img.resize((200, 100))
# top.photoimg = PhotoImage(resized_img)
# labelimage = Label(top, image=top.photoimg)
# # panel = Label(top, image = resized_img, width=100, height=100)
# labelimage.place(x=120,y=300)

temp = PhotoImage(file = "logo.png")
Label(top, image = temp, width=200, height=100).place(x=100,y=300)


top.mainloop()