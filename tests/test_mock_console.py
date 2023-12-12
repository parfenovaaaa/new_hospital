import pytest

from tests.utils.mockConsole import MockConsole


def test_input():
    console = MockConsole()
    console.add_expected_request_msg_and_return_input('Введите команду: ', 'узнать статус пациента')
    console.add_expected_request_msg_and_return_input('Введите ID пациента: ', '7')

    assert console.input('Введите команду: ') == 'узнать статус пациента'
    assert console.input('Введите ID пациента: ') == '7'


def test_input_when_invalid_request():
    console = MockConsole()
    console.add_expected_request_msg_and_return_input('Введите команду: ', 'для этого теста подходит любой ответ')

    with pytest.raises(AssertionError):
        console.input('Пожалуйста, введите команду: ')


def test_print():
    console = MockConsole()
    console.add_output_message('Статус пациента: "Болен"')
    console.add_output_message('Новый статус пациента: "Слегка болен"')

    console.output('Статус пациента: "Болен"')
    console.output('Новый статус пациента: "Слегка болен"')


def test_print_when_invalid_output_message():
    console = MockConsole()
    console.add_output_message('Статус пациента: "Болен"')

    with pytest.raises(AssertionError):
        console.output('Статус пациента: "Тяжело болен"')


def test_print_when_invalid_order_of_output_message():
    console = MockConsole()
    console.add_output_message('Первое сообщение')
    console.add_output_message('Второе сообщение')

    with pytest.raises(AssertionError):
        console.output('Второе сообщение')


def test_print_when_list_of_expected_messages_is_empty():
    console = MockConsole()
    console.add_output_message('Сообщение')

    console.output('Сообщение')

    with pytest.raises(AssertionError):
        console.output('Второе сообщение')


def test_not_verify_all_calls_have_been_made():
    console = MockConsole()
    console.add_expected_request_msg_and_return_input('Введите команду: ', 'узнать статус пациента')
    console.add_expected_request_msg_and_return_input('Введите ID пациента: ', '7')

    console.input('Введите команду: ')

    with pytest.raises(AssertionError):
        console.assert_called_mocks()


def test_not_verify_all_calls_have_been_made_error():
    console = MockConsole()
    console.add_expected_request_msg_and_return_input('Введите команду: ', 'узнать статус пациента')
    console.add_expected_request_msg_and_return_input('Введите ID пациента: ', '7')

    c1 = console.input('Введите команду: ')
    c2 = console.input('Введите ID пациента: ')

    console.assert_called_mocks()

    assert c1 == 'узнать статус пациента'
    assert c2 == '7'


def test_not_verify_all_calls_have_been_made_2():
    console = MockConsole()
    console.add_output_message('Первое сообщение')
    console.add_output_message('Второе сообщение')

    console.output('Первое сообщение')
    console.output('Второе сообщение')

    console.assert_called_mocks()


def test_not_verify_all_calls_have_been_made_2_error():
    console = MockConsole()
    console.add_output_message('Первое сообщение')
    console.add_output_message('Второе сообщение')

    console.output('Первое сообщение')

    with pytest.raises(AssertionError):
        console.assert_called_mocks()
