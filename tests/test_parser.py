from tests import mock_data
from lib.parser import get_attributes


def test_parser():
    result = get_attributes(mock_data.json_test_string, mock_data.test_fields)
    assert result == mock_data.expected_result
