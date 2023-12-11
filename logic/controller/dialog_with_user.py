from logic.utils.patient_errors import PatientIdNotIntegerOrNotPositive

YES_COMMANDS = ["yes", "y", "да"]


class DialogWithUser:

    def __init__(self, console):
        self.console = console

    def ask_user_patient_id(self) -> int:
        try:
            patient_id = int(self.ask_user_for_input("Введите ID пациента:"))
            if patient_id <= 0:
                raise PatientIdNotIntegerOrNotPositive()
            else:
                return patient_id
        except ValueError:
            raise PatientIdNotIntegerOrNotPositive()

    def print_to_user_output(self, msg: str) -> None:
        self.console.output(msg)

    def ask_user_for_input(self, msg: str) -> str:
        return self.console.input(msg)

    def ask_discharge_patient(self) -> bool:
        result = self.ask_user_for_input("Выписать пациента? (да/нет)")
        return result in YES_COMMANDS
