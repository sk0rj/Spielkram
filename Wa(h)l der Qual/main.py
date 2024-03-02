from tkinter import Tk
from gui import create_gui
from functions import resource_path

# Starten der Anwendung
def torment_the_whale():

    root = Tk()

    window_width = 300
    window_height = 418

    monitor_center_x = root.winfo_screenwidth() / 2 - (window_width / 2)
    monitor_center_y = root.winfo_screenheight() / 2 - (window_height / 2)

    root.geometry("%dx%d+%d+%d" % (window_width, window_height, monitor_center_x, monitor_center_y))
    root.resizable(width=False, height=False)
    root.title("Wa(h)l der Qual")
    root.iconbitmap(resource_path("media/whale_icon.ico"))

    create_gui(root)

    root.mainloop()

if __name__ == "__main__":
    torment_the_whale()

# pyinstaller --onefile --add-data "media/whale.png:media" --add-data "media/whale_icon.ico:media" --windowed --icon=media/whale_icon.ico main.py