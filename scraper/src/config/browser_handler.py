import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

from selenium.webdriver.chrome.options import Options
from ..custom_downloader_middleware import CustomDownloaderMiddleware
from ..js_executor import JsExecutor


class BrowserHandler:
    @staticmethod
    def conf_need_browser(config_original_content, js_render):
        group_regex = re.compile(r'\(\?P<(.+?)>.+?\)')
        results = re.findall(group_regex, config_original_content)

        return len(results) > 0 or js_render

    @staticmethod
    def init(config_original_content, js_render, user_agent):
        driver = None

        if BrowserHandler.conf_need_browser(config_original_content,
                                            js_render):
            chrome_options = Options()
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('user-agent={0}'.format(user_agent))

            driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install(), options=chrome_options)
            CustomDownloaderMiddleware.driver = driver
            JsExecutor.driver = driver
        return driver

    @staticmethod
    def destroy(driver):
        # Start browser if needed
        if driver is not None:
            driver.quit()
            driver = None

        return driver
