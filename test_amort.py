import pytest
import amort


def test_graph_iteration():
    principal = float(19000)
    rate = float(.0474/12)
    payment = float(1624.28)
    interest = 0
    principal, interest = amort.calc_graph_iteration(principal, rate, payment)
    assert interest == 75.05, interest
    assert principal == 17450.77, principal


def test_convert_param_to_float_with_float():
    param = amort.convert_param_to_float(0.0)
    assert isinstance(param, float)


def test_convert_param_to_float_with_empty_string():
    param = amort.convert_param_to_float('')
    assert param == ''


def test_convert_param_to_float_with_string_as_integer():
    param = amort.convert_param_to_float('0')
    assert isinstance(param, float)
    assert param == 0.0


def test_format_rate_with_integer():
    rate = amort.format_rate(12)
    assert rate == 0.12/12


def test_format_rate_with_decimal():
    rate = amort.format_rate(.12)
    assert rate == 0.12/12


if __name__ == "__main__":
    test_graph_iteration()
    test_convert_param_to_float_with_float()
    test_convert_param_to_float_with_empty_string()
    test_convert_param_to_float_with_string_as_integer()
    test_format_rate_with_integer()
    test_format_rate_with_decimal()
