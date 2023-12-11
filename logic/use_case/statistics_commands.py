from collections import Counter

from logic.core.patients_status_list_handler import PATIENT_STATUS, PatientsStatusListHandler


class StatisticsCommands:
    def __init__(self, patients_status_list: PatientsStatusListHandler):
        self.patients_status_list = patients_status_list

    def calculate_statistics(self) -> str:
        raw_data = self.patients_status_list.get_calculate_statistics_data()
        return self._create_calculate_statistics_output(raw_data["statistics"], raw_data["patients_amount"])

    @staticmethod
    def _create_calculate_statistics_output(counter: Counter, patient_count: int) -> str:
        count_list = [f"\n\tв статусе '{PATIENT_STATUS[i]}': {counter[i]} чел." for i in range(0, 4) if counter[i] > 0]
        return f"В больнице сейчас {patient_count} чел., из них:" + "".join(count_list)
