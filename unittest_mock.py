import math
from unittest import mock 
from unittest.mock import patch, Mock
import os

def tests_sin():
    print(math.sin(1))
    with patch('math.sin', return_value=2) as m:
        print(math.sin(1))

tests_sin()


def rename(old_full_path, full_path):
    os.rename(old_full_path, full_path)
    return full_path

@patch('os.rename', return_value=None)
@unittest_run_loop
    async def test(self, MockOsRename):
        """
        все оспользования os.rename внутри теста, заменятся на mockObj
        """

# Mock встроенной with open() 
# from unittest.mock import patch, mock_open
# @patch('builtins.open', mock_open(read_data="data"))
# 

