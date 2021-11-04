import unittest
from pandas._testing import assert_frame_equal
from web_traffic_transformation import *

class WebTransformationTest(unittest.TestCase):


    def test_bad_filename(self):
        with self.assertRaises(SystemExit):
            get_raw_data('https://public.wiwdata.com/engineering-challenge/data/', ['abc'], '.csv', 0)

    def test_correct_pivoting(self):
        df_sample = pd.read_csv('raw_sample.csv')
        df_sample_pivoted = pivot_raw_data(df_sample)
        df_sample_pivoted.to_csv('sample_pivoted.csv')

        df_pivot_expected = pd.read_csv('pivot_expected.csv')
        df_sample_actual = pd.read_csv('sample_pivoted.csv')

        assert_frame_equal(df_sample_actual, df_pivot_expected)

    def test_empty_dataframe_pivoting(self):
        with self.assertRaises(SystemExit):
            df = pd.DataFrame()
            pivot_raw_data(df)

if __name__ == '__main__':
    unittest.main()
