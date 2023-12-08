from collections import Counter

from logic.patient_db import PATIENT_STATUS, PatientsDB


class StatisticsCommands:
    def __init__(self, patients_db: PatientsDB):
        self.patients_db = patients_db

    def calculate_statistics(self) -> str:
        raw_data = self.patients_db.get_calculate_statistics_data()
        return self._create_calculate_statistics_output(raw_data["statistics"], raw_data["patients_amount"])

    @staticmethod
    def _create_calculate_statistics_output(counter: Counter, patient_count: int) -> str:
        count_list = [f"\n\tв статусе '{PATIENT_STATUS[i]}': {counter[i]} чел." for i in range(0, 4) if counter[i] > 0]
        return f"В больнице сейчас {patient_count} чел., из них:" + "".join(count_list)
