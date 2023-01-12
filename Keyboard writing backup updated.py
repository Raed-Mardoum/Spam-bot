from tkinter import *
import tkinter as tk
from tkinter.ttk import Button
import pyautogui
import time

running = True
while running:


    f = open("Replicated_storage.txt", "r+")
    f.truncate(0)
    f.close()




    root= tk.Tk()

    canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
    canvas1.pack()



    label1 = tk.Label(root, text='Enter Text')
    label1.config(font=('helvetica', 12))
    canvas1.create_window(200, 25, window=label1)

    label2 = tk.Label(root, text='Loop amount')
    label2.config(font=('helvetica', 12))
    canvas1.create_window(200, 100, window=label2)

    label3 = tk.Label(root, text='Speed of loop')
    label3.config(font=('helvetica', 12))
    canvas1.create_window(200, 175, window=label3)

    label4 = tk.Label(root, text='Counter')
    label4.config(font=('helvetica', 12))
    canvas1.create_window(350, 215, window=label4)



    k = StringVar()
    entry1 = tk.Entry(root, width=25, textvariable=k) 
    entry1.config(bg='light blue')
    canvas1.create_window(200, 65, window=entry1)

    entry2 = tk.Entry(root, width=7) 
    entry2.config(bg='light blue')
    canvas1.create_window(200, 140, window=entry2)

    entry3 = tk.Entry(root, width=7)
    entry3.config(bg='light blue')
    canvas1.create_window(200, 210, window=entry3)


    v = StringVar()
    entry4 = tk.Entry(root, width=7, textvariable=v)
    entry4.config(bg='light blue')
    canvas1.create_window(350, 250, window=entry4)




    def one_command():

        label4 = tk.Label(root, text='Complete', font=('helvetica', 10))
        canvas1.create_window(200, 275, window=label4)

        label4.after(1000, label4.destroy)


        e1 = entry1.get()
        print("e1: ", e1)

        e2 = entry2.get()
        print("e2: ", e2)

        e3 = entry3.get()
        print("e3: ", e3)

        e4 = entry4.get()
        print("e3: ", e4)


        file = open("Replicated_storage.txt", "w")

        file.write(e1 + "\n")
        file.write(e2 + "\n")
        file.write(e3 + "\n")
        file.write(e4 + "\n")

        file.close()

        Reading = open("Replicated_storage.txt", "r")


        global line1
        line1 = Reading.readline()
        print(line1)

        global line2
        line2 = Reading.readline()
        print(line2)

        global line3
        line3 = Reading.readline()
        print(line3)

        global line4
        line4 = Reading.readline()
        print(line4)



        Reading.close()










    button1 = tk.Button(text='Submit', command=one_command, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 250, window=button1)









    root.mainloop()
    time.sleep(3)



    if len(k.get()) == 0:

        counter = 0 


        print("line4", line4)


        while True:



            slide = int(line4) + counter

            street = str(slide)

            pyautogui.write(street, interval = float(line3))
            pyautogui.hotkey('shift', 'enter')

            counter += 1
            if counter == int(line2)+1:
                break

            else:
                print("Counter: ", counter)



    if len(v.get()) == 0:

        counter = 0 

        while True:



            pyautogui.write(line1, interval = float(line3))



            counter += 1
            if counter == int(line2):
                break

            else:
                print(counter)





    def close():
        print("Close")
        root.quit()
        global running
        running = False



    def redo():
        print("Redo")
        root.destroy()
        global running
        running = True
        




    root= tk.Tk()

    canvas2 = tk.Canvas(root, width=400, height=300, relief='raised')
    canvas2.pack()

    Finisher_button = tk.Button(root, text="Yes")
    Finisher_button.config(font=('helvetica', 12), bg='green', width= 5, command=redo)
    canvas2.create_window(250, 210, window=Finisher_button)

    Restart_button = tk.Button(root, text="No")
    Restart_button.config(font=('helvetica', 12), bg='red', width= 5, command=close)
    canvas2.create_window(150, 210, window=Restart_button)

    labels = tk.Label(root, text="Restart?")
    labels.config(font=('helvetica', 12))
    canvas2.create_window(200, 100, window=labels)

    root.mainloop()




