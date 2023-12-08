from collections import Counter
from typing import Dict

from logic.patient_errors import PatientIdNotExist

PATIENT_STATUS = {
    0: "Тяжело болен",
    1: "Болен",
    2: "Слегка болен",
    3: "Готов к выписке",
}


class PatientsDB:
    def __init__(self, patients_db=None):
        self.patients_db = patients_db if patients_db else [1 for _ in range(0, 200)]

    def _get_patient_index(self, patient_id: int) -> int:
        try:
            index = patient_id - 1
            _ = self.patients_db[index]
            return index
        except IndexError:
            raise PatientIdNotExist()

    def get_patient_status_by_id(self, patient_id: int) -> str:
        return PATIENT_STATUS[self.patients_db[self._get_patient_index(patient_id)]]

    def make_patient_status_down(self, patient_id: int) -> None:
        index = self._get_patient_index(patient_id)
        self.patients_db[index] = self.patients_db[index] - 1

    def cake_make_patient_status_down(self, patient_id: int) -> bool:
        if self.patients_db[self._get_patient_index(patient_id)] == 0:
            return False
        else:
            return True

    def make_patient_status_up(self, patient_id: int) -> None:
        index = self._get_patient_index(patient_id)
        self.patients_db[index] = self.patients_db[index] + 1

    def cake_make_patient_status_up(self, patient_id: int) -> bool:
        if self.patients_db[self._get_patient_index(patient_id)] == 3:
            return False
        else:
            return True

    def discharge_patient(self, patient_id: int) -> None:
        self.patients_db.pop(self._get_patient_index(patient_id))

    def get_calculate_statistics_data(self) -> Dict:
        return {"statistics": Counter(self.patients_db), "patients_amount": len(self.patients_db)}
