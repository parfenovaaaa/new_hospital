from collections import Counter

from logic.patient_db import PatientsDB
from logic.statistics_commands import StatisticsCommands


class TestsCalculateStatistics:
    def test_get_statics_data_all_status(self):
        expected_statistics = {0: 1, 1: 1, 2: 1, 3: 1}
        expected_amount = 4
        db = PatientsDB([2, 0, 1, 3])
        statistics_command = StatisticsCommands(db)
        actual_msg = statistics_command._create_calculate_statistics_output(Counter(expected_statistics), expected_amount)
        assert actual_msg == (
            "В больнице сейчас 4 чел., из них:\n\tв статусе 'Тяжело болен': 1 чел.\n\tв статусе 'Болен': 1 чел."
            "\n\tв статусе 'Слегка болен': 1 чел.\n\tв статусе 'Готов к выписке': 1 чел."
        )

    def test_get_statics_data_two_status(self):
        expected_statistics = {0: 2, 2: 1}
        expected_amount = 3
        db = PatientsDB([2, 0, 0])
        statistics_command = StatisticsCommands(db)
        actual_msg = statistics_command._create_calculate_statistics_output(Counter(expected_statistics), expected_amount)
        assert actual_msg == (
            "В больнице сейчас 3 чел., из них:\n\tв статусе 'Тяжело болен': 2 чел.\n\tв статусе 'Слегка болен': 1 чел."
        )
