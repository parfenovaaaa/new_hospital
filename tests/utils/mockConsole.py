from logic.utils.console import Console


class MockConsole(Console):
    def __init__(self):
        self._request_msg_list_in = []
        self._input_data_list_in = []
        self._output_msg_list_in = []

        self._input_cont = 0
        self._print_cont = 0

        self._request_msg_list_out = []
        self._input_data_list_out = []
        self._output_msg_list_out = []

    def input(self, msg):
        try:
            if msg != self._request_msg_list_in[self._input_cont]:
                raise AssertionError
            data = self._input_data_list_in[self._input_cont]
            self._request_msg_list_out.append(self._request_msg_list_in[self._input_cont])
            self._input_data_list_out.append(data)
            self._input_cont += 1
            return data
        except IndexError:
            raise AssertionError

    def output(self, msg):
        try:
            if msg != self._output_msg_list_in[self._print_cont] or not self._output_msg_list_in:
                raise AssertionError
            print(self._output_msg_list_in[self._print_cont])
            self._output_msg_list_out.append(self._output_msg_list_in[self._print_cont])
            self._print_cont += 1
        except IndexError:
            raise AssertionError

    def add_expected_request_msg_and_return_input(self, request_msg, input_data):
        self._request_msg_list_in.append(request_msg)
        self._input_data_list_in.append(input_data)

    def assert_called_mocks(self):
        try:
            for request in self._request_msg_list_in:
                assert self._request_msg_list_out[self._request_msg_list_in.index(request)] == request
            for output_msg in self._output_msg_list_in:
                assert self._output_msg_list_out[self._output_msg_list_in.index(output_msg)] == output_msg
        except IndexError:
            raise AssertionError

    def add_output_message(self, msg):
        self._output_msg_list_in.append(msg)
