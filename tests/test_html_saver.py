import os

import pytest

from csv_storage_app.save_as_csv import WorkWithCSV


class TestAppStorage:

    def test_create_and_type_object(self, test_data: dict, work_with_csv_object):
        assert isinstance(work_with_csv_object, WorkWithCSV), f"object should be WorkWithCSV type"
        assert work_with_csv_object, f"object is not created"
        assert work_with_csv_object.file_name == test_data.get(
            'object_name'), f"new object should be have {test_data.get('object_name')} name"


class TestSaveAsCSV:

    def test_create_file(self, new_file_with_data, test_data: dict):
        assert os.path.isfile(f"./{test_data.get('new_file_name')}.csv"), f"file has not been created"

    @pytest.mark.parametrize("expected_result", [["new_data"]])
    def test_data_in_file_with_add_head_method(self, test_data: dict, expected_result):
        with open(f"{test_data.get('new_file_name')}.csv") as file:
            content = file.readlines()
            content = [line.rstrip() for line in content]
        assert content == expected_result, f"data has not been added"

    @pytest.mark.parametrize("expected_result", [["new_data", "more_data"]])
    def test_add_data_with_add_data_method(self, more_data, test_data: dict, expected_result):
        with open(f"{test_data.get('new_file_name')}.csv") as file:
            content = file.readlines()
            content = [line.rstrip() for line in content]
        assert content == expected_result, f"data has not been added"
