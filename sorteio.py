import random
from playsound import playsound
from pyautogui import sleep

peoes =["nome 1","nome 2","nome 3","nome 4"]
p1 = peoes[random.randrange(len(peoes))]
p2 = peoes[random.randrange(len(peoes))]
p3 = peoes[random.randrange(len(peoes))]

while p1 == p2:
    p2 = peoes[random.randrange(len(peoes))]

while p3 == p1 or p3 == p2:
    p3 = peoes[random.randrange(len(peoes))]

print("SORTEIO")
playsound("Bau.mp3",0)
sleep(1)
print('....')
sleep(1)
print('....')
sleep(1)
print('....')
sleep(1)
print('....')
sleep(1)
print('....')
sleep(1)
print('....')
sleep(1)
print('....')
sleep(1)
print('....')
sleep(1)
print('....')
sleep(1)
print('....')
print("O primeiro ganhador é:  " + p1)

sleep(2)
print("\n\n\nSORTEANDO O PRÓXIMO GANHADOR")
playsound("tambores.mp3",0)
sleep(1)
print('....')
sleep(1)
print('....')
sleep(1)
print('....')
sleep(1)
print('....')
sleep(1)
print('....')
sleep(1)
print('....')
sleep(0.55)
print('....')
print("O segundo ganhador é:  " + p2)


sleep(2)
print("\n\n\nSORTEANDO O PRÓXIMO GANHADOR")
playsound("tambores.mp3",0)
sleep(1)
print('....')
sleep(1)
print('....')
sleep(1)
print('....')
sleep(1)
print('....')
sleep(1)
print('....')
sleep(1)
print('....')
sleep(0.55)
print('....')
print("O terceiro ganhador é:  " + p3)

sleep(1)
print("PARABÉNS!!!")

