import tkinter as tk

window = tk.Tk()
name = "joven aberia"
section = "BSIT 2B"
window.title(f"OOP LA28 {name}")
window.geometry("500x500")
window.configure(bg="black")
how = tk.Label(window, text=f"OOP LA29 {name} {section}")
how.grid(row=000, column=000, padx=250, pady=250)

window.mainloop()
