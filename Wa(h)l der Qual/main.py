from tkinter import Tk
from functions import create_gui

# Starten der Anwendung
def torment_the_whale():

    root = Tk()

    create_gui(root)

    root.mainloop()

if __name__ == "__main__":
    torment_the_whale()

# pyinstaller --onefile --add-data "media\whale.png;media" --add-data "media\whale_icon.ico;media" --add-data "responses.json;." --windowed --icon=media\whale_icon.ico main.py
