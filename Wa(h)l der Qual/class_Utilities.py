import json, os, sys
from random import randint, choice

class Utilities:

    # Gibt den vollständigen Pfad zu einer Datei zurück
    @staticmethod
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
        
    # Lädt Daten aus der 'watery_wonders.json' und gibt die entsprechenden Abschnitte zurück
    @staticmethod
    def load_wonders(response_type):
        with open(Utilities.resource_path('watery_wonders.json'), 'r', encoding='utf-8') as json_file:
            responses_data = json.load(json_file)

        if response_type == "oracle_description":
            return responses_data.get("oracle_description", [])
        elif response_type == "dice_responses":
            return (
                responses_data.get("dice_random_responses", []),
                responses_data.get("dice_random_dumbass", []),
                responses_data.get("dice_special_responses", [])
            )
        elif response_type == "oracle_responses":
            return (
                responses_data.get("oracle_random_positive", []),
                responses_data.get("oracle_random_negative", []),
                responses_data.get("oracle_special_responses", [])
            )
        else:
            return [], [], []

    # Generiert zufällig eine Orakelbeschreibung aus den geladenen Daten
    @staticmethod
    def generate_random_oracle_description():
        oracle_description = Utilities.load_wonders("oracle_description")
        return choice(oracle_description)

    # Verarbeitet die Benutzereingabe und aktualisiert das Ergebnislabel basierend auf Bedingungen und zufälligen Werten
    @staticmethod
    def user_input(entry, result_label, random_responses, random_dumbass, special_responses):
        try:
            max_value = int(entry.get())
            if max_value == 1 or max_value == 0:
                result_label.config(text=choice(random_dumbass))
            else:
                if randint(1, 100) <= 10:
                    result_label.config(text=choice(special_responses))
                else:
                    choice_value = Utilities.generate_random(max_value)
                    result_label.config(text=choice(random_responses) + str(choice_value))
        except ValueError:
            result_label.config(text=choice(random_dumbass))

    # Generiert eine zufällige Zahl zwischen 1 und max_value
    @staticmethod
    def generate_random(max_value):
        min_value = 1
        choice_value = randint(min_value, max_value)
        return choice_value

    # Generiert zufällig eine positive oder negative Antwort
    @staticmethod
    def generate_destiny(result_label, random_positive, random_negative, special_responses):
        decision = Utilities.generate_random(2)

        if randint(1, 100) <= 10:
            result_label.config(text=choice(special_responses))
        else:
            if decision == 1:
                result_label.config(text=choice(random_positive))
            elif decision == 2:
                result_label.config(text=choice(random_negative))

    # Handler-Methode für die Eingabetaste
    @staticmethod
    def on_enter_pressed(event, entry, result_label, random_responses, random_dumbass, special_responses):
        Utilities.user_input(entry, result_label, random_responses, random_dumbass, special_responses)

    # Limitiert die Eingabe auf 10 Zeichen
    @staticmethod
    def on_validate(P):
        return (len(P) <= 10)
    
    # Zerstört alle Widgets im Hauptfenster, außer denen, die in main_gui enthalten sind
    @staticmethod
    def destroy_widgets(root, main_gui):
        for widget in root.winfo_children():
            if widget not in main_gui:
                widget.destroy()
