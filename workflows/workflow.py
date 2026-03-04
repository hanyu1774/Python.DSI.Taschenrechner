from unittest import result
from models import foreground_color
from models.console_ui_segment import header, dividing_line, footer
from models.foreground_color import ForegroundColor
from models.operator_map import operator_map 
from flows.calculate import calculate
from flows.do_another_calculation import do_another_calculation
from flows.get_operator import get_operator
from flows.get_number import get_number
from flows.get_result_message import get_result_message

# Diese Funktion, run_workflow, dient zur Orchestration,
# um die Hauptlogik des Programmes auszufuehren.
# run_workflow wird in der Datei program.py benutzt.
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
        print(f"{ForegroundColor.Yellow}{dividing_line}\n{result_message}\n{dividing_line}{ForegroundColor.Reset}")
        another_round: bool = do_another_calculation()
        if another_round:
            continue
        break
    print(f"{ForegroundColor.Green}{footer}{ForegroundColor.Reset}") 
