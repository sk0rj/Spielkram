from tkinter import ttk
from PIL import Image, ImageTk
from functions import user_input, resource_path

# Funktion, die aufgerufen wird, wenn die Enter-Taste gedrückt wird
def on_enter_pressed(event, entry, result_label, image_label):
    user_input(entry, result_label, image_label)

# Aufbau der GUI
def create_gui(root):
    input_label = ttk.Label(root, text="Anzahl der Optionen:")
    input_label.grid(row=0, column=0, pady=10)

    input_entry = ttk.Entry(root)
    input_entry.grid(row=0, column=1, pady=10)

    button = ttk.Button(root, text="Quäl den Wal", command=lambda: user_input(input_entry, result_label, image_label))
    button.grid(row=1, column=0, columnspan=2, pady=10)

    result_label = ttk.Label(root, text="")
    result_label.grid(row=2, column=0, columnspan=2, pady=10)

    image_label = ttk.Label(root)
    image_label.grid(row=3, column=0, columnspan=2, pady=10)

    image = Image.open(resource_path("media/whale.png"))
    image.thumbnail((300, 300))
    photo = ImageTk.PhotoImage(image)

    image_label.config(image=photo)
    image_label.image = photo

    input_entry.focus_set()

    input_entry.bind("<Return>", lambda event: on_enter_pressed(event, input_entry, result_label, image_label))