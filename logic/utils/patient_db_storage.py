from typing import List


class PatientDBStorage:
    def __init__(self, patients_db=None):
        self.patients_db = patients_db if patients_db else [1 for _ in range(0, 200)]

    def return_patients_status_list(self) -> List[int]:
        return self.patients_db
