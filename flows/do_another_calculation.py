from models.foreground_color import ForegroundColor
def do_another_calculation() -> bool:
    error_message: str = f"{ForegroundColor.Red}Fehlerhafte Eingabe! Tippe 'j' oder 'n'.{ForegroundColor.Reset}"
    while(True):
        yes_or_no = input("Noch einmal? (j/n)").strip()
        if yes_or_no != 'j' or yes_or_no != 'n':
            print(error_message)
            continue
        elif yes_or_no == 'j':
            return True
        break
    return False


