from unittest.mock import MagicMock

from logic.dialog_with_user import DialogWithUser
from logic.patient_commands import PatientCommands
from logic.patient_db import PatientsDB


class TestDischargePatient:
    def test_discharge_patient(self):
        dialog_with_user = DialogWithUser()

        dialog_with_user.get_patient_id = MagicMock(return_value=2)
        dialog_with_user.send_msg_to_user = MagicMock()

        db = PatientsDB([1, 1, 1])
        patient_command = PatientCommands(dialog_with_user, db)
        patient_command.discharge_patient()
        dialog_with_user.send_msg_to_user.assert_called_with("Пациент выписан из больницы")
