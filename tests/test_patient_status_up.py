from unittest.mock import MagicMock

from logic.dialog_with_user import DialogWithUser
from logic.patient_commands import PatientCommands
from logic.patient_db import PatientsDB


class TestPatientStatusUp:
    def test_patient_status_up_success(self):
        dialog_with_user = DialogWithUser()

        dialog_with_user.get_patient_id = MagicMock(return_value=2)
        dialog_with_user.send_msg_to_user = MagicMock()

        db = PatientsDB([1, 1, 1])
        patient_command = PatientCommands(dialog_with_user, db)
        patient_command.patient_status_up()
        dialog_with_user.send_msg_to_user.assert_called_with("Новый статус пациента: 'Слегка болен'")

    def test_patient_status_up_discharge_success(self):
        dialog_with_user = DialogWithUser()

        dialog_with_user.get_patient_id = MagicMock(return_value=2)
        dialog_with_user.ask_discharge_patient = MagicMock(return_value=True)
        dialog_with_user.send_msg_to_user = MagicMock()

        db = PatientsDB([1, 3, 1])
        patient_command = PatientCommands(dialog_with_user, db)
        patient_command.patient_status_up()
        dialog_with_user.send_msg_to_user.assert_called_with("Пациент выписан из больницы")

    def test_patient_status_up_discharge_fail(self):
        dialog_with_user = DialogWithUser()

        dialog_with_user.get_patient_id = MagicMock(return_value=2)
        dialog_with_user.ask_discharge_patient = MagicMock(return_value=False)
        dialog_with_user.send_msg_to_user = MagicMock()

        db = PatientsDB([1, 3, 1])
        patient_command = PatientCommands(dialog_with_user, db)
        patient_command.patient_status_up()
        dialog_with_user.send_msg_to_user.assert_called_with("Пациент остался в статусе: 'Готов к выписке'")
