import tkinter as tk

# --- Functions ---
def press(key):
    if key == "=":
        try:
            expression = entry.get()
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif key == "C":
        entry.delete(0, tk.END)
    elif key == "←":
        entry.delete(len(entry.get()) - 1, tk.END)
    else:
        entry.insert(tk.END, key)

# Keyboard bindings
def key_event(event):
    key = event.keysym
    if key in "0123456789":
        press(key)
    elif key in ["plus", "KP_Add"]:
        press("+")
    elif key in ["minus", "KP_Subtract"]:
        press("-")
    elif key in ["asterisk", "KP_Multiply"]:
        press("*")
    elif key in ["slash", "KP_Divide"]:
        press("/")
    elif key in ["Return", "KP_Enter"]:
        press("=")
    elif key == "BackSpace":
        press("←")
    elif key.upper() == "C":
        press("C")

# --- UI Setup ---
root = tk.Tk()
root.title("Modern Calculator 🧮")
root.geometry("350x500")
root.config(bg="#1e1e1e")
root.resizable(False, False)

# --- Entry field ---
entry = tk.Entry(root, font=("Consolas", 24), bg="#2d2d2d", fg="white",
                 insertbackground="white", borderwidth=0, justify='right')
entry.pack(fill="x", ipadx=8, ipady=20, padx=10, pady=15)

# --- Button design ---
btn_bg = "#333333"
btn_hover = "#505050"
btn_active = "#606060"
btn_fg = "white"

def make_button(parent, text, row, col, colspan=1, command=None, bg=btn_bg):
    def on_enter(e): btn.config(bg=btn_hover)
    def on_leave(e): btn.config(bg=bg)
    btn = tk.Button(parent, text=text, font=("Consolas", 18), fg=btn_fg,
                    bg=bg, activebackground=btn_active, activeforeground="white",
                    bd=0, relief="flat", command=command)
    btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=4, pady=4)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# --- Button frame ---
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(expand=True, fill="both")

buttons = [
    ["C", "←", "/", "*"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", ".", "", ""]
]

for r, row in enumerate(buttons):
    for c, text in enumerate(row):
        if text:
            make_button(frame, text, r, c, command=lambda t=text: press(t))

# --- Make buttons expand equally ---
for i in range(5):
    frame.rowconfigure(i, weight=1)
for i in range(4):
    frame.columnconfigure(i, weight=1)

# --- Bind keyboard ---
root.bind("<Key>", key_event)

root.mainloop()
