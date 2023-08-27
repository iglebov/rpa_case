import time
import os
from typing import Dict, Tuple, Union
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import number_of_windows_to_be
from src.excel.excel_worker import ExcelWorker
from selenium.webdriver.common.by import By
from src.helpers.consts import (
    FEDRESURS_WEBPAGE_LINK,
    DEFAULT_WAIT_FOR_ELEMENT_TIME,
    DEFAULT_WAIT_FOR_WEBDRIVER,
    FEDRESURS_XPATH_FOR_MAGNIFIER,
    DEFAULT_WAIT_FOR_SEARCH_TIME,
    FEDRESURS_XPATH_FOR_INPUT_AREA,
    FEDRESURS_XPATH_FOR_RESULTS_COUNT,
    FEDRESURS_XPATH_FOR_COOKIES_ACCEPT_BUTTON,
    FEDRESURS_XPATH_FOR_COOKIES_CLOSE_BUTTON,
    FEDRESURS_XPATH_FOR_COMPANY_NAME,
    FEDRESURS_XPATH_FOR_COMPANY_INN,
    FEDRESURS_XPATH_FOR_COMPANY_OGRN,
    FEDRESURS_CLASS_FOR_BANKRUPTCY_CASES_HTML_TABLE,
    FEDRESURS_XPATH_FOR_FULL_COMPANY_INFO,
    FEDRESURS_XPATH_FOR_DOWNLOAD_FILE_BUTTON,
    FILE_NAME_INDEX,
)


class FedresursWorker:
    def __init__(self, driver: Chrome):
        self.driver = driver
        self.driver.implicitly_wait(DEFAULT_WAIT_FOR_ELEMENT_TIME)
        self.input_area = None
        self.main_window = None

    def open_link(self) -> None:
        self.driver.get(FEDRESURS_WEBPAGE_LINK)
        self.main_window = self.driver.current_window_handle

    def prepare_environment(self) -> None:
        self.open_link()
        self.accept_cookies()
        self.get_input_area()

    def accept_cookies(self) -> None:
        try:
            self.driver.find_element(
                By.XPATH,
                FEDRESURS_XPATH_FOR_COOKIES_ACCEPT_BUTTON,
            ).click()
        except NoSuchElementException:
            pass

    def close_cookies(self) -> None:
        try:
            self.driver.find_element(
                By.XPATH,
                FEDRESURS_XPATH_FOR_COOKIES_CLOSE_BUTTON,
            ).click()
        except NoSuchElementException:
            pass

    def get_input_area(self) -> None:
        self.input_area = self.driver.find_element(
            By.XPATH,
            FEDRESURS_XPATH_FOR_INPUT_AREA,
        )

    def get_company_info(self, company_inn: str) -> Dict[str, Union[str, list]]:
        company_info = {}

        self.fill_input_area(company_inn)
        self.click_magnifier()
        time.sleep(DEFAULT_WAIT_FOR_SEARCH_TIME)
        results_count = self.get_results_count()
        if results_count == 1:
            name, ogrn, inn = self.get_data()
            company_info["name_fedresurs"] = name
            company_info["ogrn"] = ogrn
            company_info["inn"] = inn
            self.open_full_info()
            self.download_file()
            pdf_path = self.get_path_to_downloaded_pdf()
            company_info["bankruptcy_cases"] = self.get_bankruptcy_cases()
            company_info["pdf_path"] = pdf_path
            time.sleep(DEFAULT_WAIT_FOR_ELEMENT_TIME)
            self.finish_work_with_tab()
        else:
            company_info["inn"] = company_inn
        self.clear_input_area()
        return company_info

    def finish_work_with_tab(self):
        self.driver.close()
        self.driver.switch_to.window(self.main_window)

    def fill_input_area(self, text: str) -> None:
        self.input_area.send_keys(text)

    def clear_input_area(self) -> None:
        self.input_area.clear()

    def click_magnifier(self) -> None:
        self.driver.find_element(
            By.XPATH,
            FEDRESURS_XPATH_FOR_MAGNIFIER,
        ).click()

    def wait_for_pages_to_load(self) -> None:
        WebDriverWait(self.driver, DEFAULT_WAIT_FOR_WEBDRIVER).until(
            number_of_windows_to_be(2)
        )

    def switch_to_full_info_webpage(self) -> None:
        for window_handle in self.driver.window_handles:
            if window_handle != self.main_window:
                self.driver.switch_to.window(window_handle)
                break

    def get_results_count(self) -> int:
        try:
            results_count = self.driver.find_element(
                By.XPATH,
                FEDRESURS_XPATH_FOR_RESULTS_COUNT,
            ).text
            results_count = int(results_count)
        except (ValueError, NoSuchElementException):
            results_count = 0
        return results_count

    def get_data(self) -> Tuple[str, str, str]:
        name = self.get_name()
        ogrn = self.get_ogrn()
        inn = self.get_inn()
        return name, ogrn, inn

    def get_name(self) -> str:
        try:
            return self.driver.find_element(
                By.XPATH,
                FEDRESURS_XPATH_FOR_COMPANY_NAME,
            ).text.strip()
        except NoSuchElementException:
            return ""

    def get_ogrn(self) -> str:
        try:
            return self.driver.find_element(
                By.XPATH,
                FEDRESURS_XPATH_FOR_COMPANY_OGRN,
            ).text.strip()
        except NoSuchElementException:
            return ""

    def get_inn(self) -> str:
        try:
            return self.driver.find_element(
                By.XPATH,
                FEDRESURS_XPATH_FOR_COMPANY_INN,
            ).text.strip()
        except NoSuchElementException:
            return ""

    def get_bankruptcy_cases(self) -> list:
        try:
            html_table = self.driver.find_element(
                By.CLASS_NAME,
                FEDRESURS_CLASS_FOR_BANKRUPTCY_CASES_HTML_TABLE,
            ).get_attribute("outerHTML")
            data_frame = ExcelWorker.get_dataframe_from_html(html_table)
            return ExcelWorker.get_list_of_cases(data_frame)
        except NoSuchElementException:
            return []

    def open_full_info(self) -> None:
        self.driver.find_element(
            By.XPATH,
            FEDRESURS_XPATH_FOR_FULL_COMPANY_INFO,
        ).click()
        self.wait_for_pages_to_load()
        self.switch_to_full_info_webpage()
        self.close_cookies()

    def download_file(self) -> None:
        self.driver.find_element(
            By.XPATH,
            FEDRESURS_XPATH_FOR_DOWNLOAD_FILE_BUTTON,
        ).click()

    def get_path_to_downloaded_pdf(self) -> str:
        download_file_name = (
            self.driver.current_url.split("/")[FILE_NAME_INDEX] + ".pdf"
        )
        pdf_path = os.getcwd() + "/REPORTS/" + download_file_name
        return pdf_path
