import random
import sys

import pygame
from PySide6.QtCore import Qt, Slot, QTimer
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QGridLayout,
                               QLineEdit, QPushButton, QVBoxLayout, QWidget)

pygame.mixer.init()
pygame.mixer.music.load("Bau.mp3")

class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.setGeometry(100,100,500,400)
		self.setWindowTitle("Sorteio")
		self.main_vLayout = QVBoxLayout()

		self.hLayout_1 = QHBoxLayout()
		self.main_vLayout.addLayout(self.hLayout_1)

		self.hLayout_2 = QHBoxLayout()
		self.main_vLayout.addLayout(self.hLayout_2)

		self.grid_pessoa = QGridLayout()
		self.hLayout_2.addLayout(self.grid_pessoa)
		
		

		self.timer = QTimer()
		self.timer.timeout.connect(self.count10)


		self.pessoa_2 = QLineEdit()
		self.label_pessoal_2 = QLabel()
		self.label_pessoal_2.setText('2º Lugar')
		self.grid_pessoa.addWidget(self.label_pessoal_2,0,0,Qt.AlignHCenter)
		self.grid_pessoa.addWidget(self.pessoa_2,1,0)
		self.pessoa_2.setText(' ')
		self.pessoa_2.setContentsMargins(0,0,0,25)

		self.pessoa_1 = QLineEdit()
		self.label_pessoa_1 = QLabel()
		self.label_pessoa_1.setText('1º Lugar')
		self.grid_pessoa.addWidget(self.label_pessoa_1,0,1,Qt.AlignHCenter)
		self.grid_pessoa.addWidget(self.pessoa_1,1,1)
		self.pessoa_1.setText(' ')
		self.pessoa_1.setContentsMargins(0,0,0,55)

		self.pessoa_3 = QLineEdit()
		self.label_pessoa_3 = QLabel()
		self.label_pessoa_3.setText('3º Lugar')
		self.grid_pessoa.addWidget(self.label_pessoa_3,0,2,Qt.AlignHCenter)
		self.grid_pessoa.addWidget(self.pessoa_3,1,2)
		self.pessoa_3.setText(' ')

		self.label = QLabel(self)
		self.hLayout_1.addWidget(self.label)
		self.label.setAlignment(Qt.AlignHCenter)

		self.button = QPushButton('Sortear')
		self.main_vLayout.addWidget(self.button)
		self.button.clicked.connect(self.sorteio)

		self.movie = QMovie('piao2.gif')
		self.label.setMovie(self.movie)
		
		self.movie.start()
		self.setLayout(self.main_vLayout)
		
	@Slot()
	def sorteio(self):
		global count
		pygame.mixer.music.play()
		count = 0
		self.count10()

	@Slot()
	def count10(self):
		global count
		count = count+0.1
		n1 = nomes_random[random.randrange(len(nomes_random))]
		n2 = nomes_random[random.randrange(len(nomes_random))]
		n3 = nomes_random[random.randrange(len(nomes_random))]

		self.pessoa_1.setText(n1)
		self.pessoa_2.setText(n2)
		self.pessoa_3.setText(n3)

		if count >=10:
			self.pessoa_1.setText(p1)
			self.pessoa_2.setText(p2)
			self.pessoa_3.setText(p3)
		self.timer.start(100)
	

	


global count
count = 0
pessoas_para_sortear =["Naziond","Gilmeumo","Meindîr","Taron","Thurinpeu","Huam","Urbmeyble","Docuibush","Asba","Luglump","Shagnuehug","Mahkclo"]
nomes_random = ["Nazfasdion","Gilmeufkmo","Meilhjkndîr","Tariupon","Thurinperteu","Huamahfg","Urbhafdmeyble","Docuilkjhbush","Asbhkla","Lugluhjhjkmp","Shagnhjkuehug","Mahkcsdftlo"]

p1 = pessoas_para_sortear[random.randrange(len(pessoas_para_sortear))]
p2 = pessoas_para_sortear[random.randrange(len(pessoas_para_sortear))]
p3 = pessoas_para_sortear[random.randrange(len(pessoas_para_sortear))]

#Inicialização da Aplicação
app = QApplication([])
window = Window()
window.show()

sys.exit(app.exec())
