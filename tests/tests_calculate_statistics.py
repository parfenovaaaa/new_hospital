from collections import Counter

from logic.core.patients_status_list_handler import PatientsStatusListHandler
from logic.use_case.statistics_commands import StatisticsCommands


class TestsCalculateStatistics:
    def test_get_statics_data_all_status(self):
        statistics = {0: 1, 1: 1, 2: 1, 3: 1}
        amount = 4
        patients_status_list = PatientsStatusListHandler([2, 0, 1, 3])
        statistics_command = StatisticsCommands(patients_status_list)
        actual_msg = statistics_command._create_calculate_statistics_output(Counter(statistics), amount)
        assert actual_msg == (
            "В больнице сейчас 4 чел., из них:\n\tв статусе 'Тяжело болен': 1 чел.\n\tв статусе 'Болен': 1 чел."
            "\n\tв статусе 'Слегка болен': 1 чел.\n\tв статусе 'Готов к выписке': 1 чел."
        )

    def test_get_statics_data_two_status(self):
        statistics = {0: 2, 2: 1}
        amount = 3
        patients_status_list = PatientsStatusListHandler([2, 0, 0])
        statistics_command = StatisticsCommands(patients_status_list)
        actual_msg = statistics_command._create_calculate_statistics_output(Counter(statistics), amount)
        assert actual_msg == (
            "В больнице сейчас 3 чел., из них:\n\tв статусе 'Тяжело болен': 2 чел.\n\tв статусе 'Слегка болен': 1 чел."
        )
