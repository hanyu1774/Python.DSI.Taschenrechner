def get_operator():
    chosen_operator = ""
    valid_operators = ["+", "-", "x", "/", "//", "%", "**"]
    
    while True:
        chosen_operator = input("Gebe bitte den Operator (+, -, x, /, //, %, **) ein:\t").strip()
        
        if chosen_operator not in valid_operators:
            print("Fehlerhafte Eingabe: Bitte gebe einen Operator (+, -, x, /, //, %, **) ein:\t");
            continue;
        else:
            break;
    return chosen_operator
