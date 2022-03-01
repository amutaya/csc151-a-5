#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#------------------------------------------------------------------------------------------------------------------------------
# Created By  : Annah N Mutaya
# Created Date: 2/25/2022
# -----------------------------------------------------------------------------------------------------------------------------
# This file contains a simple graphics calculator GUI that takes in 2 inputs and an operation and returns the result
# -----------------------------------------------------------------------------------------------------------------------------

from graphics import *
from Button import Button
from EasyRectangle import EasyRectangle
from cipher import *
import encryptor

class Calculator:
    """Class that draws a calculator GUI and takes in 2 inputs and an operation, calculates and displays the result"""
    def __init__(self):
        # function to initialize the calculator buttons and inputs
        self.calcrect = EasyRectangle(300,300,400,400)  # draw the calculator rectangle
        self.calcrect.setFill("sky blue")
        
        self.num2 = Entry(Point(370,210), 10)
        self.num2.setFill("gold")
        self.num2.setText("0")
        self.num1 = Entry(Point(240, 210), 10)
        self.num1.setFill("gold")
        self.num1.setText("0")
        self.add = Button(240,280,20,20, "orange","+")
        self.sub = Button(280,280,20,20, "orange","-")
        self.mult = Button(320,280,20,20, "orange","*")
        self.div = Button(360,280,20,20, "orange","/")

        self.quit = Button(490,110,15,15, "Red", "x")
        self.clear_button = Button(300, 400, 70, 30, "light green", "Clear")

        self.result = EasyRectangle(300,340,180,30)  # result button
        self.result.setFill("light yellow")
        self.result_text = Text(Point(310,340), "")
        self.toggle = Button(300,460,140,40, "pink", "Encrypt mode")
        self.toggle_num = 0

    def draw(self, win):
        # function that draws the buttons and inputs to the screen. It takes in the win and draws the objects to it
        self.calcrect.draw(win)
        self.num1.draw(win)
        self.num2.draw(win)
        self.add.draw(win)
        self.sub.draw(win)
        self.mult.draw(win)
        self.div.draw(win)
        self.result.draw(win)
        self.quit.draw(win)
        self.clear_button.draw(win)
        self.result_text.draw(win)
        self.toggle.draw(win)

    def get_input_value(self, num):
        # function to get the input values from the entry boxes. Also issues a warning if a user does not enter a valid number
        try:
            n = float(num.getText())
        except:
            n = None
            self.result_text.setText("Please eneter a valid number")
        return n

    def display_result(self, result):
        # function to display the results to the screen. It takes the result and displays it in the window
        self.result_text.setText(str(result))

    def clear(self):
        # function to clear the boxes
        self.num1.setText('')
        self.num2.setText('')
        self.result_text.setText('')
    
    def calculate(self, win):
        # function that runs the calculator. 
        while True:
            p = win.getMouse()

            entry1 = self.get_input_value(self.num1)  # get those entry values
            entry2 = self.get_input_value(self.num2)
            
            if self.quit.clicked(p):
                break
            elif self.clear_button.clicked(p):
                self.clear()
            elif self.toggle.clicked(p):
                self.toggle_num = 1
                win.close()
                win = GraphWin("Encipher", 600, 600)  
                win.setBackground("blue")
                encrypt = encryptor.Encrypt()
                encrypt.draw(win)
                encrypt.run(win) 
            else:
                entry1 != None and entry2 != None
                if self.add.clicked(p):
                    self.display_result(entry1 + entry2)
                elif self.sub.clicked(p):
                    self.display_result(entry1 - entry2)
                elif self.mult.clicked(p):
                    self.display_result(entry1 * entry2)
                elif self.div.clicked(p):
                    if entry2 != 0:
                        self.display_result(entry1 / entry2)
                    else:
                        self.display_result("Invalid operation: division by 0")   
  
if __name__ == '__main__':
    win = GraphWin("Calculator", 600, 600)  
    win.setBackground("white")
    encrypt = encryptor.Encrypt()
    calc = Calculator()  

    if  calc.toggle_num == 0:    
        calc.draw(win)
        calc.calculate(win)   # runs calculate()
    else:   
        encrypt.draw(win)
        encrypt.run(win)         