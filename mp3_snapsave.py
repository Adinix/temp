from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import json

from time import sleep

#! main
def download(pach_download=r'C:\Users\Faster\Desktop\Download'):

    def examination_file ():
        files = os.listdir(pach_download)

        switch = False

        for i in files:
            a = str(i)
            a = a.split('.')[-1]
            if a == 'part':
                print(f'Файл не полностью загружен: {i}')
                switch = True

        if not switch:
            return 'Finish!'

    def filename_savefrom_delete ():
        files = os.listdir(pach_download)

        for i in files:
            s = i
            s = s.replace('SnapSave.io - ', '')
            s = s.replace(' (128 kbps)', '')

            os.rename(rf'C:\Users\Faster\Desktop\Download\{i}', rf'C:\Users\Faster\Desktop\Download\{s}')

    #* options
    profile = FirefoxProfile(r'C:\Users\Faster\AppData\Roaming\Mozilla\Firefox\Profiles\9j85d37g.default')
    # Установите путь для сохранения загруженных файлов
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.dir", pach_download)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

    options = Options()

    options.set_preference("general.useragent.override", 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0')

    options.set_preference("dom.webdriver.enabled", False)

    options.headless = True

    driver = webdriver.Firefox(executable_path=r'geckodriver.exe',
                                options=options, firefox_profile=profile)

    url = r'https://snapsave.io/ru20/youtube-mp3'

    wait = WebDriverWait(driver, 5)

    q = 1

    with open('Temp.json', 'r') as f:
        url_list = json.load(f)

    try:
        
        for i in url_list:
            driver.get(url=url)

            input_url = wait.until(EC.presence_of_element_located((By.ID, 's_input')))
            input_url.send_keys(i)
            sleep(q)

            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-red'))).click()

            try:
                wait.until(EC.presence_of_element_located((By.ID, 'btn-action'))).click()
                sleep(q)
            except:
                continue
            wait.until(EC.presence_of_element_located((By.ID, 'asuccess'))).click()

        while True:
            if examination_file() == 'Finish!':
                break
            sleep(2)

        filename_savefrom_delete ()
        print("Finish!")
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    download()