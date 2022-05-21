import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from resource_path import Resource_path

class DeepyL():
    def __init__(self):
        self.load_url = "https://www.deepl.com/translator"
        self.in_sel = "//textarea"
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
            options.add_argument('--headless')
            service = webdriver.firefox.service.Service(executable_path=Resource_path("./driver/geckodriver.exe"), log_path=os.path.devnull)
            self.driver = webdriver.Firefox(service=service, options=options)
        except:
            try:
                options = webdriver.chrome.options.Options()
                options.add_experimental_option("excludeSwitches", ["enable-logging"])
                options.add_argument("--headless")
                service = webdriver.chrome.service.Service(executable_path=Resource_path("./driver/chromedriver.exe"))
                self.driver = webdriver.Chrome(service=service,options=options)
            except:
                options = webdriver.edge.options.Options()
                options.add_argument('--headless')
                options.add_experimental_option('excludeSwitches', ['enable-logging'])
                service = webdriver.edge.service.Service(executable_path=Resource_path("./driver/msedgedriver.exe"))
                self.driver = webdriver.Edge(service=service, options=options)
                
        self.driver.get(self.load_url)

    def close(self):
        self.driver.close()

    def io(self, text):
        self.driver.find_element(By.XPATH,self.in_sel).clear()   #インプット側をクリアする
        self.driver.find_element(By.XPATH,self.in_sel).send_keys(text)

        tmp = ""
        cnt = 10
        while (cnt > 0):
            try:
                result = self.driver.find_element(By.ID,self.out_sel).get_attribute("textContent")
                result = result.replace("\r\n","").replace("\n","")
                if (tmp != result):
                    tmp = result
                elif(tmp != ""):
                    break
            except:
                pass
            cnt = cnt - 1
            time.sleep(1)
        return result
