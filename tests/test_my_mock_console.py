import pytest

from tests.utils.mockConsole import MockConsole


class TestMockConsole:
    def test_mock_console_output(self):
        console = MockConsole()
        console.add_output_message("command")
        console.add_output_message("second command")

        console.output("command")
        console.output("second command")

    def test_mock_console_output_no_command_setted(self):
        console = MockConsole()
        console.add_output_message("command")

        with pytest.raises(AssertionError):
            console.output("not command")

    def test_mock_console_output_another_command_setted(self):
        console = MockConsole()
        with pytest.raises(AssertionError):
            console.output("not command")

    def test_mock_console_input(self):
        console = MockConsole()
        console.add_expected_message_and_returned_input("command", "input")
        assert console.input("command") == "input"

    def test_mock_console_input_no_command_setted(self):
        console = MockConsole()
        with pytest.raises(AssertionError):
            console.input("command")

    def test_mock_console_input_another_command_setted(self):
        console = MockConsole()
        console.add_expected_message_and_returned_input("command", "input")
        with pytest.raises(AssertionError):
            console.input("not command")

    def test_mock_console_input_command_before_not_called(self):
        console = MockConsole()
        console.add_expected_message_and_returned_input("command", "input")
        console.add_expected_message_and_returned_input("not command", "input1")
        with pytest.raises(AssertionError):
            console.input("not command")

    def test_mock_console_all_done(self):
        console = MockConsole()
        console.add_expected_message_and_returned_input("command", "input")
        console.add_output_message("command")
        console.output("command")
        console.input("command")
        console.assert_no_mocks_left()

    def test_mock_console_all_done_error_output(self):
        console = MockConsole()
        console.add_expected_message_and_returned_input("command", "input")
        console.add_output_message("command")
        console.input("command")
        with pytest.raises(AssertionError) as e:
            console.assert_no_mocks_left()
            assert e.value.message == "Output message left: command"

    def test_mock_console_all_done_error_input(self):
        console = MockConsole()
        console.add_expected_message_and_returned_input("command", "input")
        console.add_output_message("command")
        console.output("command")
        with pytest.raises(AssertionError) as e:
            console.assert_no_mocks_left()
            assert e.value.message == ["Input message left: command", "Input value left: input"]
