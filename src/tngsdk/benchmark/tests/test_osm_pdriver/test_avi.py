from unittest import mock
from unittest.mock import Mock
from unittest.mock import patch

from tngsdk.benchmark.tests.test_osm_pdriver.test_data import simple_function

def test_simple_function():
    result = simple_function()
    print(result)

@patch('tngsdk.benchmark.tests.test_osm_pdriver.test_data.simple_function')
def test_mock_simple_function(mock_simple_func):
    print(mock_simple_func)
    r = mock_simple_func()
    print(r)
    print(simple_function)
    result = simple_function()
    print(result)