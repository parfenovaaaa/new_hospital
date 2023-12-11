import pytest

from logic.core.patients_status_list_handler import PatientsStatusListHandler
from logic.utils.patient_errors import PatientIdNotExist


class TestPatientDB:
    def test_make_status_down(self):
        db = PatientsStatusListHandler([1, 1, 1])
        db.make_patient_status_down(2)
        assert db.patients_status_list == [1, 0, 1]

    def test_cake_make_status_down_success(self):
        db = PatientsStatusListHandler([2])
        actual = db.check_possibility_of_patient_status_down(1)
        assert actual

    def test_cake_make_status_down_fail(self):
        db = PatientsStatusListHandler([0])
        actual = db.check_possibility_of_patient_status_down(1)
        assert not actual

    def test_make_status_up(self):
        db = PatientsStatusListHandler([0, 0, 0])
        db.make_patient_status_up(2)
        assert db.patients_status_list == [0, 1, 0]

    def test_cake_make_status_up_true(self):
        db = PatientsStatusListHandler([2])
        actual = db.check_possibility_of_patient_status_up(1)
        assert actual

    def test_cake_make_status_down_false(self):
        db = PatientsStatusListHandler([3])
        actual = db.check_possibility_of_patient_status_up(1)
        assert not actual

    def test_discharge_patient(self):
        db = PatientsStatusListHandler([3, 1, 0])
        db.discharge_patient(2)
        assert db.patients_status_list == [3, 0]

    def test_calculate_statistics(self):
        db = PatientsStatusListHandler([2, 0, 1, 3])
        actual_msg = db.get_calculate_statistics_data()
        assert dict(actual_msg["statistics"]) == {0: 1, 1: 1, 2: 1, 3: 1}
        assert actual_msg["patients_amount"] == 4

    def test_get_patient_status_by_id(self):
        db = PatientsStatusListHandler([3, 1, 0])
        actual_msg = db.get_patient_status_by_id(2)
        assert actual_msg == "Болен"

    def test_get_patient_index(self):
        db = PatientsStatusListHandler([0, 3])
        actual = db._get_patient_index(2)
        assert actual == 1

    def test_get_patient_index_error(self):
        db = PatientsStatusListHandler([1])
        with pytest.raises(PatientIdNotExist) as e:
            db._get_patient_index(2)
            assert e.message == "Ошибка! Нет пациента с таким ID"
