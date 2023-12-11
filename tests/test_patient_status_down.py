from unittest.mock import MagicMock

from logic.controller.dialog_with_user import DialogWithUser
from logic.use_case.patient_commands import PatientCommands
from logic.core.patients_status_list_handler import PatientsStatusListHandler


class TestPatientStatusDown:
    def test_patient_status_down_success(self):
        dialog_with_user = DialogWithUser()

        dialog_with_user.ask_user_patient_id = MagicMock(return_value=1)
        dialog_with_user.print_to_user_output = MagicMock()

        patients_status_list = PatientsStatusListHandler([3, 3, 3])
        patient_command = PatientCommands(dialog_with_user, patients_status_list)
        patient_command.patient_status_down()
        dialog_with_user.print_to_user_output.assert_called_with("Новый статус пациента: 'Слегка болен'")
        assert patients_status_list.patients_status_list == [2, 3, 3]

    def test_patient_status_down_fail(self):
        dialog_with_user = DialogWithUser()

        dialog_with_user.ask_user_patient_id = MagicMock(return_value=2)
        dialog_with_user.print_to_user_output = MagicMock()

        patients_status_list = PatientsStatusListHandler([3, 0, 3])
        patient_command = PatientCommands(dialog_with_user, patients_status_list)
        patient_command.patient_status_down()
        dialog_with_user.print_to_user_output.assert_called_with(
            "Ошибка. Нельзя понизить самый низкий статус(наши пациенты не умирают)"
        )
        assert patients_status_list.patients_status_list == [3, 0, 3]
