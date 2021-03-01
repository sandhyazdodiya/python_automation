from python_automation.calculator import Calculator
import pytest

NUMBER_1 = 3
NUMBER_2 = 5

@pytest.fixture()
def calculator():
    return Calculator()

@pytest.fixture()
def add_data_load():
    return [NUMBER_1, NUMBER_2, 8]


@pytest.fixture()
def subtract_data_load():
    return [NUMBER_1, NUMBER_2, 2]


@pytest.fixture()
def multiply_data_load():
    return [NUMBER_1, NUMBER_2, 15]


def test_calculator_sum(calculator,add_data_load):
    ans = calculator.add(add_data_load[0], add_data_load[1])
    assert ans == add_data_load[2]


def test_calculator_subtract(calculator, subtract_data_load):
    ans = calculator.subtract(subtract_data_load[0], subtract_data_load[1])
    assert ans == subtract_data_load[2]


def test_calculator_multiply(calculator, multiply_data_load):
    ans = calculator.multiply(multiply_data_load[0],multiply_data_load[1])
    assert ans == multiply_data_load[2]