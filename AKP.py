import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)

class AKP():

   def __init__(self, the_window):

       self.the_window = the_window
       self.the_window.geometry("800x700")
       self.the_window.resizable(False, False)

       self.Main_Frame = tk.Frame(self.the_window)
       self.Main_Frame.grid()

       self.my_canvas = tk.Canvas(self.Main_Frame, width=1000, height=1000, scrollregion=(0,0, 600,1200), relief="sunk")
       self.my_canvas.grid(row=1, column=0)
       self.scrollY = tk.Scrollbar(self.Main_Frame, orient=tk.VERTICAL,
                                 command=self.my_canvas.yview)
       self.scrollY.grid(row=1, column=1, sticky=tk.NS)
       self.my_canvas["yscrollcommand"] = self.scrollY.set

       self.display_output()

    def display_output(self):

        self.fig = plt.Figure(figsize=(7, 9), dpi=100, facecolor="#D6EAF8")
        self.ax = self.fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.my_canvas)
        self.canvas.get_tk_widget().grid(row=0, column=0)

        var_text_1 = "Hello World"

        self.ax.text(-0.1, 1.03, var_text_1, fontsize=12, fontweight="roman", fontfamily="fantasy")

if __name__ == "__main__":
    my_window = tk.Tk()
    application = AKP(my_window)
    my_window.mainloop()
