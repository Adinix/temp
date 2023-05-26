from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import pygetwindow as gw
from pyperclip import paste
import json

from time import sleep


def get_urllist():

    def window_moveto(x = 9999, y = 9999, window_name = "Firefox"):
        window = gw.getWindowsWithTitle(window_name)[0]
        if window.isMinimized:
            window.restore()
        window.moveTo(x, y)

    file_list = list()

    #* options
    profile = FirefoxProfile(r'C:\Users\Faster\AppData\Roaming\Mozilla\Firefox\Profiles\9j85d37g.default')

    options = Options()

    options.set_preference("general.useragent.override", 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0')

    options.set_preference("dom.webdriver.enabled", False)

    # options.headless = True

    window_moveto()

    driver = webdriver.Firefox(executable_path=r'geckodriver.exe',
                                options=options, firefox_profile=profile)

    window_moveto()

    wait = WebDriverWait(driver, 5)

    url_list = list()

    with open('Temp.json', 'r') as f:
        url_list_temp = json.load(f)

    try:
        driver.get(url=url_list_temp[0])
        # sleep(999)

        music_index = 1
        while True:
            element = wait.until(EC.presence_of_element_located((By.XPATH, f'/html/body/ytmusic-app/ytmusic-app-layout/div[4]/ytmusic-browse-response/div[2]/div[4]/ytmusic-section-list-renderer/div[2]/ytmusic-playlist-shelf-renderer/div[1]/ytmusic-responsive-list-item-renderer[{music_index}]/ytmusic-menu-renderer/yt-button-shape/button')))
            music_index += 1

            driver.execute_script("arguments[0].scrollIntoView();", element)
            wait.until(EC.presence_of_element_located((By.XPATH, f'/html/body/ytmusic-app/ytmusic-app-layout/div[4]/ytmusic-browse-response/div[2]/div[4]/ytmusic-section-list-renderer/div[2]/ytmusic-playlist-shelf-renderer/div[1]/ytmusic-responsive-list-item-renderer[{music_index}]/ytmusic-menu-renderer/yt-button-shape/button'))).click()

            menu = wait.until(EC.presence_of_all_elements_located((By.ID, 'navigation-endpoint')))

            driver.execute_script("arguments[0].scrollIntoView();", menu[-1])
            wait.until(EC.presence_of_all_elements_located((By.ID, 'navigation-endpoint')))[-1].click()

            elemet = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/ytmusic-app/ytmusic-popup-container/tp-yt-paper-dialog/ytmusic-unified-share-panel-renderer/yt-third-party-network-section-renderer/div[2]/yt-copy-link-renderer/div/yt-button-renderer/yt-button-shape/button')))
            driver.execute_script("arguments[0].scrollIntoView();", element)
            wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/ytmusic-app/ytmusic-popup-container/tp-yt-paper-dialog/ytmusic-unified-share-panel-renderer/yt-third-party-network-section-renderer/div[2]/yt-copy-link-renderer/div/yt-button-renderer/yt-button-shape/button'))).click()
            url_list.append(paste())

            element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/ytmusic-app/ytmusic-popup-container/tp-yt-paper-dialog/ytmusic-unified-share-panel-renderer/div/tp-yt-paper-icon-button')))
            driver.execute_script("arguments[0].scrollIntoView();", element)
            wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/ytmusic-app/ytmusic-popup-container/tp-yt-paper-dialog/ytmusic-unified-share-panel-renderer/div/tp-yt-paper-icon-button'))).click()

            # print(url_list)
            with open('Temp.json', 'w') as f:
                json.dump(url_list, f, indent=4, ensure_ascii=False)

        # sleep(99)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

        try:
            window_moveto(x = 100, y = 100)
        except:
            window_moveto(x = 100, y = 100)


if __name__ == '__main__':
    get_urllist()