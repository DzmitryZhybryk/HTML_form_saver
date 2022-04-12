"""Storage module for app"""
import os

from save_as_csv import WorkWithCSV

from flask import request, Flask

app = Flask(__name__)


def work_file_object() -> WorkWithCSV:
    """
    Method create WorkWithCSV object
    :return: WorkWithCSV object
    """
    database_object = WorkWithCSV()
    return database_object


@app.route("/save-data/", methods=["GET", "POST"])
def add_data_to_file() -> None:
    """
    Rout add data to file
    """
    incoming_report = request.get_json()
    if not os.path.isfile('./new_file.csv'):
        work_file_object().add_head(incoming_report)
        work_file_object().add_data({value: key for key, value in incoming_report.items()})
    else:
        work_file_object().add_data({value: key for key, value in incoming_report.items()})


if __name__ == '__main__':
    app.run(host='172.16.238.5', port=5001)
