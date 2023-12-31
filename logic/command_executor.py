from logic.dialog_with_user import DialogWithUser
from logic.patient_commands import PatientCommands
from logic.statistics_commands import StatisticsCommands

GET_STATUS_COMMANDS = ["get status", "узнать статус пациента", "1"]
STATUS_UP_COMMANDS = ["status up", "повысить статус пациента", "2"]
STATUS_DOWN_COMMANDS = ["status down", "понизить статус пациента", "3"]
DISCHARGE_COMMANDS = ["discharge", "выписать пациента", "4"]
STATISTICS_COMMANDS = ["calculate statistics", "рассчитать статистику", "5"]
STOP_COMMANDS = ["stop", "стоп"]
COMMANDS = (
        GET_STATUS_COMMANDS + STATUS_UP_COMMANDS + STATUS_DOWN_COMMANDS + DISCHARGE_COMMANDS + STATISTICS_COMMANDS
)


class CommandExecutor:
    def __init__(
            self, dialog_with_user: DialogWithUser,
            statistics_commands: StatisticsCommands, patient_commands: PatientCommands
    ):
        self.statistics_commands = statistics_commands
        self.dialog_with_user = dialog_with_user
        self.patient_commands = patient_commands

    def start_operation(self) -> None:
        while True:
            command = self.dialog_with_user.get_msg_from_user("Введите команду: ")
            if command in STOP_COMMANDS:
                self.dialog_with_user.send_msg_to_user("Сеанс завершён")
                break
            elif command not in COMMANDS:
                self.dialog_with_user.send_msg_to_user("Неизвестная команда! Попробуйте еще раз!")
                break
            elif command in STATISTICS_COMMANDS:
                statistics = self.statistics_commands.calculate_statistics()
                self.dialog_with_user.send_msg_to_user(statistics)
            elif command in GET_STATUS_COMMANDS:
                self.patient_commands.get_patient_status()
            elif command in STATUS_UP_COMMANDS:
                self.patient_commands.patient_status_up()
            elif command in STATUS_DOWN_COMMANDS:
                self.patient_commands.patient_status_down()
            elif command in DISCHARGE_COMMANDS:
                self.patient_commands.discharge_patient()
