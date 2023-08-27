import psycopg2

from typing import Dict, Union


class DBWorker:
    def __init__(self, user, host, port, password, database):
        self.connection = self.connect(user, host, port, password, database)

    @staticmethod
    def connect(user, host, port, password, database):
        return psycopg2.connect(
            user=user, host=host, port=port, password=password, database=database
        )

    def add_data_about_company(
        self,
        company_info: Dict[str, Union[str, list]],
        dadata_company_info: Dict[str, Union[str, dict]],
    ):
        postgres_insert_query = """INSERT INTO companies (
                inn, name_fedresurs, ogrn, bankruptcy_cases, pdf_path, name_full, name, fio, okato, oktmo, okpo, 
                address, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        record_to_insert = (
            company_info.get("inn"),
            company_info.get("name_fedresurs"),
            company_info.get("ogrn"),
            company_info.get("bankruptcy_cases"),
            company_info.get("pdf_path"),
            dadata_company_info.get("name_full"),
            dadata_company_info.get("name"),
            dadata_company_info.get("fio"),
            dadata_company_info.get("okato"),
            dadata_company_info.get("oktmo"),
            dadata_company_info.get("okpo"),
            dadata_company_info.get("address"),
            dadata_company_info.get("status"),
        )
        cursor = self.connection.cursor()
        cursor.execute(postgres_insert_query, record_to_insert)
        self.connection.commit()

    def add_data_about_case(
        self,
        case_info: Dict[str, Union[str, list]],
    ):
        postgres_insert_query = """INSERT INTO cases (case_name, judge, plaintiff, applicants, third_parties, other_parties)
                 VALUES (%s, %s, %s, %s, %s, %s);"""
        record_to_insert = (
            case_info.get("case_name"),
            case_info.get("judge"),
            case_info.get("plaintiff"),
            case_info.get("applicants"),
            case_info.get("third_parties"),
            case_info.get("other_parties"),
        )
        cursor = self.connection.cursor()
        cursor.execute(postgres_insert_query, record_to_insert)
        self.connection.commit()

    def finish(self):
        self.connection.close()
