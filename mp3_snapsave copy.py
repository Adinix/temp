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
def main():
    def examination_file (pach, list):
        global examination_switch

        files = os.listdir(pach)

        switch = False

        for i in files:
            a = str(i)
            a = a.split('.')[-1]
            if a == 'part':
                s = i.split('.')[0]
                print(f'Файл не полностью загружен: {s}')
                switch = True

        for i in list:
            if not i in files:
                print(f"Файл {i} не удалось загрузить! Попробуйте сново")
                switch = True

        if not switch:
            examination_switch = False

    #* Variable
    pach_download = r'C:\Users\Faster\Desktop\Download'
    file_list = list()
    examination_switch = True

    #* options
    profile = FirefoxProfile(r'C:\Users\Faster\AppData\Roaming\Mozilla\Firefox\Profiles\9j85d37g.default')
    # Установите путь для сохранения загруженных файлов
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.dir", pach_download)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

    options = Options()

    options.set_preference("general.useragent.override", 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0')

    # options.set_preference("dom.webdriver.enabled", False)

    # options.headless = True

    driver = webdriver.Firefox(executable_path=r'C:\Users\Faster\Documents\my_python\school\selenium\firefoxdriver\Driver\windows_x64\geckodriver.exe',
                                options=options, firefox_profile=profile)

    url = r'https://snapsave.io/ru20/youtube-mp3'

    wait = WebDriverWait(driver, 30)

    q = 1

    with open('Temp.json', 'r') as f:
        url_list = json.load(f)

    try:
        
        for i in url_list:
            driver.get(url=url)
            # sleep(999)
            print(1)
            current_handle = driver.current_window_handle

            input_url = wait.until(EC.presence_of_element_located((By.ID, 's_input')))
            input_url.send_keys(i)
            sleep(q)

            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-red'))).click()
            print(2)

            # wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-red'))).click()
            # sleep(2)
            print(3)

            wait.until(EC.presence_of_element_located((By.ID, 'btn-action'))).click()
            sleep(q)
            print(4)

            wait.until(EC.presence_of_element_located((By.ID, 'asuccess'))).click()
            # sleep(1)
            # download_link = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/a')
            # download_link = download_link.get_attribute('href')
            print(5)

            # driver.execute_script(f"window.open('{download_link}', '_blank');")
            # print(6)

            # sleep(q)

            # Закрываем все прочие вкладки
            # all_handles = driver.window_handles
            # for handle in all_handles:
            #     if handle != current_handle:
            #         driver.switch_to.window(handle)
            #         driver.close()

            # driver.switch_to.window(current_handle)
            # print(7)

        # while examination_switch:
        #     examination_file(pach_download, file_list)
        #     sleep(2)

        print("Finish!")
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()



if __name__ == "__main__":
    main()