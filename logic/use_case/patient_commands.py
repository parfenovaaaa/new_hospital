from logic.controller.dialog_with_user import DialogWithUser
from logic.core.patients_status_list_handler import PatientsStatusListHandler
from logic.utils.patient_errors import PatientIdNotIntegerOrNotPositive, PatientIdNotExist


class PatientCommands:
    def __init__(self, dialog_with_user: DialogWithUser, patients_status_list: PatientsStatusListHandler):
        self._patients_status_list_handler = patients_status_list
        self._dialog_with_user = dialog_with_user

    def patient_status_down(self):
        try:
            patient_id = self._dialog_with_user.ask_user_patient_id()
            if self._patients_status_list_handler.check_possibility_of_patient_status_down(patient_id):
                self._patients_status_list_handler.make_patient_status_down(patient_id)
                status = self._patients_status_list_handler.get_patient_status_by_id(patient_id)
                self._dialog_with_user.print_to_user_output(f"Новый статус пациента: '{status}'")
            else:
                self._dialog_with_user.print_to_user_output(
                    "Ошибка. Нельзя понизить самый низкий статус(наши пациенты не умирают)")
        except (PatientIdNotIntegerOrNotPositive, PatientIdNotExist) as e:
            self._dialog_with_user.print_to_user_output(e.message)

    def patient_status_up(self):
        try:
            patient_id = self._dialog_with_user.ask_user_patient_id()
            if self._patients_status_list_handler.check_possibility_of_patient_status_up(patient_id):
                self._patients_status_list_handler.make_patient_status_up(patient_id)
                status = self._patients_status_list_handler.get_patient_status_by_id(patient_id)
                self._dialog_with_user.print_to_user_output(f"Новый статус пациента: '{status}'")
            else:
                if self._dialog_with_user.ask_user_to_discharge_patient():
                    self._patients_status_list_handler.discharge_patient(patient_id)
                    self._dialog_with_user.print_to_user_output("Пациент выписан из больницы")
                else:
                    status = self._patients_status_list_handler.get_patient_status_by_id(patient_id)
                    self._dialog_with_user.print_to_user_output(f"Пациент остался в статусе: '{status}'")
        except (PatientIdNotIntegerOrNotPositive, PatientIdNotExist) as e:
            self._dialog_with_user.print_to_user_output(e.message)

    def get_patient_status(self):
        try:
            patient_id = self._dialog_with_user.ask_user_patient_id()
            status = self._patients_status_list_handler.get_patient_status_by_id(patient_id)
            self._dialog_with_user.print_to_user_output(f"Статус пациента: '{status}'")
        except (PatientIdNotIntegerOrNotPositive, PatientIdNotExist) as e:
            self._dialog_with_user.print_to_user_output(e.message)

    def discharge_patient(self):
        try:
            patient_id = self._dialog_with_user.ask_user_patient_id()
            self._patients_status_list_handler.discharge_patient(patient_id)
            self._dialog_with_user.print_to_user_output("Пациент выписан из больницы")
        except (PatientIdNotIntegerOrNotPositive, PatientIdNotExist) as e:
            self._dialog_with_user.print_to_user_output(e.message)
