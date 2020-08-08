import os
import time
from selenium import webdriver
from resource_path import Resource_path

class DeepyL():
    def __init__(self, lang):
        self.load_url = "https://www.deepl.com/" + lang + "/translator"
        self.in_sel = "#dl_translator > div.lmt__sides_container > div.lmt__side_container.lmt__side_container--source > div.lmt__textarea_container > div > textarea"
        self.out_sel = "#dl_translator > div.lmt__sides_container > div.lmt__side_container.lmt__side_container--target > div.lmt__textarea_container > div.lmt__translations_as_text > p > button.lmt__translations_as_text__text_btn"
        try:
            self.get()
        except:
            return False
        else:
            self.close()

    def get(self):
        try:
            options = webdriver.chrome.options.Options()
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            options.add_argument("--headless")
            self.driver = webdriver.Chrome(executable_path=Resource_path("./driver/chromedriver.exe"),options=options)
        except:
            options = webdriver.firefox.options.Options()
            options.add_argument("--headless")
            self.driver = webdriver.Firefox(executable_path=Resource_path("./driver/geckodriver.exe"),options=options,log_path=os.path.devnull)
        self.driver.get(self.load_url)

    def close(self):
        self.driver.close()

    def io(self, text):
        self.driver.find_element_by_css_selector(self.in_sel).clear()   #インプット側をクリアする
        self.driver.find_element_by_css_selector(self.in_sel).send_keys(text)

        tmp = ""
        while True:
            try:
                result = self.driver.find_element_by_css_selector(self.out_sel).get_attribute("textContent")
                if (tmp != result and len(result) != 1):
                    return result
                time.sleep(1)
            except:
                pass