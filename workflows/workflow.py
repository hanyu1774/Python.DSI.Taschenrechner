from models.console_ui_segment import header, footer
from models.color_map import ForegroundColor
#from models.console_ui_segment import ???
from models.map_operators import operator_map 
from flows.calculate import calculate
from flows.get_operator import get_operator

# Diese Funktion, run_workflow, dient zur Orchestration,
# um die Hauptlogik des Programmes auszufuehren.
# run_workflow wird in der Datei program.py benutzt.
def run_workflow():
    print(f"{ForegroundColor.Green}{header}{ForegroundColor.Reset}");
    print("Operatoren")
    for key, value in operator_map.items():
        print(f"{key}:\t {value}")


