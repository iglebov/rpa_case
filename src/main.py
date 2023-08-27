from helpers.options import get_chrome_options
from excel.excel_worker import ExcelWorker
from data_base.db_worker import DBWorker
from undetected_chromedriver import Chrome
from helpers.fedresurs_worker import FedresursWorker
from helpers.kad_arbitr_worker import KadArbitrWorker
from helpers.da_data import get_dadata_info

if __name__ == "__main__":
    options = get_chrome_options()
    with Chrome(options=options) as driver:
        companies_info = {}
        dadata_companies_info = {}
        cases_info = {}
        companies_inns = ExcelWorker.get_companies_inns("name_of_your_file.xlsx")

        worker = FedresursWorker(driver)
        worker.prepare_environment()

        for company_inn in companies_inns:
            companies_info[company_inn] = worker.get_company_info(company_inn)
            dadata_companies_info[company_inn] = get_dadata_info(company_inn)

        worker = KadArbitrWorker(driver)
        worker.prepare_environment()

        cases_names = worker.get_cases_names(companies_info)
        for case_name in cases_names:
            cases_info[case_name] = worker.get_info_about_bankruptcy_case(case_name)

    db_worker = DBWorker(
        user="Your user",
        host="localhost",
        port="Your port",
        password="Your password",
        database="Your database",
    )

    for company_inn in companies_inns:
        db_worker.add_data_about_company(
            companies_info[company_inn], dadata_companies_info[company_inn]
        )

    for case_name in cases_names:
        db_worker.add_data_about_case(cases_info[case_name])

    db_worker.finish()
