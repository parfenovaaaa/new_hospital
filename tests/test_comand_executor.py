
from unittest.mock import MagicMock

from logic.command_executor import CommandExecutor
from logic.dialog_with_user import DialogWithUser
from logic.patient_commands import PatientCommands
from logic.patient_db import PatientsDB
from logic.statistics_commands import StatisticsCommands


class TestsCommandExecutor:
    def test_unknown_command(self):
        dialog_with_user = DialogWithUser()

        dialog_with_user.get_msg_from_user = MagicMock(return_value="unknown command")
        dialog_with_user.send_msg_to_user = MagicMock()

        db = PatientsDB([])
        statistics_command = StatisticsCommands(db)
        patient_command = PatientCommands(dialog_with_user, db)
        executor = CommandExecutor(dialog_with_user, statistics_command, patient_command, )
        executor.start_operation()
        dialog_with_user.send_msg_to_user.assert_called_with("Неизвестная команда! Попробуйте еще раз!")

    def test_stop_command(self):
        dialog_with_user = DialogWithUser()

        dialog_with_user.get_msg_from_user = MagicMock(return_value="stop")
        dialog_with_user.send_msg_to_user = MagicMock()

        db = PatientsDB([])
        statistics_command = StatisticsCommands(db)
        patient_command = PatientCommands(dialog_with_user, db)
        executor = CommandExecutor(dialog_with_user, statistics_command, patient_command, )
        executor.start_operation()
        dialog_with_user.send_msg_to_user.assert_called_with("Сеанс завершён")
