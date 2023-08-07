import os
import requests
import tkinter as tk
from tkinter import filedialog

def download_image(url, save_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

def browse_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
    entry_path.delete(0, tk.END)
    entry_path.insert(0, file_path)

def download():
    url = entry_url.get()
    save_path = entry_path.get()
    if url and save_path:
        download_image(url, save_path)
        status_label.config(text="Image downloaded successfully.")
    else:
        status_label.config(text="Please provide URL and save path.")

# Create the main window
root = tk.Tk()
root.title("Image Downloader")

# Create and arrange widgets
label_url = tk.Label(root, text="Image URL:")
label_url.pack()
entry_url = tk.Entry(root, width=50)
entry_url.pack()

label_path = tk.Label(root, text="Please Save Path:")
label_path.pack()
entry_path = tk.Entry(root, width=50)
entry_path.pack()
button_browse = tk.Button(root, text="Browse", command=browse_file)
button_browse.pack()

button_download = tk.Button(root, text="Download Image", command=download, fg="green")
button_download.pack()

status_label = tk.Label(root, text="", fg="purple")
status_label.pack()

# Start the main event loop
root.mainloop()
