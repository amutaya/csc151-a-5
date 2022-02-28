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

class Calculator:
    def __init__(self):
        self.calcrect = EasyRectangle(300,300,400,400)  # draw the calculator rectangle
        self.calcrect.setFill("light grey")
        
        self.num2 = Entry(Point(370,210), 10)
        self.num2.setText("0")
        self.num1 = Entry(Point(240, 210), 10)
        self.num1.setText("0")
        self.add = Button(240,280,20,20, "light blue","+")
        self.sub = Button(280,280,20,20, "light blue","-")
        self.mult = Button(320,280,20,20, "light blue","*")
        self.div = Button(360,280,20,20, "light blue","/")

        self.quit = Button(490,110,15,15, "Red", "x")
        self.clear_button = Button(300, 400, 70, 30, "light green", "Clear")

        self.result = EasyRectangle(300,340,180,30)
        self.result.setFill("light yellow")
        self.result_text = Text(Point(310,340), "")

   

    def draw(self, win):
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

    def get_input_value(self, num):
        try:
            n = float(num.getText())
        except:
            n = None
            self.result_text.setText("Please eneter a valid number")
        return n

    def display_result(self, result):
        self.result_text.setText(str(result))

    def clear(self):
        self.num1.setText('')
        self.num2.setText('')
        self.result_text.setText('')


    def calculate(self, win):
        while True:
            p = win.getMouse()

            entry1 = self.get_input_value(self.num1)
            entry2 = self.get_input_value(self.num2)
            
            if self.quit.clicked(p):
                break
            elif self.clear_button.clicked(p):
                self.clear()
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
                
            

def main():
    win = GraphWin("Calculator", 600, 600)
    win.setBackground("white")

    calc = Calculator()
    calc.draw(win)
    calc.calculate(win)

    win.close()

main()