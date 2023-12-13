from hospital_application import HospitalApplication
from logic.controller.dialog_with_user import DialogWithUser
from logic.use_case.patient_commands import PatientCommands
from logic.core.patients_status_list_handler import PatientsStatusListHandler
from logic.use_case.statistics_commands import StatisticsCommands
from tests.utils.mock_console import MockConsole


def prepare_application(console, patients_list):
    dialog_with_user = DialogWithUser(console)
    patients_status_list = PatientsStatusListHandler(patients_list)
    statistics_commands = StatisticsCommands(dialog_with_user, patients_status_list)
    patient_commands = PatientCommands(dialog_with_user, patients_status_list)
    return HospitalApplication(dialog_with_user, statistics_commands, patient_commands)


class TestsHospitalApplication:

    def test_unknown_command(self):
        mock_console = MockConsole()
        application = prepare_application(mock_console, [])

        mock_console.add_expected_message_and_returned_input("Введите команду: ", "команда")
        mock_console.add_output_message("Неизвестная команда! Попробуйте еще раз!")
        mock_console.add_expected_message_and_returned_input("Введите команду: ", "stop")
        mock_console.add_output_message("Сеанс завершён")

        application.start_operation()

        mock_console.assert_no_mocks_left()

    def test_patient_id_invalid_input(self):

        mock_console = MockConsole()
        application = prepare_application(mock_console, [1, 1])
        mock_console.add_expected_message_and_returned_input("Введите команду: ", "узнать статус пациента")
        mock_console.add_expected_message_and_returned_input("Введите ID пациента:", "-1")
        mock_console.add_output_message("Ошибка! ID пациента должно быть числом(целым и положительным)")

        mock_console.add_expected_message_and_returned_input("Введите команду: ", "узнать статус пациента")
        mock_console.add_expected_message_and_returned_input("Введите ID пациента:", "0")
        mock_console.add_output_message("Ошибка! ID пациента должно быть числом(целым и положительным)")

        mock_console.add_expected_message_and_returned_input("Введите команду: ", "узнать статус пациента")
        mock_console.add_expected_message_and_returned_input("Введите ID пациента:", "two")
        mock_console.add_output_message("Ошибка! ID пациента должно быть числом(целым и положительным)")

        mock_console.add_expected_message_and_returned_input("Введите команду: ", "узнать статус пациента")
        mock_console.add_expected_message_and_returned_input("Введите ID пациента:", "3")
        mock_console.add_output_message("Ошибка! Нет пациента с таким ID")

        mock_console.add_expected_message_and_returned_input("Введите команду: ", "stop")
        mock_console.add_output_message("Сеанс завершён")

        application.start_operation()

        mock_console.assert_no_mocks_left()