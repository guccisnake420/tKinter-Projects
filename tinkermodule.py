import tkinter
import tkinter.messagebox
class milesGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.prompt1_label = tkinter.Label(self.top_frame, text ='Enter number of gallons of gas the car holds')
        self.gal_entry = tkinter.Entry(self.top_frame, width= 10)
        self.prompt_label = tkinter.Label(self.mid_frame, text ='Enter number of miles car can drive on full tank')
        self.miles_entry = tkinter.Entry(self.mid_frame, width= 10)
        self.prompt1_label.pack(side ='left')
        self.prompt_label.pack(side='left')
        self.gal_entry.pack(side = 'left')
        self.miles_entry.pack(side = 'left')
        self.Calculatempg_button = tkinter.Button(self.bottom_frame, text= 'Calculate MPG', command = self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command = self.main_window.destroy)
        self.Calculatempg_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()
    def convert(self):
        miles = float(self.miles_entry.get())
        gallons = float(self.gal_entry.get())
        milespergallon = miles / gallons
        tkinter.messagebox.showinfo('Results', 'The car has ' + str(milespergallon) + ' MPG')
if __name__ == '__main__':
    mpg_conv = milesGUI()

    
 