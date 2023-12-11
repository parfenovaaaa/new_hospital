from unittest.mock import MagicMock

import pytest

from logic.utils.console import Console
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

    @pytest.mark.parametrize("patient_id, error_msg", [
        [-2, "Ошибка! ID пациента должно быть числом(целым и положительным)"],
        ["two", "Ошибка! ID пациента должно быть числом(целым и положительным)"],
        [0, "Ошибка! ID пациента должно быть числом(целым и положительным)"],
        [2, "Ошибка! Нет пациента с таким ID"],
    ]
                             )
    def test_patient_status_patient_id_error(self, patient_id, error_msg):
        dialog_with_user = DialogWithUser(Console())
        dialog_with_user.ask_user_for_input = MagicMock(return_value=patient_id)
        dialog_with_user.print_to_user_output = MagicMock()

        patients_list = PatientsStatusListHandler([0])
        patient_command = PatientCommands(dialog_with_user, patients_list)
        patient_command.get_patient_status()

        dialog_with_user.print_to_user_output.assert_called_with(error_msg)
