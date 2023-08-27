from undetected_chromedriver import ChromeOptions


def get_chrome_options() -> ChromeOptions:
    options = ChromeOptions()
    prefs = dict()
    prefs["profile.default_content_settings.popups"] = 0
    prefs[
        "download.default_directory"
    ] = "/Users/Your name/rpa_case/src/REPORTS"
    options.add_experimental_option("prefs", prefs)
    return options
