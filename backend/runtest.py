import unittest
import server
import pandas as pd
from pandas.testing import assert_frame_equal
from io import StringIO

class TestPayrollProcessor(unittest.TestCase):
    def test_all(self):
        test_data = pd.DataFrame({
            'name': ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'c', 'c'],
            'hours': [24, 6.9, 4.2, 8, 8, 8, 8, 24, 24]
        })
        expected_response = pd.DataFrame({
            'name': ['a', 'b', 'c'], 
            'hours': [27.1, 24.0, 16.0]
        })

        test_data_csv = StringIO()
        test_data.to_csv(test_data_csv, index=False)
        test_data_csv.seek(0)

        test_response = server.process_payroll(test_data_csv)

        assert_frame_equal(pd.read_csv(test_response), expected_response)


if __name__ == '__main__':
    unittest.main()

