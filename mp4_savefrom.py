from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import json

from time import sleep

#! main
def download(pach_download = r'C:\Users\Faster\Desktop\Download'):

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

    #* Variable
    file_list = list()

    #* options
    profile = webdriver.FirefoxProfile()
    # Установите путь для сохранения загруженных файлов
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.dir", pach_download)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

    options = webdriver.FirefoxOptions()

    options.set_preference("general.useragent.override", 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0')

    options.set_preference("dom.webdriver.enabled", False)

    options.headless = True

    driver = webdriver.Firefox(executable_path=r'geckodriver.exe',
                                options=options, firefox_profile=profile)

    url = r'https://ru.savefrom.net'

    wait = WebDriverWait(driver, 5)

    q = .5

    with open('Temp.json', 'r') as f:
        url_list = json.load(f)

    try:
        for i in url_list:
            driver.get(url=url)
            # sleep(999)
            current_handle = driver.current_window_handle

            input_url = wait.until(EC.presence_of_element_located((By.ID, 'sf_url')))
            input_url.send_keys(i)
            # sleep(q)

            wait.until(EC.presence_of_element_located((By.ID, 'sf_submit'))).click()
            sleep(2)
            
            button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[4]/div/div[1]/div[2]/div[2]/div[1]/a')))
            file_list.append(button.get_attribute('download'))
            button.click()
            sleep(q)

            # Закрываем все прочие вкладки
            all_handles = driver.window_handles
            for handle in all_handles:
                if handle != current_handle:
                    driver.switch_to.window(handle)
                    driver.close()

            driver.switch_to.window(current_handle)

        while True:
            sleep(3)
            if examination_file() == 'Finish!':
                break

        print("Finish!")
    except Exception as ex:
        return ex
    finally:
        driver.close()
        driver.quit()



if __name__ == "__main__":
    download()