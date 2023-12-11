from unittest.mock import MagicMock

from logic.utils.console import Console
from logic.controller.dialog_with_user import DialogWithUser
from logic.use_case.patient_commands import PatientCommands
from logic.core.patients_status_list_handler import PatientsStatusListHandler


class TestDischargePatient:
    def test_discharge_patient(self):
        dialog_with_user = DialogWithUser(Console())
        dialog_with_user.ask_user_patient_id = MagicMock(return_value=2)
        dialog_with_user.print_to_user_output = MagicMock()

        patients_list = PatientsStatusListHandler([0, 1, 3])
        patients_command = PatientCommands(dialog_with_user, patients_list)
        patients_command.discharge_patient()
        dialog_with_user.print_to_user_output.assert_called_with("Пациент выписан из больницы")
        assert patients_list.patients_status_list == [0, 3]
