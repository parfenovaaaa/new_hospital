from typing import Tuple


class MockConsole:
    def __init__(self):
        self._output_msg_list = []
        self._input_msg_list = []
        self._input_value_list = []

    def output(self, msg: str) -> None:
        assert len(self._output_msg_list) > 0, "No output messages"
        current_output_msg = self._get_current_output_msg()
        assert msg == current_output_msg, f"\nActual output message: {msg}, \nexpected: {current_output_msg}"

    def _get_current_output_msg(self) -> str:
        return self._output_msg_list.pop(0)

    def add_output_message(self, msg: str):
        self._output_msg_list.append(msg)

    def add_expected_message_and_returned_input(self, message: str, input_value: str) -> None:
        self._input_msg_list.append(message)
        self._input_value_list.append(input_value)

    def input(self, msg: str):
        assert len(self._input_msg_list) > 0, "No input messages"
        current_input_msg, current_input_value = self._get_current_input_msg_and_input_value()
        assert msg == current_input_msg, f"\nActual input message: {msg}, \nexpected: {current_input_msg}"
        return current_input_value

    def _get_current_input_msg_and_input_value(self) -> Tuple:
        return self._input_msg_list.pop(0), self._input_value_list.pop(0)

    def assert_no_messages_or_inputs_left(self):
        list_of_left_data = []
        if len(self._output_msg_list) > 0:
            list_of_left_data.append(f"Output message left: {self._output_msg_list}")
        if len(self._input_msg_list) > 0:
            list_of_left_data.append(f"Input message left: {self._input_msg_list}")
        if len(self._input_value_list) > 0:
            list_of_left_data.append(f"Input value left: {self._input_value_list}")
        assert not list_of_left_data, list_of_left_data
