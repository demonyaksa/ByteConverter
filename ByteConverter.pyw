import tkinter as tk

def convert_units():
    try:
        byte = float(byte_entry.get())
        mb = byte / (1024 ** 2)
        gb = byte / (1024 ** 3)
        byte_var.set("{:.2f}".format(byte))
        mb_var.set("{:.2f}".format(mb))
        gb_var.set("{:.2f}".format(gb))
    except ValueError:
        byte_var.set("Invalid input")
        mb_var.set("Invalid input")
        gb_var.set("Invalid input")

window = tk.Tk()
window.title("Byte Converter")

# Set window size and position
window_width = 300
window_height = 200
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width - window_width) / 2)
y = int((screen_height - window_height) / 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create byte entry
byte_var = tk.StringVar()
byte_label = tk.Label(window, text="Byte", font=("Arial", 14))
byte_label.grid(row=0, column=0, pady=10)
byte_entry = tk.Entry(window, textvariable=byte_var, font=("Arial", 14))
byte_entry.grid(row=0, column=1, pady=10)

# Create MB entry
mb_var = tk.StringVar()
mb_label = tk.Label(window, text="MB", font=("Arial", 14))
mb_label.grid(row=1, column=0, pady=10)
mb_entry = tk.Entry(window, textvariable=mb_var, state="readonly", font=("Arial", 14))
mb_entry.grid(row=1, column=1, pady=10)

# Create GB entry
gb_var = tk.StringVar()
gb_label = tk.Label(window, text="GB", font=("Arial", 14))
gb_label.grid(row=2, column=0, pady=10)
gb_entry = tk.Entry(window, textvariable=gb_var, state="readonly", font=("Arial", 14))
gb_entry.grid(row=2, column=1, pady=10)

# Create convert button
convert_button = tk.Button(window, text="Convert", command=convert_units, font=("Arial", 14))
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

window.mainloop()
