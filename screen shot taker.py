import pyautogui
import tkinter as tk
from tkinter.filedialog import *

root = tk.Tk()
screenshottaker = tk.Canvas(root , width = 300 , height = 300)
screenshottaker.pack()

def takeScreenshot():
    myscreenshot = pyautogui.screenshot()
    save_path = asksaveasfilename()
    myscreenshot.save(save_path + "_screenshot.png")

mybtn = tk.Button(text = "Take Screenshot" , command = takeScreenshot , font = 10)
screenshottaker.create_window(150,150 , window = mybtn)



tk.mainloop()