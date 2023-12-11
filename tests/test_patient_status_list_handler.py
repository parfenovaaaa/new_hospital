import pytest

from logic.core.patients_status_list_handler import PatientsStatusListHandler
from logic.utils.patient_errors import PatientIdNotExist


class TestPatientsStatusListHandler:
    def test_make_status_down(self):
        patients_list = PatientsStatusListHandler([1, 1, 1])
        patients_list.make_patient_status_down(2)
        assert patients_list.patients_status_list == [1, 0, 1]

    @pytest.mark.parametrize("patient_status", [1, 2, 3])
    def test_check_possibility_of_patient_status_down_success(self, patient_status):
        patients_list = PatientsStatusListHandler([patient_status])
        assert patients_list.check_possibility_of_patient_status_down(1)

    def test_check_possibility_of_patient_status_down_fail(self):
        patients_list = PatientsStatusListHandler([0])
        assert not patients_list.check_possibility_of_patient_status_down(1)

    def test_make_status_up(self):
        patients_list = PatientsStatusListHandler([0, 0, 0])
        patients_list.make_patient_status_up(2)
        assert patients_list.patients_status_list == [0, 1, 0]

    @pytest.mark.parametrize("patient_status", [0, 1, 2])
    def test_check_possibility_of_patient_status_up_true(self, patient_status):
        patients_list = PatientsStatusListHandler([patient_status])
        assert patients_list.check_possibility_of_patient_status_up(1)

    def test_check_possibility_of_patient_status_up_false(self):
        patients_list = PatientsStatusListHandler([3])
        assert not patients_list.check_possibility_of_patient_status_up(1)

    def test_discharge_patient(self):
        patients_list = PatientsStatusListHandler([3, 1, 0])
        patients_list.discharge_patient(2)
        assert patients_list.patients_status_list == [3, 0]

    def test_calculate_statistics(self):
        patients_list = PatientsStatusListHandler([2, 0, 1, 3])
        actual_data = patients_list.get_calculate_statistics_data()
        assert dict(actual_data["statistics"]) == {0: 1, 1: 1, 2: 1, 3: 1}
        assert actual_data["patients_amount"] == 4

    @pytest.mark.parametrize("status, value", [
        ["Тяжело болен", 0],
        ["Болен", 1],
        ["Слегка болен", 2],
        ["Готов к выписке", 3],
    ])
    def test_get_patient_status_by_id(self, status, value):
        patients_list = PatientsStatusListHandler([3, value, 0])
        actual_status = patients_list.get_patient_status_by_id(2)
        assert actual_status == status

    def test_get_patient_index(self):
        patients_list = PatientsStatusListHandler([0, 3])
        actual = patients_list._get_patient_index(2)
        assert actual == 1

    def test_get_patient_index_error(self):
        patients_list = PatientsStatusListHandler([1])
        with pytest.raises(PatientIdNotExist) as e:
            patients_list._get_patient_index(2)
            assert e.value.message == "Ошибка! Нет пациента с таким ID"
