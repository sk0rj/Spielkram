from tkinter import ttk
from PIL import Image, ImageTk
from class_Utilities import Utilities

class WhaleGUI:
    # Initialisiert die GUI und setzt Fenstereigenschaften
    def __init__(self, root):

        self.__root = root
        self.__window_width = 300
        self.__window_height = 465
        self.__monitor_center_x = self.__root.winfo_screenwidth() / 2 - (self.__window_width / 2)
        self.__monitor_center_y = self.__root.winfo_screenheight() / 2 - (self.__window_height / 2)

        self.__root.geometry("%dx%d+%d+%d" % (self.__window_width, self.__window_height, self.__monitor_center_x, self.__monitor_center_y))
        self.__root.resizable(width=False, height=False)
        self.__root.title("Wa(h)l der Qual")
        self.__root.iconbitmap(Utilities.resource_path("media\\whale_icon.ico"))

        self.__create_gui()

    # Erstellt die Haupt GUI-Elemente
    def __create_gui(self):

        self.__oracle_mode_button = ttk.Button(self.__root, text="Wal Orakel", command=self.__oracle, width=20)
        self.__oracle_mode_button.grid(row=0, column=0, pady=3, padx=(10, 5))

        self.__dice_mode_button = ttk.Button(self.__root, text="Wal Würfel", command=self.__roll_dice, width=20)
        self.__dice_mode_button.grid(row=0, column=1, pady=3, padx=(5, 10))

        self.__root.columnconfigure(0, weight=1)
        self.__root.columnconfigure(1, weight=1)

        self.__root.rowconfigure(3, weight=1)

        self.__image_label = ttk.Label(self.__root)
        self.__image_label.grid(row=5, column=0, columnspan=2, pady=10, sticky="s")

        image = Image.open(Utilities.resource_path("media\\whale.png"))
        image.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(image)

        self.__image_label.config(image=photo)
        self.__image_label.image = photo

        self.__main_gui = self.__oracle_mode_button, self.__dice_mode_button, self.__image_label


    # Methode für den Orakel-Modus
    def __oracle(self):

        Utilities.destroy_widgets(self.__root, self.__main_gui)

        self.__oracle_mode_button['state'] = 'disabled'
        self.__dice_mode_button['state'] = 'enabled'

        oracle_responses = Utilities.load_wonders("oracle_responses")

        self.__description_label = ttk.Label(self.__root, text=Utilities.generate_random_oracle_description(), font=("Arial", 10, "bold"), justify="center")
        self.__description_label.grid(row=1, column=0, columnspan=2, pady=5)

        self.__result_label = ttk.Label(self.__root, text="", justify="center", font=("Arial", 10, "italic"))
        self.__result_label.grid(row=3, column=0, columnspan=2, pady=5, sticky="n")

        self.__button = ttk.Button(self.__root, text="Frag den Wal", command=lambda: Utilities.generate_destiny(self.__result_label, *oracle_responses))
        self.__button.grid(row=2, column=0, columnspan=2, pady=5, sticky="s")


    # Methode für den Würfel-Modus
    def __roll_dice(self):

        Utilities.destroy_widgets(self.__root, self.__main_gui)

        self.__oracle_mode_button['state'] = 'enabled'
        self.__dice_mode_button['state'] = 'disabled'

        dice_responses = Utilities.load_wonders("dice_responses")

        self.__description_label = ttk.Label(self.__root, text="Wie viele Seiten\nsoll der Würfel haben:", font=("Arial", 10, "bold"), justify="center")
        self.__description_label.grid(row=1, column=0, columnspan=2, pady=5, padx=13, sticky="w")

        validate_cmd = self.__root.register(Utilities.on_validate)

        self.__input_entry = ttk.Entry(self.__root, validate="key", validatecommand=(validate_cmd, '%P'), width=18)
        self.__input_entry.grid(row=1, column=1, pady=5, padx=13, sticky="e, s")

        self.__result_label = ttk.Label(self.__root, text="", justify="center", font=("Arial", 10, "italic"))
        self.__result_label.grid(row=3, column=0, columnspan=2, pady=5)

        self.__button = ttk.Button(self.__root, text="Lass den Wal würfeln", command=lambda: Utilities.user_input(self.__input_entry, self.__result_label, *dice_responses))
        self.__button.grid(row=2, column=0, columnspan=2, pady=5)

        self.__input_entry.focus_set()

        self.__input_entry.bind("<Return>", lambda event: Utilities.on_enter_pressed(event, self.__input_entry, self.__result_label, *dice_responses))
