# gui.py
import tkinter as tk
from tkinter import Entry, Label, Button, messagebox
from tkinter import filedialog
from tkinter import ttk
from main import download_instagram_post

def browse_target_folder(entry):
    folder_path = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, folder_path)

def download_button_clicked(entry_url, entry_folder, progress_bar):
    url = entry_url.get()
    target_folder = entry_folder.get()
    download_instagram_post(url, target_folder, progress_bar)

def create_gui():
    root = tk.Tk()
    root.title("Instagram Downloader")

    # URL Entry
    label_url = Label(root, text="Instagram Post URL:")
    label_url.pack()
    entry_url = Entry(root, width=40)
    entry_url.pack()

    # Target Folder Entry
    label_folder = Label(root, text="Target Folder:")
    label_folder.pack()
    entry_folder = Entry(root, width=40)
    entry_folder.pack()

    # Browse Button
    browse_button = Button(root, text="Browse", command=lambda: browse_target_folder(entry_folder))
    browse_button.pack()

    # Progress Bar
    progress_bar = ttk.Progressbar(root, mode="determinate", length=200)
    progress_bar.pack()

    # Download Button
    download_button = Button(root, text="Download", command=lambda: download_button_clicked(entry_url, entry_folder, progress_bar))
    download_button.pack()

    return root

