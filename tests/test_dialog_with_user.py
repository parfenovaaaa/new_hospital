from unittest.mock import MagicMock

import pytest

from logic.utils.console import Console
from logic.controller.dialog_with_user import DialogWithUser
from logic.utils.patient_errors import PatientIdNotIntegerOrNotPositive


class TestDialogWithUser:
    @pytest.mark.parametrize("patient_id", [1, "201"])
    def test_ask_user_patient_id(self, patient_id):
        dialog_with_user = DialogWithUser(Console())
        dialog_with_user.ask_user_for_input = MagicMock(return_value=patient_id)
        result = dialog_with_user.ask_user_patient_id()
        assert result == int(patient_id)

    @pytest.mark.parametrize("patient_id", [-1, "two", 0])
    def test_ask_user_patient_id_with_error(self, patient_id):
        dialog_with_user = DialogWithUser(Console())
        dialog_with_user.ask_user_for_input = MagicMock(return_value=patient_id)
        with pytest.raises(PatientIdNotIntegerOrNotPositive) as e:
            dialog_with_user.ask_user_patient_id()
        assert e.value.message == "Ошибка! ID пациента должно быть числом(целым и положительным)"

    def test_print_to_user_output(self):
        console = Console()
        console.output = MagicMock()
        dialog_with_user = DialogWithUser(console)
        dialog_with_user.print_to_user_output("Input data")
        console.output.assert_called_with("Input data")

    def test_ask_user_for_input(self):
        console = Console()
        console.input = MagicMock(return_value="New string")
        dialog_with_user = DialogWithUser(console)
        actual_data = dialog_with_user.ask_user_for_input("Input data")
        console.input.assert_called_with("Input data")
        assert actual_data == "New string"

    @pytest.mark.parametrize("command", ["yes", "y", "да"])
    def test_ask_discharge_patient_yes(self, command):
        dialog_with_user = DialogWithUser(Console())
        dialog_with_user.ask_user_for_input = MagicMock(return_value=command)
        assert dialog_with_user.ask_user_to_discharge_patient()

    @pytest.mark.parametrize("command", ["ye", "no", "д", "нет"])
    def test_ask_discharge_patient_no(self, command):
        dialog_with_user = DialogWithUser(Console())
        dialog_with_user.ask_user_for_input = MagicMock(return_value=command)
        assert not dialog_with_user.ask_user_to_discharge_patient()
