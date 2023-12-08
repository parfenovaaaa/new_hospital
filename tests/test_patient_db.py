from logic.patient_db import PatientsDB
from logic.patient_errors import PatientIdNotExist


class TestPatientDB:
    def test_make_status_down(self):
        db = PatientsDB([3, 3, 3])
        db.make_patient_status_down(2)
        assert db.patients_db == [3, 2, 3]

    def test_cake_make_status_down_success(self):
        db = PatientsDB([1])
        actual = db.cake_make_patient_status_down(1)
        assert actual

    def test_cake_make_status_down_fail(self):
        db = PatientsDB([0])
        actual = db.cake_make_patient_status_down(1)
        assert not actual

    def test_make_status_up(self):
        db = PatientsDB([1, 1, 1])
        db.make_patient_status_up(2)
        assert db.patients_db == [1, 2, 1]

    def test_cake_make_status_up_true(self):
        db = PatientsDB([2])
        actual = db.cake_make_patient_status_up(1)
        assert actual

    def test_cake_make_status_down_false(self):
        db = PatientsDB([3])
        actual = db.cake_make_patient_status_up(1)
        assert not actual

    def test_discharge_patient(self):
        db = PatientsDB([1, 1, 1])
        db.discharge_patient(2)
        assert db.patients_db == [1, 1]

    def test_calculate_statistics(self):
        db = PatientsDB([2, 0, 1, 3])
        actual_msg = db.get_calculate_statistics_data()
        assert dict(actual_msg["statistics"]) == {0: 1, 1: 1, 2: 1, 3: 1}
        assert actual_msg["patients_amount"] == 4

    def test_get_patient_status_by_id(self):
        db = PatientsDB([2, 1, 2])
        actual_msg = db.get_patient_status_by_id(2)
        assert actual_msg == "Болен"

    def test_get_patient_index(self):
        db = PatientsDB([0, 3])
        actual = db._get_patient_index(2)
        assert actual == 1

    def test_get_patient_index_error(self):
        db = PatientsDB([1])
        try:
            db._get_patient_index(2)
            raise AssertionError
        except PatientIdNotExist as e:
            assert e.message == "Ошибка! Нет пациента с таким ID"
