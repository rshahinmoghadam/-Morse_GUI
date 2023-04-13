import RPi.GPIO as GPIO # import the GPIO library	
from time import sleep # import the time for apply delay
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QWidget, QLabel, QMessageBox

import sys



GPIO.setmode(GPIO.BOARD) # set the standard mode 
GPIO.setup(40,GPIO.OUT) # set the port 40 as output to LED



class window(QWidget): # create a class of window
	def __init__(self):		# the cunstructor
		super().__init__()
		
		#GPIO.output(40,GPIO.LOW)
		
		self.setGeometry(600, 600, 400, 300)	# setting the size of window
		self.setWindowTitle("Task 5.3D")	#setting the title of the window
		
		
		self.textbox = QLineEdit(self)		# create an empty text box for user input
		self.textbox.move(50,80)			# move to the right location
		self.textbox.setMaxLength(12)		# set the max number of letters allowed 
		
		
		regex = QtCore.QRegExp("[A-Z_]+")	# setting a validator to limit the input fromuser to Capital letters only
		validator = QtGui.QRegExpValidator(regex)
		self.textbox.setValidator(validator)
		
		label = QLabel("Only Capital letters allowed!",self)	# create a lable that tells user only capital letters allowed
		label.move(50,10)
		
		
		b5 = QtWidgets.QPushButton(self)		# create a push button for Exit
		b5.setText("Exit")
		b5.move(50,120)
		b5.clicked.connect(app.quit)
		
		
		
		b1 = QtWidgets.QPushButton(self)		# create a push button for morse
		b1.setText("Start Morse")
		b1.move(50,40)
		b1.clicked.connect(self.func)			# connect the button to the func function
	
	def func(self):				# read the input from the user and loop over each character to call the right letter function
		input = self.textbox.text()			
		for item in input:
			if (item == "A"):			# for example if character is A then the letterA function is called
				self.letterA()
				
			if (item == "B"):
				self.letterB()
				
			if (item == "C"):
				self.letterC()
				
			if (item == "D"):
				self.letterD()
				
			if (item == "E"):
				self.letterE()
				
			if (item == "F"):
				self.letterF()
				
			if (item == "G"):
				self.letterG()
				
			if (item == "H"):
				self.letterH()
				
			if (item == "I"):
				self.letterI()
				
			if (item == "J"):
				self.letterJ()
				
			if (item == "K"):
				self.letterK()
				
			if (item == "L"):
				self.letterL()
				
			if (item == "M"):
				self.letterM()
				
			if (item == "N"):
				self.letterN()
				
			if (item == "O"):
				self.letterO()
				
			if (item == "P"):
				self.letterP()
				
			if (item == "Q"):
				self.letterQ()
				
			if (item == "R"):
				self.letterR()
				
			if (item == "S"):
				self.letterS()
				
			if (item == "T"):
				self.letterT()
				
			if (item == "U"):
				self.letterU()
				
			if (item == "V"):
				self.letterV()
			
			if (item == "W"):
				self.letterW()
				
			if (item == "X"):
				self.letterX()
				
			if (item == "Y"):
				self.letterY()
				
			if (item == "Z"):
				self.letterZ()
		self.textbox.setText("")			# clears the text box
		QMessageBox.question(self,'Message', "Fnished ",QMessageBox.Ok, QMessageBox.Ok)		# show a message that morsing is finished
		
				
				
				
	# These are all the letter functions that blink the LED 
	def letterA(self):
		
		GPIO.output(40,GPIO.HIGH)		# set LED on 
		sleep(1)						#delay for 1 second
		GPIO.output(40,GPIO.LOW)		#set LED off
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(2)
				
	def letterB(self):
		
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(2)
		
	
	def letterC(self):
		
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(2)
		
	def letterD(self):
		
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(2)
	
	def letterE(self):
		
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(2)
		
	def letterF(self):
		
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(2)
		
		
	def letterG(self):
		
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(2)
	
	def letterH(self):
		
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(2)
		
	def letterI(self):
		
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(2)
	
	def letterJ(self):
		
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(2)
		
	def letterK(self):
		
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(2)
		
	def letterL(self):
		
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(2)
		
	def letterM(self):
		
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(2)
		
	def letterN(self):
		
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(2)
		
	def letterO(self):
		
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(2)
		
	def letterP(self):
		
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(2)
		
	def letterQ(self):
		
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(2)
		
	def letterR(self):
		
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(2)
		
	def letterS(self):
		
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(2)
		
	def letterT(self):
		
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(2)
		
	def letterU(self):
		
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(2)
		
	def letterV(self):
		
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(2)
		
	def letterW(self):
		
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(2)
		
	def letterX(self):
		
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(2)
		
	def letterY(self):
		
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(2)
		
	def letterZ(self):
		
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(3)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(1)
		GPIO.output(40,GPIO.HIGH)
		sleep(1)
		GPIO.output(40,GPIO.LOW)
		sleep(2)
		
		


		
		
		
	


	
	
	
	
app = QApplication(sys.argv)			# create an object of app	
window = window()						# create an object of window
try:
	window.show()						# show the window
	sys.exit(app.exec())				#exit
except:
	GPIO.cleanup()						#clean the GPIO pins
	

