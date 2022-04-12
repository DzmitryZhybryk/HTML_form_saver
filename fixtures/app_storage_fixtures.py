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
    return WorkWithCSV(test_data.get("object_name"))
