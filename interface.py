from datetime import datetime, timedelta
import tkinter as tk
import random
from playsound import playsound
from pyautogui import sleep


def sorteio(pessoa_1,pessoa_2,pessoa_3):
    pessoas =["Bianca Rodrigues","Fernando Júlio","Henrique Caldas","Henrique Jurgens","Isabella Kelles","Lucas Lima","Luigi Willian", "Moisés Soares","Fabio Mariano","Gustavo Silvestre","Marcelo Boufleur", "Rafael Cardoso","Rodrigo Garcia","Rafael Helvadjian","Rodrigo Casita","Marcos Lucena","Roberto Santos","Acelino","Walter Piantavinha", "Ayrton Pitta","João Crispim","Ivan Gustavo"]
    p1 = pessoas[random.randrange(len(pessoas))]
    p2 = pessoas[random.randrange(len(pessoas))]
    p3 = pessoas[random.randrange(len(pessoas))]
    while p1 == p2:
        p2 = pessoas[random.randrange(len(pessoas))]

    while p3 == p1 or p3 == p2:
        p3 = pessoas[random.randrange(len(pessoas))]

    playsound("Bau.mp3",0)
    sleep(10)
    pessoa_1.set(p1)
    pessoa_2.set(p2)
    pessoa_3.set(p3)
    
    
    label_text.set("PARABÉNS!!!")


    

root = tk.Tk()
root.resizable(500,500)
frame_a= tk.Frame(root)
frame_esq = tk.Frame(frame_a)
frame_meio = tk.Frame(frame_a)
frame_dir = tk.Frame(frame_a)

pessoa_1= tk.StringVar()
pessoa_2= tk.StringVar()
pessoa_3= tk.StringVar()
label_text = tk.StringVar()
label_text.set("Sorteio")
tk.Entry(root, textvariable=label_text,justify='center', font="Arial 16").pack(side='top', fill='x')

tk.Label(frame_meio, text="1º Lugar").pack(side='top')
entry_1 = tk.Entry(frame_meio, textvariable=pessoa_1, justify='center').pack()

tk.Label(frame_esq, text="2º Lugar").pack(side='top')
entry_2 = tk.Entry(frame_esq, textvariable=pessoa_2, justify='center').pack()

tk.Label(frame_dir, text="3º Lugar").pack(side='top')
entry_3 = tk.Entry(frame_dir, textvariable=pessoa_3, justify='center').pack()


frame_esq.pack(side='left', padx= 10, ipady=10)
frame_meio.pack(side='left', padx= 10, ipady=20)
frame_dir.pack(side='left', padx= 10, ipady=5)
frame_a.pack()

tk.Button(root, text='Sortear!',command=lambda : sorteio(pessoa_1,pessoa_2,pessoa_3)).pack(side='bottom')





root.mainloop()