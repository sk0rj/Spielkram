from tkinter import Tk
from class_WhaleGUI import WhaleGUI

# Startet die Anwendung und öffnet das Hauptfenster
def torment_the_whale():
    root = Tk()
    app = WhaleGUI(root)
    root.mainloop()


# Hauptausführungspunkt der Anwendung
if __name__ == "__main__":
    torment_the_whale()


# pyinstaller --onefile --add-data "media\whale.png;media" --add-data "media\whale_icon.ico;media" --add-data "watery_wonders.json;." --windowed --icon=media\whale_icon.ico main.py
