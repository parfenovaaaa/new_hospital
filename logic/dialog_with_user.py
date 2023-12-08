from logic.patient_errors import PatientIdNotIntegerOrNotPositive

YES_COMMANDS = ["yes", "y", "да"]


class DialogWithUser:

    def get_patient_id(self) -> int:
        try:
            patient_id = int(self.get_msg_from_user("Введите ID пациента:"))
            if patient_id <= 0:
                raise PatientIdNotIntegerOrNotPositive()
            else:
                return patient_id
        except ValueError:
            raise PatientIdNotIntegerOrNotPositive()

    @staticmethod
    def send_msg_to_user(msg: str) -> None:
        print(msg)
        pass

    @staticmethod
    def get_msg_from_user(msg: str) -> str:
        command = input(msg)
        return command
        pass

    @staticmethod
    def ask_discharge_patient() -> bool:
        result = input("Выписать пациента? (да/нет)")
        if result in YES_COMMANDS:
            return True
        else:
            return False
        pass
