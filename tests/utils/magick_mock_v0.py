from unittest.mock import MagicMock


class MockConsole:
    def __init__(self, console):
        self.console = console
        self.request_msg_list = []
        self.input_data_list = []
        self.output_msg_list = []

    def add_expected_request_msg_and_return_input(self, request_msg, input_data):
        self.request_msg_list.append(request_msg)
        self.console.input = MagicMock()
        self.input_data_list.append(input_data)
        self.console.input.side_effect = self.input_data_list

    def assert_called_mocks(self):
        for request in self.request_msg_list:
            assert self.console.input.call_args_list[self.request_msg_list.index(request)][0][0] == request
        for output_msg in self.output_msg_list:
            assert self.console.output.call_args_list[self.output_msg_list.index(output_msg)][0][0] == output_msg

    def add_output_message(self, msg):
        self.console.output = MagicMock()
        self.output_msg_list.append(msg)
