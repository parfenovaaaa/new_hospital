from unittest.mock import MagicMock

import pytest

from logic.controller.console import Console
from logic.controller.dialog_with_user import DialogWithUser
from logic.use_case.patient_commands import PatientCommands
from logic.core.patients_status_list_handler import PatientsStatusListHandler


class TestGetPatientStatus:
    @pytest.mark.parametrize("status, index",
                             [["Тяжело болен", 1],
                             ["Болен", 2],
                             ["Слегка болен", 3],
                             ["Готов к выписке", 4]]
                             )
    def test_get_patient_status(self, status, index):
        dialog_with_user = DialogWithUser(Console())
        dialog_with_user.print_to_user_output = MagicMock()
        dialog_with_user.ask_user_patient_id = MagicMock(return_value=index)

        patients_list = PatientsStatusListHandler([0, 1, 2, 3])
        patient_command = PatientCommands(dialog_with_user, patients_list)

        patient_command.get_patient_status()
        dialog_with_user.print_to_user_output.assert_called_with(f"Статус пациента: '{status}'")

    def test_patient_status_id_error_negative(self):
        dialog_with_user = DialogWithUser(Console())
        dialog_with_user.ask_user_for_input = MagicMock(return_value=-2)
        dialog_with_user.print_to_user_output = MagicMock()

        patients_list = PatientsStatusListHandler([])
        patient_command = PatientCommands(dialog_with_user, patients_list)

        patient_command.get_patient_status()
        dialog_with_user.print_to_user_output.assert_called_with(
            "Ошибка! ID пациента должно быть числом(целым и положительным)"
        )

    def test_patient_status_id_error_string(self):
        dialog_with_user = DialogWithUser(Console())
        dialog_with_user.ask_user_for_input = MagicMock(return_value="sdg")
        dialog_with_user.print_to_user_output = MagicMock()

        patients_list = PatientsStatusListHandler([])
        patient_command = PatientCommands(dialog_with_user, patients_list)

        patient_command.get_patient_status()
        dialog_with_user.print_to_user_output.assert_called_with(
            "Ошибка! ID пациента должно быть числом(целым и положительным)"
        )

    def test_patient_status_id_error_not_exist(self):
        dialog_with_user = DialogWithUser(Console())
        dialog_with_user.ask_user_for_input = MagicMock(return_value=2)
        dialog_with_user.print_to_user_output = MagicMock()

        patients_list = PatientsStatusListHandler([0])
        patient_command = PatientCommands(dialog_with_user, patients_list)

        patient_command.get_patient_status()
        dialog_with_user.print_to_user_output.assert_called_with("Ошибка! Нет пациента с таким ID")
