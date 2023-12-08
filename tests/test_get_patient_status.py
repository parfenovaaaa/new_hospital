from unittest.mock import MagicMock

from logic.dialog_with_user import DialogWithUser
from logic.patient_commands import PatientCommands
from logic.patient_db import PatientsDB


class TestGetPatientStatus:
    def test_get_patient_status(self):
        dialog_with_user = DialogWithUser()
        dialog_with_user.send_msg_to_user = MagicMock()

        db = PatientsDB([0, 1, 2, 3])
        patient_command = PatientCommands(dialog_with_user, db)

        dialog_with_user.get_patient_id = MagicMock(return_value=1)
        patient_command.get_patient_status()
        dialog_with_user.send_msg_to_user.assert_called_with("Статус пациента: 'Тяжело болен'")

        dialog_with_user.get_patient_id = MagicMock(return_value=2)
        patient_command.get_patient_status()
        dialog_with_user.send_msg_to_user.assert_called_with("Статус пациента: 'Болен'")

        dialog_with_user.get_patient_id = MagicMock(return_value=3)
        patient_command.get_patient_status()
        dialog_with_user.send_msg_to_user.assert_called_with("Статус пациента: 'Слегка болен'")

        dialog_with_user.get_patient_id = MagicMock(return_value=4)
        patient_command.get_patient_status()
        dialog_with_user.send_msg_to_user.assert_called_with("Статус пациента: 'Готов к выписке'")

    def test_patient_status_id_error_negative(self):
        dialog_with_user = DialogWithUser()

        dialog_with_user.get_msg_from_user = MagicMock(return_value=-2)
        dialog_with_user.send_msg_to_user = MagicMock()

        db = PatientsDB()
        patient_command = PatientCommands(dialog_with_user, db)
        patient_command.get_patient_status()
        dialog_with_user.send_msg_to_user.assert_called_with(
            "Ошибка! ID пациента должно быть числом(целым и положительным)"
        )

    def test_patient_status_id_error_string(self):
        dialog_with_user = DialogWithUser()

        dialog_with_user.get_msg_from_user = MagicMock(return_value="sdg")
        dialog_with_user.send_msg_to_user = MagicMock()

        db = PatientsDB()
        patient_command = PatientCommands(dialog_with_user, db)
        patient_command.get_patient_status()
        dialog_with_user.send_msg_to_user.assert_called_with(
            "Ошибка! ID пациента должно быть числом(целым и положительным)"
        )

    def test_patient_status_id_error_not_exist(self):
        dialog_with_user = DialogWithUser()

        dialog_with_user.get_msg_from_user = MagicMock(return_value=2)
        dialog_with_user.send_msg_to_user = MagicMock()

        db = PatientsDB([0])
        patient_command = PatientCommands(dialog_with_user, db)
        patient_command.get_patient_status()
        dialog_with_user.send_msg_to_user.assert_called_with("Ошибка! Нет пациента с таким ID")
