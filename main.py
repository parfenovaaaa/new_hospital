from logic.command_executor import CommandExecutor
from logic.dialog_with_user import DialogWithUser
from logic.patient_commands import PatientCommands
from logic.statistics_commands import StatisticsCommands
from logic.patient_db import PatientsDB


if __name__ == '__main__':
    patients_db = PatientsDB()
    dialog_with_user = DialogWithUser()
    statistics_commands = StatisticsCommands(patients_db)
    patient_commands = PatientCommands(dialog_with_user, patients_db)
    command_executor = CommandExecutor(dialog_with_user, statistics_commands, patient_commands)
    command_executor.start_operation()
