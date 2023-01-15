import pyspeedtest
from tkinter import *

from itertools import count
import statistics as st
import math as mt

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Wifi Test Manager")
        self.geometry("1500x850")
        self.create_widgets()
    
    def create_widgets(self):
        # create canvas
        self.canvas = FigureCanvasTkAgg(plt.gcf(), master=self)

        # create quit button
        self.button_quit = Button(self, text="Quitter", bg='red', fg='white', height=1, width=10, font=('Calibri', 20), command=self.quit)
        self.button_quit.pack(side=BOTTOM)

        # create toolbar
        self.toolbar = NavigationToolbar2Tk(self.canvas, self, pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.pack(side=BOTTOM, fill=X)

        # place canvas
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

# x axis
x_vals = []
# value for first graph
y_vals = []
y_mean = []
# values for second graph
y_vals2 = []
y_mean2 = []

index = count()
index2 = count()

def refresh(i):
    # Get all axes of figure
    ax1, ax2 = plt.gcf().get_axes()
    
    # Clear current data
    ax1.cla()
    ax2.cla()

    # Generate values
    test = pyspeedtest.SpeedTest("www.google.com")
    down = test.download()
    x_vals.append(next(index))
    y_vals.append(test.ping())
    if len(str(mt.floor(down))) < 3:
        y_vals2.append(down)
        ax2.set_ylabel("b/s")
    if len(str(mt.floor(down))) >= 3 and len(str(mt.floor(down))) < 6:
        y_vals2.append(down/1000)
        ax2.set_ylabel("Kb/s")
    if len(str(mt.floor(down))) >= 6 and len(str(mt.floor(down))) < 9:
        y_vals2.append(down/10000)
        ax2.set_ylabel("Mb/s")
    if len(str(mt.floor(down))) >= 9:
        y_vals2.append(down/100000)
        ax2.set_ylabel("Gb/s")
    
    y_mean.append(st.mean(y_vals))
    y_mean2.append(st.mean(y_vals2))

    # Plot new data
    ax1.plot(x_vals, y_vals, label='ping')
    ax1.plot(x_vals, y_mean, "r--", label='ping moyen')
    ax2.plot(x_vals, y_vals2, label='débit descendant')
    ax2.plot(x_vals, y_mean2, "r--", label='débit descendant moyen')

    ax1.set_ylabel("Ping")
    ax2.set_xlabel("Temps passé [s]")

    ax1.legend()
    ax2.legend()
    

if __name__ == "__main__":

    app = App()

    plt.style.use('fivethirtyeight')
    plt.gcf().subplots(2, 1)

    ani = FuncAnimation(plt.gcf(), refresh, interval=1000, blit=False)

    app.mainloop()