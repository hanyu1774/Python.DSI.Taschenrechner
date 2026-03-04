# ── Models ───────────────────────────────────────────────
# Hier sind nur reine Daten

# Diese Klasse namens ForegroundColor hat Farbcodes zum
# Aendern der Schriftfarbe in der Konsole.
class ForegroundColor:
    Red: str = "\033[31m"
    LightRubyRed: str = "\033[38;5;197m"
    Green: str = "\033[32m"
    Yellow: str = "\033[33m"
    Cyan: str = "\033[36m"
    Orange: str = "\033[38;5;208m"
    Reset: str = "\033[0m"

dividing_line = 65 * '#'
header = f"{dividing_line}\nGuten Tag!\nIch bin der beste Taschenrechner!\nIch kann +, -, x, /, //, % und ** berechnen!\n{dividing_line}"
footer = f"{dividing_line}\nProgram wird beendet...\n{dividing_line}"

operator_map = {
    "+" :"\t\t\tAddition",
    "-" :"\t\t\tSubtraktion",
    "x" :"\t\t\tMultiplikation",
    "/" :"\t\t\tDivision",
    "//" :"\t\t\tDivision mit Abrundung",
    "%" :"\t\t\tRestzahl einer Division bestimmen",
    "**" :"\t\t\tPotenzieren",
}

# ── Flows ───────────────────────────────────────────────────────
# Hier sind Funktionen, die Aufgaben erledigen

def calculate(operator: str, number_a: float, number_b: float):
    operations = {
        # Dieses Dictionary umfasst Lambda-Funktionen
        # Key: die Operatoren
        # Value: die Funktion (z.B. Addition, Subtraktion, etc.)
        "+": lambda a,b: a + b,
        "-": lambda a,b: a - b,
        "x": lambda a,b: a * b,
        "/": lambda a,b: a / b,
        "//": lambda a,b: a // b,
        "%": lambda a,b: a % b,
        "**": lambda a,b: a ** b,
    }
    return operations[operator](number_a, number_b)


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
    return 0;

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

def get_result_message(first_number: float, operator: str, second_number: float, result: float)-> str:
    return f"Das Ergebnis der Rechnung {first_number} {operator} {second_number} lautet {result:.2f} !"

# ── Workflow ─────────────────────────────────────────────────────
# Orchestrierung der Logik

# Diese Funktion, run_workflow, dient zur Orchestration,
# um die Hauptlogik des Programmes auszufuehren.

def run_workflow():
    print(f"{ForegroundColor.Green}{header}{ForegroundColor.Reset}");
    print(f"{ForegroundColor.Cyan}{dividing_line}\nOperatoren\n{dividing_line}")
    for key, value in operator_map.items():
        print(f"{key} {value}")
    print(f"{dividing_line}{ForegroundColor.Reset}")
    while True:
        first_number = get_number()
        selected_operator = get_operator()
        second_number = get_number(True)
        calculation_result = calculate(selected_operator, first_number, second_number)
        result_message = get_result_message(first_number, selected_operator, second_number, calculation_result) 
        print(f"{ForegroundColor.Orange}{dividing_line}\n{result_message}\n{dividing_line}{ForegroundColor.Reset}")
        another_round: bool = do_another_calculation()
        if another_round:
            continue
        break
    print(f"{ForegroundColor.LightRubyRed}{footer}{ForegroundColor.Reset}") 

# ── Ausfuerung des Taschenrechners ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    run_workflow()
