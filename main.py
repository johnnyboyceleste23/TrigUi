import tkinter as tk
from tkinter import ttk
import math

BG = "#f8f4e3"

def deg_to_rad(deg: float) -> float:
    return deg * math.pi / 180

def get_degrees():
    try:
        return float(entry1.get())
    except ValueError:
        output_label.config(text="Please enter a valid number.")
        return None

def do_sin():
    deg = get_degrees()
    if deg is None:
        return
    result = math.sin(deg_to_rad(deg))
    output_label.config(text=f"sin({deg}°) = {result}")

def do_cos():
    deg = get_degrees()
    if deg is None:
        return
    result = math.cos(deg_to_rad(deg))
    output_label.config(text=f"cos({deg}°) = {result}")

def do_tan():
    deg = get_degrees()
    if deg is None:
        return
    result = math.tan(deg_to_rad(deg))
    output_label.config(text=f"tan({deg}°) = {result}")


root = tk.Tk()
root.title("Trig")
root.geometry("520x330")
root.configure(bg=BG)

style = ttk.Style()
style.theme_use("clam")

# Make frames/labels match beige background
style.configure("TFrame", background=BG)
style.configure("Header.TLabel", font=("Segoe UI", 22, "bold"), foreground="#5a4a2a", background=BG)
style.configure("Input.TLabel", font=("Segoe UI", 12), foreground="#6b5b3a", background=BG)
style.configure("Output.TLabel", font=("Segoe UI", 12, "bold"), foreground="#5a4a2a", background=BG)

# Buttons
style.configure(
    "Trig.TButton",
    font=("Segoe UI", 12, "bold"),
    padding=10,
    background="#d6c7a1",
    foreground="#2f2f2f"
)
style.map("Trig.TButton", background=[("active", "#c5b68f")])

# Main container
main = ttk.Frame(root, padding=20)
main.pack(fill="both", expand=True)

# Make 3 columns behave nicely
main.columnconfigure(0, weight=1)
main.columnconfigure(1, weight=1)
main.columnconfigure(2, weight=1)

# Title
ttk.Label(main, text="Trigonometry Functions", style="Header.TLabel").grid(
    row=0, column=0, columnspan=3, pady=(0, 15)
)

# Button row
ttk.Button(main, text="sin", style="Trig.TButton", command=do_sin).grid(row=1, column=0, padx=10, pady=5, sticky="ew")
ttk.Button(main, text="cos", style="Trig.TButton", command=do_cos).grid(row=1, column=1, padx=10, pady=5, sticky="ew")
ttk.Button(main, text="tan", style="Trig.TButton", command=do_tan).grid(row=1, column=2, padx=10, pady=5, sticky="ew")

# Input label + entry (center column)
ttk.Label(main, text="Enter Number", style="Input.TLabel").grid(row=2, column=1, pady=(15, 5))
entry1 = ttk.Entry(main, justify="center")
entry1.grid(row=3, column=1, ipady=3, sticky="ew")

# Output
output_label = ttk.Label(main, text="", style="Output.TLabel")
output_label.grid(row=4, column=0, columnspan=3, pady=(18, 0))

root.mainloop()