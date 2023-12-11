from unittest.mock import MagicMock

from logic.controller.console import Console
from logic.controller.dialog_with_user import DialogWithUser
from logic.use_case.patient_commands import PatientCommands
from logic.core.patients_status_list_handler import PatientsStatusListHandler


class TestPatientStatusUp:
    def test_patient_status_up_success(self):
        dialog_with_user = DialogWithUser(Console())
        dialog_with_user.ask_user_patient_id = MagicMock(return_value=2)
        dialog_with_user.print_to_user_output = MagicMock()

        patients_status_list = PatientsStatusListHandler([0, 0, 0])
        patient_command = PatientCommands(dialog_with_user, patients_status_list)
        patient_command.patient_status_up()

        dialog_with_user.print_to_user_output.assert_called_with("Новый статус пациента: 'Болен'")
        assert patients_status_list.patients_status_list == [0, 1, 0]

    def test_patient_status_up_discharge_success(self):
        dialog_with_user = DialogWithUser(Console())
        dialog_with_user.ask_user_patient_id = MagicMock(return_value=2)
        dialog_with_user.ask_discharge_patient = MagicMock(return_value=True)
        dialog_with_user.print_to_user_output = MagicMock()

        patients_status_list = PatientsStatusListHandler([1, 3, 1])
        patient_command = PatientCommands(dialog_with_user, patients_status_list)
        patient_command.patient_status_up()

        dialog_with_user.print_to_user_output.assert_called_with("Пациент выписан из больницы")
        assert patients_status_list.patients_status_list == [1, 1]

    def test_patient_status_up_discharge_fail(self):
        dialog_with_user = DialogWithUser(Console())
        dialog_with_user.ask_user_patient_id = MagicMock(return_value=2)
        dialog_with_user.ask_discharge_patient = MagicMock(return_value=False)
        dialog_with_user.print_to_user_output = MagicMock()

        patients_status_list = PatientsStatusListHandler([1, 3, 1])
        patient_command = PatientCommands(dialog_with_user, patients_status_list)
        patient_command.patient_status_up()

        dialog_with_user.print_to_user_output.assert_called_with("Пациент остался в статусе: 'Готов к выписке'")
        assert patients_status_list.patients_status_list == [1, 3, 1]
