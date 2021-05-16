import os
import time
from selenium import webdriver
from resource_path import Resource_path

class DeepyL():
    def __init__(self, lang):
        self.load_url = "https://www.deepl.com/" + lang + "/translator"
        self.in_sel = "//div[@id='dl_translator']/div[5]/div[3]/div[1]/div[2]/div/textarea"
        self.out_sel = "target-dummydiv"
        try:
            self.get()
        except:
            return False
        else:
            self.close()

    def get(self):
        try:
            options = webdriver.firefox.options.Options()
            options.add_argument("--headless")
            self.driver = webdriver.Firefox(executable_path=Resource_path("./driver/geckodriver.exe"),options=options,log_path=os.path.devnull)
        except:
            options = webdriver.chrome.options.Options()
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            options.add_argument("--headless")
            self.driver = webdriver.Chrome(executable_path=Resource_path("./driver/chromedriver.exe"),options=options)
        self.driver.get(self.load_url)

    def close(self):
        self.driver.close()

    def io(self, text):
        self.driver.find_element_by_xpath(self.in_sel).clear()   #インプット側をクリアする
        self.driver.find_element_by_xpath(self.in_sel).send_keys(text)

        tmp = ""
        cnt = 5
        while (cnt > 0):
            try:
                result = self.driver.find_element_by_id(self.out_sel).get_attribute("textContent")
                if (tmp != result and len(result) != 1):
                    tmp = result
                cnt = cnt - 1
                time.sleep(1)
            except:
                pass
        return result
