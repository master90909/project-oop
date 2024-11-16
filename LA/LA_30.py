import tkinter as tk

def print_anime():
    anime_title = "One Punch Man"
    print(f"My favorite anime is {anime_title}")

window = tk.Tk()
window.title("Anime print")
window.geometry("300x400")

button = tk.Button(window, text="Run", command=print_anime)
button.pack(pady=20)

window.mainloop()
