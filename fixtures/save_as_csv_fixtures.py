import os

import pytest
import yaml

from csv_storage_app.save_as_csv import WorkWithCSV


@pytest.fixture(scope="module")
def global_test_data(request) -> dict:
    """
    Fixture reads the yaml file and returns parameters depending on the test that called it
    :return: dict with parameters
    """
    with open(f"{request.fspath.dirname}/data.yaml") as file:
        return yaml.safe_load(file)


@pytest.fixture
def test_data(global_test_data, request) -> dict:
    """
    Fixture reads the yaml file and returns parameters depending on the test that called it
    :return: dict with parameters
    """
    return global_test_data.get(request.function.__name__)


@pytest.fixture
def work_with_csv_object(test_data: dict) -> WorkWithCSV:
    """
    Fixture create new WorkWithCSV object
    :param test_data: dict with parameters
    :return: WorkWithCSV object
    """
    return WorkWithCSV(test_data.get("new_file_name"))


@pytest.fixture
def new_file_with_data(work_with_csv_object: WorkWithCSV, test_data: dict):
    """
    Fixture creates new CSV file and adds the data there
    :param test_data: dict with parameters
    :param work_with_csv_object: WorkWithCSV object
    """
    return work_with_csv_object.add_head(test_data.get("test_data"))


@pytest.fixture
def more_data(work_with_csv_object: WorkWithCSV, test_data: dict):
    """
    Fixture adds data to the CSV file and deletes the file after work
    :param test_data: dict with parameters
    :param work_with_csv_object: WorkWithCSV object
    """
    work_with_csv_object.add_data(test_data.get("test_data"))
    yield
    os.remove(f"./{test_data.get('new_file_name')}.csv")
