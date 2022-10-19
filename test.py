import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
# file_path = filedialog.askopenfilename()
file_path = filedialog.askdirectory()

new_file = input("Name file\n")
open_file = open(f"{file_path}\%s.py" % new_file, 'w')