from enum import Enum

# Dieses Dictionary hat Farbcodes zum
# Aendern der Schriftfarbe in der Konsole
# Diese Farbcodes sind in der "Escape notation", 
# da sie zur "Escape-Sequenz gehoeren".
# Die Farbecodes sind hinter dem "\"-Zeichen
#
# Was ist eine Escape-Sequenz?
# Der Befehl "\n" ist z.B. eine Escape-Sequenz, die
# am Ende eines Strings eine neue Zeile erzeugt
# Anwendung: 
# print("Hallo!\nWie geht es dir?")
#
# Diese Farbcodes funktionieren nur in der Konsole


# Hier ist eine Enum-Klasse namens "Color".
# Ein Enum ist eine eigener, definierter Datentyp
# Jede Farbe entspricht ihren eigenen Datentyp
class ForegroundColor(Enum):
    Red = "\033[31m",
    Green = "\033[32m",
    Yellow = "\033[33m",
    Blue = "\033[34m"
    Reset = "\033[0m"


# Wie man es benutzt?
# Damit kann man die Schriftfarbe eines Strings aendern.
# Anwendung:
# print(f"{ForegroundColor.Yello}Hallo, wie geht es dir?{ForegroundColor.Reset}")
# Man muss am Ende des Strings die benutzte Farbe zuerucksetzen, sonst wird die Farbe des gesamten
# Textes in der Konsole geaendert.
