from logic.controller.console import Console
from logic.use_case.command_executor import CommandExecutor
from logic.controller.dialog_with_user import DialogWithUser
from logic.use_case.patient_commands import PatientCommands
from logic.use_case.statistics_commands import StatisticsCommands
from logic.core.patients_status_list_handler import PatientsStatusListHandler


if __name__ == '__main__':
    console = Console()
    dialog_with_user = DialogWithUser(console)
    patients_status_list = PatientsStatusListHandler([])
    statistics_commands = StatisticsCommands(patients_status_list)
    patient_commands = PatientCommands(dialog_with_user, patients_status_list)
    command_executor = CommandExecutor(dialog_with_user, statistics_commands, patient_commands)
    command_executor.start_operation()
