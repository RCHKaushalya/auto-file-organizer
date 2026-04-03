import tkinter as tk
from tkinter import filedialog
from organizer import organize_files
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def select_folder():
    path = filedialog.askdirectory()
    if path:
        summary, unsorted_files = organize_files(path)

        report = '\n Summary of organized files:\n'
        for folder, count in summary.items():
            report += f"{folder}: {count} files\n"
        if unsorted_files:
            report += "\n Unsorted files:\n"
            for filename in unsorted_files:
                report += f" - {filename}\n"
        
        tk.messagebox.showinfo("Organization Report", report)

root = tk.Tk()
root.title("File Organizer")
root.geometry("400x200")
root.configure(bg="#f0f0f0")
root.iconbitmap(resource_path("app_icon.ico"))

label = tk.Label(root, text="Select a folder to organize", font=("Arial", 14), bg="#f0f0f0")
label.pack(pady=20)

button = tk.Button(root, text="Choose Folder", command=select_folder, bg='#4CAF50', fg='white', font=("Arial", 12))
button.pack(pady=10)

root.mainloop()
