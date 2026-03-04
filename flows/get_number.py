from models.foreground_color import ForegroundColor
def get_number(second_input_request: bool = False)-> float:
    input_number = ""
    first_input_message = "Tippe die erste Zahl ein... \t"
    second_input_message = "Tippe die zweite Zahl ein... \t"
    error_message = f"{ForegroundColor.Red}Fehlerhafte Eingabe! Du musst eine Zahl eintippen.{ForegroundColor.Reset}"

    while True:
        if not second_input_request:
            input_number = input(first_input_message).strip()
        else:
            input_number = input(second_input_message).strip()
        if not input_number.isdecimal():
            print(f"{error_message}");
            continue;
        break;
    return float(input_number)
