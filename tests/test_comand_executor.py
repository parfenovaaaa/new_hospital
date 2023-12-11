
from unittest.mock import MagicMock

from logic.utils.console import Console
from hospital_application import HospitalApplication
from logic.controller.dialog_with_user import DialogWithUser
from logic.use_case.patient_commands import PatientCommands
from logic.core.patients_status_list_handler import PatientsStatusListHandler
from logic.use_case.statistics_commands import StatisticsCommands


class TestsCommandExecutor:
    # def test_unknown_command(self):
    #     dialog_with_user = DialogWithUser(Console())
    #     dialog_with_user.ask_user_for_input = MagicMock(return_value="unknown command")
    #     dialog_with_user.print_to_user_output = MagicMock()
    #
    #     db = PatientsStatusListHandler([])
    #     statistics_command = StatisticsCommands(db)
    #     patient_command = PatientCommands(dialog_with_user, db)
    #     executor = CommandExecutor(dialog_with_user, statistics_command, patient_command)
    #
    #     executor.start_operation()
    #     dialog_with_user.print_to_user_output.assert_called_with("Неизвестная команда! Попробуйте еще раз!")

    def test_stop_command(self):
        dialog_with_user = DialogWithUser(Console())

        dialog_with_user.ask_user_for_input = MagicMock(return_value="stop")
        dialog_with_user.print_to_user_output = MagicMock()

        patients_list = PatientsStatusListHandler([])
        statistics_command = StatisticsCommands(patients_list)
        patient_command = PatientCommands(dialog_with_user, patients_list)
        executor = HospitalApplication(dialog_with_user, statistics_command, patient_command, )

        executor.start_operation()
        dialog_with_user.print_to_user_output.assert_called_with("Сеанс завершён")
