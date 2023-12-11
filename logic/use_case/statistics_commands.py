from collections import Counter

from logic.controller.dialog_with_user import DialogWithUser
from logic.core.patients_status_list_handler import PATIENT_STATUS, PatientsStatusListHandler


class StatisticsCommands:
    def __init__(self, dialog_with_user: DialogWithUser,  patients_status_list: PatientsStatusListHandler):
        self.dialog_with_user = dialog_with_user
        self.patients_status_list = patients_status_list

    def calculate_statistics(self) -> None:
        statistics_data = self.patients_status_list.get_calculate_statistics_data()
        statistics = self._create_calculate_statistics_output(
            statistics_data["statistics"], statistics_data["patients_amount"])
        self.dialog_with_user.print_to_user_output(statistics)

    @staticmethod
    def _create_calculate_statistics_output(counter: Counter, patient_count: int) -> str:
        count_list = [f"\n\tв статусе '{PATIENT_STATUS[i]}': {counter[i]} чел." for i in range(0, 4) if counter[i] > 0]
        return f"В больнице сейчас {patient_count} чел., из них:" + "".join(count_list)
