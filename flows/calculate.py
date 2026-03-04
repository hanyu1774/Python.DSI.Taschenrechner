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
