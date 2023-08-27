import pandas as pd
from pandas import DataFrame
from typing import List, Optional


class ExcelWorker:
    @staticmethod
    def read_file(path: str) -> DataFrame:
        return pd.read_excel(path)

    @staticmethod
    def get_list_of_inns(df: DataFrame) -> list:
        return [str(inn) for inn in df["ИНН"].to_list()]

    @staticmethod
    def get_list_of_cases(df: DataFrame) -> list:
        return df["Дело"].to_list()

    @staticmethod
    def get_dataframe_from_html(html: str) -> DataFrame:
        return pd.read_html(html)[0]

    @classmethod
    def get_companies_inns(cls, excel_file_path: str) -> List[Optional[str]]:
        data_frame = cls.read_file(excel_file_path)
        return cls.get_list_of_inns(data_frame)
