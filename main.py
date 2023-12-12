from logic.utils.console import Console
from hospital_application import HospitalApplication
from logic.controller.dialog_with_user import DialogWithUser
from logic.use_case.patient_commands import PatientCommands
from logic.use_case.statistics_commands import StatisticsCommands
from logic.core.patients_status_list_handler import PatientsStatusListHandler


if __name__ == '__main__':
    console = Console()
    dialog_with_user = DialogWithUser(console)
    patients_status_list = PatientsStatusListHandler([1, 1, 1])
    statistics_commands = StatisticsCommands(dialog_with_user, patients_status_list)
    patient_commands = PatientCommands(dialog_with_user, patients_status_list)
    application = HospitalApplication(dialog_with_user, statistics_commands, patient_commands)
    application.start_operation()
