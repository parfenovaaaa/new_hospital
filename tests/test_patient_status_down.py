from unittest.mock import MagicMock

from logic.dialog_with_user import DialogWithUser
from logic.patient_commands import PatientCommands
from logic.patient_db import PatientsDB


class TestPatientStatusDown:
    def test_patient_status_down_success(self):
        dialog_with_user = DialogWithUser()

        dialog_with_user.get_patient_id = MagicMock(return_value=2)
        dialog_with_user.send_msg_to_user = MagicMock()

        db = PatientsDB([3, 3, 3])
        patient_command = PatientCommands(dialog_with_user, db)
        patient_command.patient_status_down()
        dialog_with_user.send_msg_to_user.assert_called_with("Новый статус пациента: 'Слегка болен'")

    def test_patient_status_down_fail(self):
        dialog_with_user = DialogWithUser()

        dialog_with_user.get_patient_id = MagicMock(return_value=2)
        dialog_with_user.send_msg_to_user = MagicMock()

        db = PatientsDB([3, 0, 3])
        patient_command = PatientCommands(dialog_with_user, db)
        patient_command.patient_status_down()
        dialog_with_user.send_msg_to_user.assert_called_with(
            "Ошибка. Нельзя понизить самый низкий статус(наши пациенты не умирают)"
        )
