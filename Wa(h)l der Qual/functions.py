import json, os, sys
import tkinter as tk
from random import randint, choice
from tkinter import ttk
from PIL import Image, ImageTk

# Bestimmen des absoluten Pfads von Ressourcen
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Laden der Listen aus der responeses.json
with open(resource_path('responses.json'), 'r', encoding='utf-8') as json_file:
    responses_data = json.load(json_file)

# Extrahieren der Listen aus der geladenen responeses.json
random_responses = responses_data.get("random_responses", [])
random_dumbass = responses_data.get("random_dumbass", [])
special_responses = responses_data.get("special_responses", [])

# Benutzereingabe
def user_input(entry, result_label, image_label):
    try:
        max_value = int(entry.get())
        if max_value == 1 or max_value == 0:
            result_label.config(text=choice(random_dumbass))
        else:
            if randint(1, 100) <= 10:
                result_label.config(text=choice(special_responses))
            else:
                choice_value = generate_random(max_value)
                result_label.config(text=choice(random_responses) + str(choice_value))
    except ValueError:
        result_label.config(text=choice(random_dumbass))

# Zufallsgenerator
def generate_random(max_value):
    min_value = 1
    choice = randint(min_value, max_value)
    return choice

# Funktion, die aufgerufen wird, wenn die Enter-Taste gedrückt wird
def on_enter_pressed(event, entry, result_label, image_label):
    user_input(entry, result_label, image_label)

# Überprüfungsfunktion für das input_entry
def on_validate(P):
    return P == "" or (P.isdigit() and len(P) <= 3)

# Aufbau der GUI
def create_gui(root):
    window_width = 300
    window_height = 418

    monitor_center_x = root.winfo_screenwidth() / 2 - (window_width / 2)
    monitor_center_y = root.winfo_screenheight() / 2 - (window_height / 2)

    root.geometry("%dx%d+%d+%d" % (window_width, window_height, monitor_center_x, monitor_center_y))
    root.resizable(width=False, height=False)
    root.title("Wa(h)l der Qual")
    root.iconbitmap(resource_path("media\\whale_icon.ico"))

    input_label = ttk.Label(root, text="Anzahl der Optionen:")
    input_label.grid(row=0, column=0, pady=10)

    validate_cmd = root.register(on_validate)

    input_entry = ttk.Entry(root, validate="key", validatecommand=(validate_cmd, '%P'))
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
