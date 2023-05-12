# -*- coding: utf-8 -*-
"""scientific_calculator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tafkLBO4cGXsI2DVplyjSfuZLCgmR8zM

# Group members 
- Muhammad Ali 
- Muhammad Haris
- Muhammad Mahad
- Mubarak Ghani
- Nabeel Afzal
"""

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import math

class CalculatorLayout(GridLayout):
    def __init__(self, **kwargs):
        super(CalculatorLayout, self).__init__(**kwargs)
        self.cols = 5  # Set the number of columns in the layout

        self.display = Label(text='0', font_size=40, size_hint_y=None, height=100)
        self.add_widget(self.display)

        # Create buttons for numbers 0-9
        for i in range(9, -1, -1):
            button = Button(text=str(i), font_size=40)
            button.bind(on_press=self.on_button_press)
            self.add_widget(button)

        # Create buttons for operators (+, -, *, /)
        operators = ['+', '-', '*', '/']
        for operator in operators:
            button = Button(text=operator, font_size=40)
            button.bind(on_press=self.on_button_press)
            self.add_widget(button)

        # Create equals button (=)
        equals_button = Button(text='=', font_size=40)
        equals_button.bind(on_press=self.calculate_result)
        self.add_widget(equals_button)

        # Create clear button (C)
        clear_button = Button(text='C', font_size=40)
        clear_button.bind(on_press=self.clear_display)
        self.add_widget(clear_button)

    def on_button_press(self, instance):
        if self.display.text == '0':
            self.display.text = instance.text
        else:
            self.display.text += instance.text

    def calculate_result(self, instance):
        try:
            result = eval(self.display.text)
            self.display.text = str(result)
        except:
            self.display.text = 'Error'

    def clear_display(self, instance):
        self.display.text = '0'

class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()

if __name__ == '__main__':
    CalculatorApp().run()

