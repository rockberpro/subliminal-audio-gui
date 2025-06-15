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

def input_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("WAV files", "*.wav")],
        title="Select a WAV file"
    )
    if file_path:
        feedback_var.set(f"Source: {file_path.split('/')[-1]}")
    else:
        feedback_var.set("No input file was selected.")

def output_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".wav",
        filetypes=[("WAV files", "*.wav"), ("All files", "*.*")],
        title="Select destination filename"
    )
    if file_path:
        output_feedback_var.set(f"Destination: {file_path.split('/')[-1]}")
    else:
        output_feedback_var.set("No output destination selected.")

def encode():
    encoder.encode_audio()

def decode():
    decoder.decode_audio()

root = ttk.Window(title="Subliminal Audio Generator", size=(400, 210))  # Reduza a altura aqui
center_window(root, 400, 210)

# Container para seleção de arquivos
input_frame = ttk.Frame(root)
input_frame.pack(side=TOP, pady=(20, 0))

# Frame para input
input_btn_frame = ttk.Frame(input_frame)
input_btn_frame.grid(row=0, column=0, padx=(0, 10))
file_btn = ttk.Button(
    input_btn_frame, text="Input file", bootstyle=INFO, command=input_file
)
file_btn.pack(anchor="w")
feedback_var = StringVar()
feedback_label = ttk.Label(
    input_btn_frame, textvariable=feedback_var, bootstyle=SECONDARY, width=28
)
feedback_label.pack(anchor="w", pady=(5, 0))

# Frame para output
output_btn_frame = ttk.Frame(input_frame)
output_btn_frame.grid(row=0, column=1, padx=(10, 0))
output_btn = ttk.Button(
    output_btn_frame, text="Output file", bootstyle=SECONDARY, command=output_file
)
output_btn.pack(anchor="w")
output_feedback_var = StringVar()
output_feedback_label = ttk.Label(
    output_btn_frame, textvariable=output_feedback_var, bootstyle=SECONDARY, width=28
)
output_feedback_label.pack(anchor="w", pady=(5, 0))

# Separador visual
separator = ttk.Separator(root, orient="horizontal")
separator.pack(fill="x", pady=20)

# Container para botões de ação
action_frame = ttk.Frame(root)
action_frame.pack(side=TOP, pady=(0, 0))  # Reduza ou remova o padding inferior

encode_btn = ttk.Button(
    action_frame, text="Encode", bootstyle=SUCCESS, command=encode
)
encode_btn.pack(side=LEFT, padx=20)

decode_btn = ttk.Button(
    action_frame, text="Decode", bootstyle=WARNING, command=decode
)
decode_btn.pack(side=LEFT, padx=20)

root.mainloop()