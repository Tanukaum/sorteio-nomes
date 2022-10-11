import tkinter as tk
import random
import pygame

pygame.mixer.init()
pygame.mixer.music.load("Bau.mp3")

def sorteio():
    global count
    pygame.mixer.music.play()
    count = 0
    count10()
   
    

def count10():
    global count
    count = count+0.1
    n1 = nomes_random[random.randrange(len(nomes_random))]
    n2 = nomes_random[random.randrange(len(nomes_random))]
    n3 = nomes_random[random.randrange(len(nomes_random))]

    pessoa_1.set(n1)
    pessoa_2.set(n2)
    pessoa_3.set(n3)

    if count >=10:
        pessoa_1.set(p1)
        pessoa_2.set(p2)
        pessoa_3.set(p3)
        label_text.set("PARABÉNS!!!")
    
    label_count.after(100,count10)
    

global count
count = 0
root = tk.Tk()
root.resizable(500,500)
frame_a= tk.Frame(root)
frame_esq = tk.Frame(frame_a)
frame_meio = tk.Frame(frame_a)
frame_dir = tk.Frame(frame_a)

pessoa_1 = tk.StringVar()
pessoa_2 = tk.StringVar()
pessoa_3 = tk.StringVar()
label_text = tk.StringVar()
label_count = tk.Label(root)
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

tk.Button(root, text='Sortear!',command=lambda :sorteio()).pack(side='bottom')

pessoas_para_sortear =["Naziond","Gilmeumo","Meindîr","Taron","Thurinpeu","Huam","Urbmeyble","Docuibush","Asba","Luglump","Shagnuehug","Mahkclo"]
nomes_random = ["Nazfasdion","Gilmeufkmo","Meilhjkndîr","Tariupon","Thurinperteu","Huamahfg","Urbhafdmeyble","Docuilkjhbush","Asbhkla","Lugluhjhjkmp","Shagnhjkuehug","Mahkcsdftlo"]

p1 = pessoas_para_sortear[random.randrange(len(pessoas_para_sortear))]
p2 = pessoas_para_sortear[random.randrange(len(pessoas_para_sortear))]
p3 = pessoas_para_sortear[random.randrange(len(pessoas_para_sortear))]

while p1 == p2:
    p2 = pessoas_para_sortear[random.randrange(len(pessoas_para_sortear))]

while p3 == p1 or p3 == p2:
    p3 = pessoas_para_sortear[random.randrange(len(pessoas_para_sortear))]




root.mainloop()