import random

def get_random_number():
    return random.randint(1,10)


# The function to test
def check_random_number():
    number = get_random_number()
    if number > 5:
        return "Greater than 5"
    else:
        return "Less than or equal to 5"

import pytest
from unittest import mock


def test_check_random_number():
    with mock.patch('random.randint') as mock_randint:
        mock_randint.return_value = 7   # self.return value comes from the mock module and is the syntax to use to return the mock value
        result = check_random_number()
        assert result == "Greater than 5"

        mock_randint.return_value = 3
        result = check_random_number()
        assert result == "Less than or equal to 5"