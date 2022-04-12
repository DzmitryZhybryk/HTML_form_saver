"""Storage module for class WorkWithCSV"""
import csv
import logging


class WorkWithCSV:
    __INSTANCE = None

    def __new__(cls, *args, **kwargs):
        if cls.__INSTANCE is None:
            cls.__INSTANCE: WorkWithCSV = super().__new__(cls)
        return cls.__INSTANCE

    def __del__(self):
        WorkWithCSV.__file_connection = None

    def __init__(self, file_name: str = "new_file"):
        """
        Initialization method
        :param file_name: name for new file
        """
        self.file_name = file_name

    def add_head(self, column_names: str) -> None:
        """
        Method create head for new files
        :param column_names: str with column names
        """
        try:
            with open(f"{self.file_name}.csv", mode="a", encoding="utf-8") as w_file:
                file_writer = csv.writer(w_file, delimiter=',', lineterminator='\r')
                file_writer.writerow(column_names)
        except Exception as ex:
            logging.error(ex)

    def add_data(self, data: dict) -> None:
        """
        Method add data to file
        :param data: data for save
        """
        try:
            with open(f"{self.file_name}.csv", mode="a", encoding="utf-8") as w_file:
                file_writer = csv.writer(w_file, delimiter=',', lineterminator='\r')
                file_writer.writerow(data)
        except Exception as ex:
            logging.error(ex)
