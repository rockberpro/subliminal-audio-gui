import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog

def center_window(window, width=300, height=200):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    window.geometry(f'{width}x{height}+{x}+{y}')

def select_wav_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("WAV files", "*.wav")],
        title="Selecione um arquivo WAV"
    )
    if file_path:
        print(f"Selected audio file: {file_path}")

root = ttk.Window(title="Subliminal Audio Converter", size=(400, 120))
center_window(root, 400, 120)

encode_btn = ttk.Button(
    root, text="Select file", bootstyle=INFO, command=select_wav_file
)
encode_btn.pack(side=LEFT, padx=20, pady=30, expand=True)

root.mainloop()

