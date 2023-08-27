# Link to webpage 'Fedresurs'
FEDRESURS_WEBPAGE_LINK = "https://bankrot.fedresurs.ru/bankrupts?searchString="
# Link to webpage 'Kad Arbitr'
KAD_ARBITR_WEBPAGE_LINK = "https://kad.arbitr.ru"
# Default time for waiting element to load
DEFAULT_WAIT_FOR_ELEMENT_TIME = 4
# Default time for waiting search to complete
DEFAULT_WAIT_FOR_SEARCH_TIME = 2
DEFAULT_WAIT_FOR_WEBDRIVER = 10
FEDRESURS_XPATH_FOR_COOKIES_ACCEPT_BUTTON = (
    "/html/body/app-root/app-common-msg/div/div/app-cookie-disclaimer/div/div/button"
)
FEDRESURS_XPATH_FOR_COOKIES_CLOSE_BUTTON = (
    "/html/body/fedresurs-app/app-custom-common-msg/div/div/"
    + "app-cookie-disclaimer/div/div/span/img"
)
FEDRESURS_XPATH_FOR_INPUT_AREA = (
    "/html/body/app-root/div[1]/app-bankrupt/div/div[1]/div/app-bankrupt-form/div/form/"
    + "app-form-search-string/div/form/div/div/el-input/div/div/div/input"
)
KADARBITR_XPATH_FOR_INPUT_AREA = '//*[@id="sug-cases"]/div/input'
FEDRESURS_XPATH_FOR_MAGNIFIER = (
    "/html/body/app-root/div[1]/app-bankrupt/div/div[1]/div/app-bankrupt-form/div/form/"
    + "app-form-search-string/div/form/div/el-button/div/button"
)
KADARBITR_XPATH_FOR_FIND_BUTTON = '//*[@id="b-form-submit"]/div/button'
FEDRESURS_XPATH_FOR_RESULTS_COUNT = (
    "/html/body/app-root/div[1]/app-bankrupt/div/div[2]/div/"
    + "app-loader/div[1]/app-bankrupt-result/el-tab-panel/div[1]/ul/li[1]/div/span[2]"
)
FEDRESURS_XPATH_FOR_COMPANY_NAME = (
    "/html/body/app-root/div[1]/app-bankrupt/div/div[2]/div/app-loader/div[1]/"
    + "app-bankrupt-result/el-tab-panel/div[2]/el-tab[1]/div/div/app-loader/div[1]/"
    + "app-bankrupt-result-companies/app-bankrupt-result-card-company/div/div/div[1]/div[1]/span"
)
FEDRESURS_XPATH_FOR_COMPANY_OGRN = (
    "/html/body/app-root/div[1]/app-bankrupt/div/div[2]/div/app-loader/div[1]/"
    + "app-bankrupt-result/el-tab-panel/div[2]/el-tab[1]/div/div/app-loader/div[1]/"
    + "app-bankrupt-result-companies/app-bankrupt-result-card-company/div/div/div[1]/div[3]/div[2]/span[2]"
)
FEDRESURS_XPATH_FOR_COMPANY_INN = (
    "/html/body/app-root/div[1]/app-bankrupt/div/div[2]/div/app-loader/div[1]/"
    + "app-bankrupt-result/el-tab-panel/div[2]/el-tab[1]/div/div/app-loader/div[1]/"
    + "app-bankrupt-result-companies/app-bankrupt-result-card-company/div/div/div[1]/div[3]/div[1]/span[2]"
)
FEDRESURS_XPATH_FOR_FULL_COMPANY_INFO = (
    "/html/body/app-root/div[1]/app-bankrupt/div/div[2]/div/app-loader/div[1]/"
    + "app-bankrupt-result/el-tab-panel/div[2]/el-tab[1]/div/div/app-loader/div[1]/app-bankrupt-result-companies/"
    + "app-bankrupt-result-card-company/div/div/el-info-link/a/span"
)
FEDRESURS_XPATH_FOR_DOWNLOAD_FILE_BUTTON = (
    "/html/body/fedresurs-app/div[1]/company-card/div/div/div[1]/ul[1]/li[2]/a/i"
)
FEDRESURS_CLASS_FOR_BANKRUPTCY_CASES_HTML_TABLE = "info_table.bankrot_case"
KADARBITR_CLASS_FOR_JUDGE = "judge"
KADARBITR_CLASS_FOR_CASE = "num_case"
KADARBITR_XPATH_FOR_JUDGE_LOCATION = '//*[@id="b-cases"]/tbody/tr/td[2]/div/div[2]'
KADARBITR_XPATH_FOR_PLAINTIFF = (
    "/html/body/div[1]/div[1]/div[2]/dl/dd/div[4]/div/table/tbody"
    + "/tr/td[3]/div/div/span"
)
KADARBITR_XPATH_FOR_APPLICANTS = "/html/body/div[1]/div[1]/dl/dd/div[3]/div/div[1]/div[1]/table/tbody/tr/td[1]/div/ul"
KADARBITR_XPATH_FOR_THIRD_PARTIES = (
    "/html/body/div[1]/div[1]/dl/dd/div[3]/div/div[1]/div[1]/table/tbody/tr/td[3]/"
    + "div/ul"
)
KADARBITR_XPATH_FOR_OTHER_PARTIES = (
    "/html/body/div[1]/div[1]/dl/dd/div[3]/div/div[1]/div[1]/table/tbody/tr/td[4]/"
    + "div/ul"
)
FILE_NAME_INDEX = -1
DADATA_INFO_INDEX = 0
KADARBITR_CLASS_FOR_RESULTS_COUNT = "b-found-total"
KADARBITR_RESULTS_COUNT_INDEX = 1
POSTGRES_SELECT_FROM_COMPANIES_QUERY = """SELECT * FROM companies;"""
POSTGRES_SELECT_FROM_CASES_QUERY = """SELECT * FROM cases;"""
