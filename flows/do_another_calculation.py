from models.foreground_color import ForegroundColor

def do_another_calculation() -> bool:
    error_message: str = f"{ForegroundColor.Red}Fehlerhafte Eingabe! Tippe 'j' oder 'n'.\t\t\t{ForegroundColor.Reset}"
    while True:
        yes_or_no = input("Noch einmal? (j/n)\t\t\t\t").strip()
        if yes_or_no not in ('j', 'n'):
            print(error_message)
            continue
        elif yes_or_no == 'j':
            return True
        break
    return False
