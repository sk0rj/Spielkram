from tkinter import ttk
from PIL import Image, ImageTk
from class_Utilities import Utilities

class WhaleGUI:
    # Initialisiert die GUI und setzt Fenstereigenschaften
    def __init__(self, root):

        self.__root = root
        self.__window_width = 320
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

        # Erstellen der Hauptframes
        self.__main_button_frame = ttk.Frame(self.__root)
        self.__main_button_frame.grid(row=0, column=0, columnspan=2)

        self.__current_mode_frame = ttk.Frame(self.__root)
        self.__current_mode_frame.grid(row=1, column=0, columnspan=2, sticky="ew")

        self.__whale_image_frame = ttk.Frame(self.__root)
        self.__whale_image_frame.grid(row=2, column=0, columnspan=2, sticky="s")


        # Gewichtung der Frames im Hauptfenster
        self.__root.rowconfigure(0, weight=0) # __main_button_frame
        self.__root.rowconfigure(1, weight=0) # __current_mode_frame
        self.__root.rowconfigure(2, weight=1) # __whale_image_frame

        self.__root.columnconfigure(0, weight=1)
        self.__root.columnconfigure(1, weight=1)


        # Buttons für Modusauswahl (__main_button_frame)
        self.__oracle_mode_button = ttk.Button(self.__main_button_frame, text="Wal Orakel", command=self.__oracle, width=20)
        self.__oracle_mode_button.grid(row=0, column=0, padx=10, pady=3)

        self.__dice_mode_button = ttk.Button(self.__main_button_frame, text="Wal Würfel", command=self.__roll_dice, width=20)
        self.__dice_mode_button.grid(row=0, column=1, padx=10, pady=3)


        # Wal-Grafik (__whale_image_frame)
        self.__image_label = ttk.Label(self.__whale_image_frame)
        self.__image_label.grid(row=5, column=0, columnspan=2, pady=10)

        image = Image.open(Utilities.resource_path("media\\whale.png"))
        image.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(image)

        self.__image_label.config(image=photo)
        self.__image_label.image = photo



    # Methode für den Orakel-Modus
    def __oracle(self):

        # Löschen der Widgets im Mode-Frame (__current_mode_frame)
        Utilities.destroy_widgets(self.__current_mode_frame)


        # Button Switch
        self.__oracle_mode_button['state'] = 'disabled'
        self.__dice_mode_button['state'] = 'enabled'


        # Laden der Texte
        oracle_responses = Utilities.load_wonders("oracle_responses")


        # Gewichtung der Widgets im Frame (__current_mode_frame) für den Orakel-Modus
        self.__current_mode_frame.rowconfigure(0, weight=0) # __description_label
        self.__current_mode_frame.rowconfigure(1, weight=0) # __button
        self.__current_mode_frame.rowconfigure(2, weight=1) # __result_label
        self.__current_mode_frame.columnconfigure(0, weight=1)
        self.__current_mode_frame.columnconfigure(1, weight=1)


        # Modi Beschreibung
        self.__description_label = ttk.Label(self.__current_mode_frame, text=Utilities.generate_random_oracle_description(), font=("Arial", 10, "bold"), justify="center")
        self.__description_label.grid(row=1, column=0, columnspan=2, pady=5)


        # Button
        self.__button = ttk.Button(self.__current_mode_frame, text="Frag den Wal", command=lambda: Utilities.generate_destiny(self.__result_label, *oracle_responses))
        self.__button.grid(row=2, column=0, columnspan=2, pady=5, sticky="s")


        # Ergebnisausgabe
        self.__result_label = ttk.Label(self.__current_mode_frame, text="", justify="center", font=("Arial", 10, "italic"))
        self.__result_label.grid(row=3, column=0, columnspan=2, pady=5, sticky="n")



    # Methode für den Würfel-Modus
    def __roll_dice(self):

        # Löschen der Widgets im Mode-Frame (__current_mode_frame)
        Utilities.destroy_widgets(self.__current_mode_frame)


        # Button Switch
        self.__oracle_mode_button['state'] = 'enabled'
        self.__dice_mode_button['state'] = 'disabled'

        # Laden der Texte
        dice_responses = Utilities.load_wonders("dice_responses")


        # Gewichtung der Widgets im Frame (__current_mode_frame) für den Würfel-Modus
        self.__current_mode_frame.rowconfigure(0, weight=0) # __description_label & __input_entry
        self.__current_mode_frame.rowconfigure(1, weight=0) # __button
        self.__current_mode_frame.rowconfigure(2, weight=1) # __result_label
        self.__current_mode_frame.columnconfigure(0, weight=1)
        self.__current_mode_frame.columnconfigure(1, weight=1)


        # Modi Beschreibung
        self.__description_label = ttk.Label(self.__current_mode_frame, text="Wie viele Seiten\nsoll der Würfel haben:", font=("Arial", 10, "bold"), justify="center")
        self.__description_label.grid(row=0, column=0, pady=5, padx=3)

        
        # Eingabefeld
        validate_cmd = self.__current_mode_frame.register(Utilities.on_validate)

        self.__input_entry = ttk.Entry(self.__current_mode_frame, validate="key", validatecommand=(validate_cmd, '%P'), width=20)
        self.__input_entry.grid(row=0, column=1, pady=5, padx=3, sticky="s, w")

        self.__input_entry.focus_set()


        # Button
        self.__button = ttk.Button(self.__current_mode_frame, text="Lass den Wal würfeln", command=lambda: Utilities.user_input(self.__input_entry, self.__result_label, *dice_responses))
        self.__button.grid(row=1, column=0, columnspan=2, pady=5)


        # Ergebnisausgabe
        self.__result_label = ttk.Label(self.__current_mode_frame, text="", justify="center", font=("Arial", 10, "italic"))
        self.__result_label.grid(row=2, column=0, columnspan=2, pady=5)


        # Verarbeitung der Eingabe durch drücken der Enter-Taste
        self.__input_entry.bind("<Return>", lambda event: Utilities.on_enter_pressed(event, self.__input_entry, self.__result_label, *dice_responses))
