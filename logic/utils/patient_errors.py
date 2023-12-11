
class PatientIdNotIntegerOrNotPositive(Exception):
    def __init__(self):
        self.message = "Ошибка! ID пациента должно быть числом(целым и положительным)"


class PatientIdNotExist(Exception):
    def __init__(self):
        self.message = "Ошибка! Нет пациента с таким ID"
