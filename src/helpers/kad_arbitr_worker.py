import time

from typing import Dict, Tuple, Union, List, Optional
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import number_of_windows_to_be
from selenium.webdriver.common.by import By
from src.helpers.consts import (
    KAD_ARBITR_WEBPAGE_LINK,
    DEFAULT_WAIT_FOR_ELEMENT_TIME,
    KADARBITR_XPATH_FOR_FIND_BUTTON,
    KADARBITR_XPATH_FOR_INPUT_AREA,
    KADARBITR_CLASS_FOR_JUDGE,
    KADARBITR_XPATH_FOR_JUDGE_LOCATION,
    KADARBITR_XPATH_FOR_PLAINTIFF,
    KADARBITR_XPATH_FOR_APPLICANTS,
    KADARBITR_CLASS_FOR_RESULTS_COUNT,
    KADARBITR_RESULTS_COUNT_INDEX,
    KADARBITR_CLASS_FOR_CASE,
    DEFAULT_WAIT_FOR_SEARCH_TIME,
    KADARBITR_XPATH_FOR_THIRD_PARTIES,
    KADARBITR_XPATH_FOR_OTHER_PARTIES,
)


class KadArbitrWorker:
    def __init__(self, driver: Chrome):
        self.driver = driver
        self.input_area = None
        self.main_window = None
        self.companies_inns = None

    def open_link(self) -> None:
        self.driver.get(KAD_ARBITR_WEBPAGE_LINK)
        self.main_window = self.driver.current_window_handle

    def prepare_environment(self) -> None:
        self.open_link()
        self.get_input_area()

    def get_input_area(self) -> None:
        self.input_area = self.driver.find_element(
            By.XPATH,
            KADARBITR_XPATH_FOR_INPUT_AREA,
        )

    def finish_work_with_tab(self) -> None:
        self.driver.close()
        self.driver.switch_to.window(self.main_window)

    def fill_input_area(self, text: str) -> None:
        self.input_area.send_keys(text)

    def clear_input_area(self) -> None:
        self.input_area.clear()

    def click_find_button(self) -> None:
        self.driver.find_element(
            By.XPATH,
            KADARBITR_XPATH_FOR_FIND_BUTTON,
        ).click()

    def wait_for_pages_to_load(self) -> None:
        WebDriverWait(self.driver, 10).until(number_of_windows_to_be(2))

    def switch_to_case_info_webpage(self) -> None:
        for window_handle in self.driver.window_handles:
            if window_handle != self.main_window:
                self.driver.switch_to.window(window_handle)
                break

    def get_results_count(self) -> int:
        try:
            results_count = self.driver.find_element(
                By.CLASS_NAME,
                KADARBITR_CLASS_FOR_RESULTS_COUNT,
            ).text
            results_count = int(results_count.split()[KADARBITR_RESULTS_COUNT_INDEX])
        except (ValueError, NoSuchElementException):
            results_count = 0
        return results_count

    def get_data(self) -> Tuple[str, str]:
        judge = self.get_judge()
        plaintiff = self.get_plaintiff()
        return judge, plaintiff

    def get_judge(self) -> str:
        try:
            name = self.driver.find_element(
                By.CLASS_NAME,
                KADARBITR_CLASS_FOR_JUDGE,
            ).text.strip()
        except NoSuchElementException:
            name = ""
        try:
            location = self.driver.find_element(
                By.XPATH,
                KADARBITR_XPATH_FOR_JUDGE_LOCATION,
            ).text.strip()
        except NoSuchElementException:
            location = ""
        return " ".join((name, location))

    def get_plaintiff(self) -> str:
        try:
            return self.driver.find_element(
                By.XPATH,
                KADARBITR_XPATH_FOR_PLAINTIFF,
            ).text.strip()
        except NoSuchElementException:
            return ""

    def get_info_about_bankruptcy_case(self, case: str) -> Dict[str, Union[str, list]]:
        case_info = {}

        self.fill_input_area(case)
        self.click_find_button()
        time.sleep(DEFAULT_WAIT_FOR_SEARCH_TIME)
        results_count = self.get_results_count()
        if results_count == 1:
            judge, plaintiff = self.get_data()
            case_info["case_name"] = case
            case_info["judge"] = judge
            case_info["plaintiff"] = plaintiff
            self.open_case_info()
            case_info["applicants"] = self.get_applicants()
            case_info["third_parties"] = self.get_third_parties()
            case_info["other_parties"] = self.get_other_parties()
            time.sleep(DEFAULT_WAIT_FOR_ELEMENT_TIME)
            self.finish_work_with_tab()
        self.clear_input_area()
        return case_info

    def open_case_info(self) -> None:
        self.driver.find_element(
            By.CLASS_NAME,
            KADARBITR_CLASS_FOR_CASE,
        ).click()
        self.wait_for_pages_to_load()
        self.switch_to_case_info_webpage()

    def get_applicants(self) -> List[Optional[str]]:
        try:
            html_list = self.driver.find_element(
                By.XPATH,
                KADARBITR_XPATH_FOR_APPLICANTS,
            )
            items = html_list.find_elements(By.TAG_NAME, "li")
            applicants_list = [item.text for item in items]
            return applicants_list
        except NoSuchElementException:
            return []

    def get_third_parties(self) -> List[Optional[str]]:
        try:
            html_list = self.driver.find_element(
                By.XPATH,
                KADARBITR_XPATH_FOR_THIRD_PARTIES,
            )
            items = html_list.find_elements(By.TAG_NAME, "li")
            third_parties = [item.text for item in items]
            return third_parties
        except NoSuchElementException:
            return []

    def get_other_parties(self) -> List[Optional[str]]:
        try:
            html_list = self.driver.find_element(
                By.XPATH,
                KADARBITR_XPATH_FOR_OTHER_PARTIES,
            )
            items = html_list.find_elements(By.TAG_NAME, "li")
            other_parties_list = [item.text for item in items]
            return other_parties_list
        except NoSuchElementException:
            return []

    @staticmethod
    def get_cases_names(companies_info: dict) -> List[Optional[str]]:
        cases_names = []
        cases_lists = [
            item.get("bankruptcy_cases", []) for item in companies_info.values()
        ]
        for cases_list in cases_lists:
            for case in cases_list:
                cases_names.append(case)
        return cases_names
