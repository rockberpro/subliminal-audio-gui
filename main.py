import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import StringVar
import tkinter as tk

from decoder import decoder
from encoder import encoder

def center_window(window, width=300, height=200):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def input_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("WAV files", "*.wav")],
        title="Select source WAV file"
    )
    if file_path:
        input_file_path.set(file_path)
        input_feedback_var.set(f"{file_path.split('/')[-1]}")

def output_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".wav",
        filetypes=[("WAV files", "*.wav"), ("All files", "*.*")],
        title="Select destination WAV file"
    )
    if file_path:
        output_file_path.set(file_path)
        output_feedback_var.set(f"{file_path.split('/')[-1]}")

def encode():
    global input_file_path, output_file_path
    if not input_file_path.get():
        messagebox.showerror("Error", "Select input file before encoding")
    if not output_file_path.get():
        messagebox.showerror("Error", "Select output file before encoding")
    if not input_file_path.get() or not output_file_path.get():
        return
    encoder.encode_audio(input_file_path.get(), output_file_path.get())

def decode():
    global input_file_path, output_file_path
    if not input_file_path.get():
        messagebox.showerror("Error", "Select input file before decoding")
    if not output_file_path.get():
        messagebox.showerror("Error", "Select output file before decoding")
    if not input_file_path.get() or not output_file_path.get():
        return
    decoder.decode_audio(input_file_path.get(), output_file_path.get())

root = tk.Tk()
root.iconbitmap('./img/radar.ico')
root.title("Subliminal Audio Generator")
center_window(root, 400, 210)

input_file_path = StringVar()
output_file_path = StringVar()

# Container for input and output file selection
input_frame = ttk.Frame(root)
input_frame.pack(side=TOP, pady=(20, 0))

# Input file
file_btn = ttk.Button(
    input_frame, text="Input file", bootstyle=INFO, command=input_file, width=15
)
file_btn.grid(row=0, column=0, sticky="w", padx=(40, 10), pady=(0, 5))
input_feedback_var = StringVar()
input_feedback_label = ttk.Label(
    input_frame, textvariable=input_feedback_var, bootstyle=SECONDARY, width=32, anchor="w"
)
input_feedback_label.grid(row=0, column=1, sticky="w", padx=(0, 40), pady=(0, 5))

# Output file
output_btn = ttk.Button(
    input_frame, text="Output file", bootstyle=INFO, command=output_file, width=15
)
output_btn.grid(row=1, column=0, sticky="w", padx=(40, 10), pady=(0, 5))
output_feedback_var = StringVar()
output_feedback_label = ttk.Label(
    input_frame, textvariable=output_feedback_var, bootstyle=SECONDARY, width=32, anchor="w"
)
output_feedback_label.grid(row=1, column=1, sticky="w", padx=(0, 40), pady=(0, 5))

# Horizontal separator
separator = ttk.Separator(root, orient="horizontal")
separator.pack(fill="x", pady=20)

# Container for action buttons
action_frame = ttk.Frame(root)
action_frame.pack(side=TOP, pady=(0, 0))

encode_btn = ttk.Button(
    action_frame, text="Encode", bootstyle=SUCCESS, command=encode
)
encode_btn.pack(side=LEFT, padx=20)

decode_btn = ttk.Button(
    action_frame, text="Decode", bootstyle=WARNING, command=decode
)
decode_btn.pack(side=LEFT, padx=20)

root.mainloop()