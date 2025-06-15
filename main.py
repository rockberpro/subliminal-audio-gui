import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, StringVar

from decoder import decoder
from encoder import encoder

def center_window(window, width=300, height=200):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def inupt_wav_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("WAV files", "*.wav")],
        title="Select a WAV file"
    )
    if file_path:
        feedback_var.set(f"Selected file: {file_path.split('/')[-1]}")
    else:
        feedback_var.set("No file was selected.")

def encode():
    encoder.encode_audio()

def decode():
    decoder.decode_audio()

root = ttk.Window(title="Subliminal Audio Generator", size=(400, 120))
center_window(root, 400, 120)

feedback_var = StringVar()
feedback_label = ttk.Label(root, textvariable=feedback_var, bootstyle=SECONDARY)
feedback_label.pack(side=TOP, pady=(10, 0))

file_btn = ttk.Button(
    root, text="Input file", bootstyle=INFO, command=inupt_wav_file
)
file_btn.pack(side=LEFT, padx=20, pady=30, expand=True)

encode_btn = ttk.Button(
    root, text="Encode", bootstyle=SUCCESS, command=encode
)
encode_btn.pack(side=LEFT, padx=20, pady=30, expand=True)

decode_btn = ttk.Button(
    root, text="Decode", bootstyle=WARNING, command=decode
)
decode_btn.pack(side=LEFT, padx=20, pady=30, expand=True)

root.mainloop()