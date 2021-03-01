import pytest

@pytest.mark.usefixtures('data_load')
class TestDataLoad:
    # To use data you need to pass data_load fixture name in method
    def test_edit_profile(self, data_load):
        print(data_load[0])



