from random import randint
import os
import sys

# Benutzereingabe
def user_input(entry, result_label, image_label):
    try:
        max_value = int(entry.get())
        if max_value == 1 or max_value == 0:
            result_label.config(text="Der Wal lacht dich aus")
        else:
            choice = generate_random(max_value)
            result_label.config(text="Der Wal hat entschieden: " + str(choice))
    except ValueError:
        result_label.config(text="Der Wal sieht dich skeptisch an..")

# Zufallsgenerator
def generate_random(max_value):
    min_value = 1
    choice = randint(min_value, max_value)
    return choice

# Bestimmen des absoluten Pfads von Ressourcen
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)