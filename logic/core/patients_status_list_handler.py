from collections import Counter
from typing import Dict

from logic.utils.patient_errors import PatientIdNotExist

PATIENT_STATUS = {
    0: "Тяжело болен",
    1: "Болен",
    2: "Слегка болен",
    3: "Готов к выписке",
}


class PatientsStatusListHandler:
    def __init__(self, patients_status_list):
        self.patients_status_list = patients_status_list if patients_status_list else [1 for _ in range(0, 200)]

    def _get_patient_index(self, patient_id: int) -> int:
        try:
            index = patient_id - 1
            _ = self.patients_status_list[index]
            return index
        except IndexError:
            raise PatientIdNotExist()

    def get_patient_status_by_id(self, patient_id: int) -> str:
        return PATIENT_STATUS[self.patients_status_list[self._get_patient_index(patient_id)]]

    def make_patient_status_down(self, patient_id: int) -> None:
        index = self._get_patient_index(patient_id)
        self.patients_status_list[index] = self.patients_status_list[index] - 1

    def check_possibility_of_patient_status_down(self, patient_id: int) -> bool:
        return self.patients_status_list[self._get_patient_index(patient_id)] != 0

    def make_patient_status_up(self, patient_id: int) -> None:
        index = self._get_patient_index(patient_id)
        self.patients_status_list[index] = self.patients_status_list[index] + 1

    def check_possibility_of_patient_status_up(self, patient_id: int) -> bool:
        return self.patients_status_list[self._get_patient_index(patient_id)] != 3

    def discharge_patient(self, patient_id: int) -> None:
        self.patients_status_list.pop(self._get_patient_index(patient_id))

    def get_calculate_statistics_data(self) -> Dict:
        return {"statistics": Counter(self.patients_status_list), "patients_amount": len(self.patients_status_list)}
