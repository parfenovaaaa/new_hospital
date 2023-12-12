from logic.utils.console import Console


class MockConsole(Console):
    def __init__(self):
        self._output_msg_list = []
        self._input_msg_list = []
        self._input_value_list = []

    def output(self, msg: str) -> None:
        try:
            assert msg == self._output_msg_list[0], f"\nActual output message: {msg}, \nexpected: {self._output_msg_list[0]}"
            print(msg)
            self._output_msg_list.pop(0)
        except IndexError:
            raise AssertionError("No output messages")

    def add_output_message(self, msg: str):
        self._output_msg_list.append(msg)

    def add_expected_message_and_returned_input(self, message: str, input_value: str) -> None:
        self._input_msg_list.append(message)
        self._input_value_list.append(input_value)

    def input(self, msg: str):
        try:
            mock_msg = self._input_msg_list.pop(0)
            assert msg == mock_msg, f"\nActual input message: {msg}, \nexpected: {mock_msg}"
            return self._input_value_list.pop(0)
        except IndexError:
            raise AssertionError("No input messages")

    def assert_no_mocks_left(self):
        errors = []
        if not self._output_msg_list:
            errors.append(f"Output message left: {self._output_msg_list}")
        if not self._input_msg_list:
            errors.append(f"Input message left: {self._input_msg_list}")
        if not self._input_value_list:
            errors.append(f"Input value left: {self._input_value_list}")
        assert errors, errors
