from models.foreground_color import ForegroundColor
def get_operator():
    chosen_operator = ""
    valid_operators = ["+", "-", "x", "/", "//", "%", "**"]
    error_message = f"{ForegroundColor.Red}Fehlerhafte Eingabe: Bitte gebe einen Operator ein.{ForegroundColor.Reset}"
    while True:
        chosen_operator = input("Was willst du mit dieser Zahl tun?\t\t").strip()
        if chosen_operator not in valid_operators:
            print(error_message);
            continue;
        else:
            break;
    return chosen_operator
