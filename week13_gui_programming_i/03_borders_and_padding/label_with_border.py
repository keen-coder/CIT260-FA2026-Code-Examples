# This program uses the side='left' argument with
# the pack method to change the layout of the widgets.

import tkinter as tk

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tk.Tk()

        # Create two Label widget.
        self.label1 = tk.Label(self.main_window, \
                                    text='Hello World!',
                                    borderwidth=5,
                                    relief='sunken')
        
        label2_config_dict = {'text': 'Hello World', 'borderwidth': 5, 'relief':'raised'}

        self.label2 = tk.Label(self.main_window, label2_config_dict)

        self.label3 = tk.Label(self.main_window)
        
        self.label3['text'] = 'This is label 3'
        self.label3['borderwidth'] = 10
        self.label3['relief'] = 'solid'
        self.label3['background'] = 'green'

        # Call both Label widgets' pack method.
        self.label1.pack(side='left')
        self.label2.pack(side='right')
        self.label3.pack(side='bottom')

        # Enter the tkinter main loop.
        tk.mainloop()

# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()