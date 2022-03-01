#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#------------------------------------------------------------------------------------------------------------------------------
# Created By  : Annah N Mutaya
# Created Date: 2/25/2022
# -----------------------------------------------------------------------------------------------------------------------------
# This file contains a simple graphics encryption GUI that takes in a message and a pad as inputs and returns the encrypted or decrypted message
# -----------------------------------------------------------------------------------------------------------------------------

from graphics import *
from Button import Button
from EasyRectangle import EasyRectangle
from cipher import *
import calculator 

class Encrypt:
    """Class that draws an encryptor GUI by taking a message and a pad, and displaying the encrypted and/or decrypted message"""
    def __init__(self):
        # function to initialize the encryptor buttons and inputs
        self.encryptrect = EasyRectangle(300,300,400,400)  # draw the calculator rectangle
        self.encryptrect.setFill("sky blue")
        
        self.label1 = Text(Point(300, 130), "Input message to encrypt/decrypt")
        self.msg = Entry(Point(300,150), 50)
        self.msg.setFill("orange")
        self.label2 = Text(Point(300, 190), "Input pad")
        self.pad_input = Entry(Point(300, 210), 50)
        self.pad_input.setFill("orange")
        self.pad_button = Button(300,370,300,30, "yellow","Encrypt by generating pad")

        self.encrypt_button = Button(220,320,120,25, "light blue","Encrypt")
        self.decrypt_button = Button(360,320,120,25, "light blue","Decrypt")
        self.quit = Button(490,110,15,15, "Red", "x")
        self.clear_button = Button(300, 420, 140, 30, "light green", "Clear")

        self.result = EasyRectangle(290,270,260,30)  
        self.result.setFill("light yellow")
        self.result_text = Text(Point(290,270), "")
        self.toggle = Button(300,480,140,30, "pink", "Basic mode")  # button to switch between basic and encryption mode
        self.toggle_num = 1

    def draw(self, win):
        # function that draws the buttons and inputs to the screen. It takes in the win and draws the objects to it
        self.encryptrect.draw(win)
        self.msg.draw(win)
        self.pad_button.draw(win)
        self.result.draw(win)
        self.quit.draw(win)
        self.clear_button.draw(win)
        self.result_text.draw(win)
        self.toggle.draw(win)
        self.encrypt_button.draw(win)
        self.decrypt_button.draw(win)
        self.pad_input.draw(win)
        self.label1.draw(win)
        self.label2.draw(win)

    def get_input_value(self, msg):
        # function to get the input values from the entry boxes. Also issues a warning if a user does not enter a valid number
        try:
            n = str(msg.getText())
        except:
            n = None
            self.result_text.setText("Enter a valid string")
        return n

    def display_result(self, result):
        # function to display the results to the screen. It takes the result and displays it in the window
        self.result_text.setText(str(result))

    def clear(self):
        # function to clear the boxes
        self.pad_input.setText('')
        self.msg.setText('')
        self.result_text.setText('')

    def run(self, win):
        # function that runs the encryptor 
        while True:
            p = win.getMouse()

            entry = self.get_input_value(self.msg)  # get those entry texts
            pad = self.get_input_value(self.pad_input)
            if self.quit.clicked(p):
                break
            elif self.clear_button.clicked(p):
                self.clear() 
            elif self.toggle.clicked(p):   # run basic calculator if toggle is clicked
                self.toggle_num = 0
                win.close() 
                win = GraphWin("Calculator", 600, 600)  
                win.setBackground("white")
                calculate = calculator.Calculator()
                calculate.draw(win)
                calculate.calculate(win)  
            else:
                if self.encrypt_button.clicked(p) and entry != None and pad != None:  # if user inputs both message and pad
                    encyrpted_message = encipher(entry, pad)
                    save_file("encrypted-message.txt", encyrpted_message)  # save the encrypted message to a file called encrypted-message.txt
                    self.display_result("Your message is saved to encrypted-message.txt") 
                elif entry != None and self.pad_button.clicked(p): # user inputs message and clicks generate pad
                    pad = generatePad(len(entry))
                    encyrpted_message = encipher(entry, pad)
                    save_file("encrypted-message.txt", encyrpted_message)
                    self.display_result("Your message is saved to encrypted-message.txt") 
                elif self.decrypt_button.clicked(p):
                    decrypted_message = decipher(entry, pad)
                    save_file("decrypted-message.txt", decrypted_message)
                    self.display_result("Your message is saved to decrypted-message.txt") 
    
if __name__ == '__main__':
    encrypt = Encrypt()   # instanciate Encrypt
    calc = calculator.Calculator()  
    if  encrypt.toggle_num == 0:   # switch to basic calculator mode
        win = GraphWin("Calculator", 600, 600)  
        win.setBackground("white")
        calc.draw(win)
        calc.calculate(win)
    else:                    # else just run the current encrypt mode
        win = GraphWin("Encipher", 600, 600)  
        win.setBackground("white")
        encrypt.draw(win)
        encrypt.run(win)         

           




