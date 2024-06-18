from unittest import TestCase

import pandas as pd

from python_iccd_demo.main import from_dict


class TestFromDict(TestCase):
    def test_from_dict(self) -> None:
        data = {"col1": [1, 2], "col2": [3, 4]}

        expected_df = pd.DataFrame.from_records(data)

        result_df = from_dict(data)

        self.assertTrue(result_df.equals(expected_df))
