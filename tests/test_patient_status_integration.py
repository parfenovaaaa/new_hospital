from collections import Counter
from unittest.mock import MagicMock

import pytest

from logic.controller.dialog_with_user import DialogWithUser
from logic.core.patients_status_list_handler import PatientsStatusListHandler
from logic.use_case.patient_commands import PatientCommands
from logic.use_case.statistics_commands import StatisticsCommands
from logic.utils.console import Console


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

    @pytest.mark.parametrize("invalid_index, message",
                             [[-1, "Ошибка! ID пациента должно быть числом(целым и положительным)"],
                              [0, "Ошибка! ID пациента должно быть числом(целым и положительным)"],
                              ["two", "Ошибка! ID пациента должно быть числом(целым и положительным)"],
                              [4, "Ошибка! Нет пациента с таким ID"]]
                             )
    def test_patient_status_up_discharge_with_invalid_index_error(self, invalid_index, message):
        dialog_with_user = DialogWithUser(Console())
        dialog_with_user.ask_user_for_input = MagicMock(return_value=invalid_index)
        dialog_with_user.print_to_user_output = MagicMock()

        patients_status_list = PatientsStatusListHandler([1, 3, 1])
        patient_command = PatientCommands(dialog_with_user, patients_status_list)

        patient_command.patient_status_up()
        dialog_with_user.print_to_user_output.assert_called_with(message)


class TestPatientStatusDown:
    def test_patient_status_down_success(self):
        dialog_with_user = DialogWithUser(Console())
        dialog_with_user.ask_user_patient_id = MagicMock(return_value=2)
        dialog_with_user.print_to_user_output = MagicMock()

        patients_status_list = PatientsStatusListHandler([1, 1, 1])
        patient_command = PatientCommands(dialog_with_user, patients_status_list)
        patient_command.patient_status_down()

        dialog_with_user.print_to_user_output.assert_called_with("Новый статус пациента: 'Тяжело болен'")
        assert patients_status_list.patients_status_list == [1, 0, 1]

    def test_patient_status_down_fail(self):
        dialog_with_user = DialogWithUser(Console())
        dialog_with_user.ask_user_patient_id = MagicMock(return_value=2)
        dialog_with_user.print_to_user_output = MagicMock()

        patients_status_list = PatientsStatusListHandler([3, 0, 3])
        patient_command = PatientCommands(dialog_with_user, patients_status_list)
        patient_command.patient_status_down()

        dialog_with_user.print_to_user_output.assert_called_with(
            "Ошибка. Нельзя понизить самый низкий статус(наши пациенты не умирают)"
        )
        assert patients_status_list.patients_status_list == [3, 0, 3]

    @pytest.mark.parametrize("invalid_index, message",
                             [[-1, "Ошибка! ID пациента должно быть числом(целым и положительным)"],
                              [0, "Ошибка! ID пациента должно быть числом(целым и положительным)"],
                              ["two", "Ошибка! ID пациента должно быть числом(целым и положительным)"],
                              [4, "Ошибка! Нет пациента с таким ID"]]
                             )
    def test_patient_status_down_with_invalid_index_error(self, invalid_index, message):
        dialog_with_user = DialogWithUser(Console())
        dialog_with_user.ask_user_for_input = MagicMock(return_value=invalid_index)
        dialog_with_user.print_to_user_output = MagicMock()

        patients_status_list = PatientsStatusListHandler([3, 0, 3])
        patient_command = PatientCommands(dialog_with_user, patients_status_list)
        patient_command.patient_status_down()

        dialog_with_user.print_to_user_output.assert_called_with(message)


class TestDischargePatient:
    @pytest.mark.parametrize("patients_db",
                             [[0, 0, 3],
                              [0, 1, 3],
                              [0, 2, 3],
                              [0, 3, 3]]
                             )
    def test_discharge_patient(self, patients_db):
        dialog_with_user = DialogWithUser(Console())
        dialog_with_user.ask_user_patient_id = MagicMock(return_value=2)
        dialog_with_user.print_to_user_output = MagicMock()

        patients_list = PatientsStatusListHandler(patients_db)
        patients_command = PatientCommands(dialog_with_user, patients_list)
        patients_command.discharge_patient()
        dialog_with_user.print_to_user_output.assert_called_with("Пациент выписан из больницы")
        assert patients_list.patients_status_list == [0, 3]

    @pytest.mark.parametrize("invalid_index, message",
                             [[-1, "Ошибка! ID пациента должно быть числом(целым и положительным)"],
                              [0, "Ошибка! ID пациента должно быть числом(целым и положительным)"],
                              ["two", "Ошибка! ID пациента должно быть числом(целым и положительным)"],
                              [4, "Ошибка! Нет пациента с таким ID"]]
                             )
    def test_discharge_patient_with_invalid_index_error(self, invalid_index, message):
        dialog_with_user = DialogWithUser(Console())
        dialog_with_user.ask_user_for_input = MagicMock(return_value=invalid_index)
        dialog_with_user.print_to_user_output = MagicMock()

        patients_list = PatientsStatusListHandler([1, 1, 1])
        patients_command = PatientCommands(dialog_with_user, patients_list)
        patients_command.discharge_patient()
        dialog_with_user.print_to_user_output.assert_called_with(message)


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

    @pytest.mark.parametrize("invalid_index, message",
                             [[-1, "Ошибка! ID пациента должно быть числом(целым и положительным)"],
                              [0, "Ошибка! ID пациента должно быть числом(целым и положительным)"],
                              ["two", "Ошибка! ID пациента должно быть числом(целым и положительным)"],
                              [4, "Ошибка! Нет пациента с таким ID"]]
                             )
    def test_patient_status_patient_with_invalid_index_error(self, invalid_index, message):
        dialog_with_user = DialogWithUser(Console())
        dialog_with_user.ask_user_for_input = MagicMock(return_value=invalid_index)
        dialog_with_user.print_to_user_output = MagicMock()

        patients_list = PatientsStatusListHandler([0])
        patient_command = PatientCommands(dialog_with_user, patients_list)
        patient_command.get_patient_status()

        dialog_with_user.print_to_user_output.assert_called_with(message)


class TestsCalculateStatistics:
    def test_get_statics_data_all_status(self):
        statistics = {0: 1, 1: 1, 2: 1, 3: 1}
        amount = 4
        dialog_with_user = DialogWithUser(Console())
        patients_status_list = PatientsStatusListHandler([2, 0, 1, 3])
        statistics_command = StatisticsCommands(dialog_with_user, patients_status_list)
        actual_msg = statistics_command._create_calculate_statistics_output(Counter(statistics), amount)
        assert actual_msg == (
            "В больнице сейчас 4 чел., из них:\n\tв статусе 'Тяжело болен': 1 чел.\n\tв статусе 'Болен': 1 чел."
            "\n\tв статусе 'Слегка болен': 1 чел.\n\tв статусе 'Готов к выписке': 1 чел."
        )

    def test_get_statics_data_two_status(self):
        statistics = {0: 2, 2: 1}
        amount = 3
        dialog_with_user = DialogWithUser(Console())
        patients_status_list = PatientsStatusListHandler([2, 0, 0])
        statistics_command = StatisticsCommands(dialog_with_user, patients_status_list)
        actual_msg = statistics_command._create_calculate_statistics_output(Counter(statistics), amount)
        assert actual_msg == (
            "В больнице сейчас 3 чел., из них:\n\tв статусе 'Тяжело болен': 2 чел.\n\tв статусе 'Слегка болен': 1 чел."
        )
