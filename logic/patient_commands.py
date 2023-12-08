from logic.dialog_with_user import DialogWithUser
from logic.patient_db import PatientsDB
from logic.patient_errors import PatientIdNotIntegerOrNotPositive, PatientIdNotExist


class PatientCommands:
    def __init__(self, dialog_with_user: DialogWithUser, patients_db: PatientsDB):
        self.patients_db = patients_db
        self.dialog_with_user = dialog_with_user

    def patient_status_down(self):
        try:
            patient_id = self.dialog_with_user.get_patient_id()
            if self.patients_db.cake_make_patient_status_down(patient_id):
                self.patients_db.make_patient_status_down(patient_id)
                status = self.patients_db.get_patient_status_by_id(patient_id)
                self.dialog_with_user.send_msg_to_user(f"Новый статус пациента: '{status}'")
            else:
                self.dialog_with_user.send_msg_to_user(
                    "Ошибка. Нельзя понизить самый низкий статус(наши пациенты не умирают)")
        except (PatientIdNotIntegerOrNotPositive, PatientIdNotExist) as e:
            self.dialog_with_user.send_msg_to_user(e.message)

    def patient_status_up(self):
        try:
            patient_id = self.dialog_with_user.get_patient_id()
            if self.patients_db.cake_make_patient_status_up(patient_id):
                self.patients_db.make_patient_status_up(patient_id)
                status = self.patients_db.get_patient_status_by_id(patient_id)
                self.dialog_with_user.send_msg_to_user(f"Новый статус пациента: '{status}'")
            else:
                if self.dialog_with_user.ask_discharge_patient():
                    self.patients_db.discharge_patient(patient_id)
                    self.dialog_with_user.send_msg_to_user("Пациент выписан из больницы")
                else:
                    status = self.patients_db.get_patient_status_by_id(patient_id)
                    self.dialog_with_user.send_msg_to_user(f"Пациент остался в статусе: '{status}'")
        except (PatientIdNotIntegerOrNotPositive, PatientIdNotExist) as e:
            self.dialog_with_user.send_msg_to_user(e.message)

    def get_patient_status(self):
        try:
            patient_id = self.dialog_with_user.get_patient_id()
            status = self.patients_db.get_patient_status_by_id(patient_id)
            self.dialog_with_user.send_msg_to_user(f"Статус пациента: '{status}'")
        except (PatientIdNotIntegerOrNotPositive, PatientIdNotExist) as e:
            self.dialog_with_user.send_msg_to_user(e.message)

    def discharge_patient(self):
        try:
            patient_id = self.dialog_with_user.get_patient_id()
            self.patients_db.discharge_patient(patient_id)
            self.dialog_with_user.send_msg_to_user("Пациент выписан из больницы")
        except (PatientIdNotIntegerOrNotPositive, PatientIdNotExist) as e:
            self.dialog_with_user.send_msg_to_user(e.message)
