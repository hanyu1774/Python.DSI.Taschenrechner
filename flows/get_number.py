from models.foreground_color import ForegroundColor
def get_number(second_input_request: bool = False)-> float:
    input_number = ""
    first_input_message = "Tippe die erste Zahl ein... \t\t\t"
    second_input_message = "Tippe die zweite Zahl ein... \t\t\t"
    error_message = f"{ForegroundColor.Red}Fehlerhafte Eingabe! Du musst eine Zahl eintippen.{ForegroundColor.Reset}"
    message_request = ""
    if second_input_request:
        message_request = second_input_message
    else:
        message_request = first_input_message

    while True:
        input_number = input(message_request).strip()
        try:
            return float(input_number)
        except Exception:
            print(error_message)
            continue
        break
    return 0;
