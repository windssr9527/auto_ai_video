from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.remote.remote_connection import RemoteConnection
from seleniumbase import Driver
import subprocess
import random


def start_copilot():

    num = 0
    text_list = []
    hot_list = []
    options = Options()
    driver = webdriver.Chrome(options=options)
    url = 'https://m.weibo.cn/p/index?containerid=106003type%3D25%26t%3D3%26disable_hot%3D1%26filter_type%3Drealtimehot&title=%E5%BE%AE%E5%8D%9A%E7%83%AD%E6%90%9C&show_cache_when_error=1&extparam=seat%3D1%26filter_type%3Drealtimehot%26dgr%3D0%26c_type%3D30%26lcate%3D1001%26mi_cid%3D100103%26cate%3D10103%26region_relas_conf%3D0%26pos%3D0_0%26display_time%3D1718515398%26pre_seqid%3D171851539867504138165&luicode=10000011&lfid=102803'
    driver.get(url)
    driver.implicitly_wait(15)
    hot_elements = driver.find_elements(By.CSS_SELECTOR, 'span.main-text.m-text-cut')
    print('a')
    for item in hot_elements:
        print('aaa')
        if num % 2 == 1:
            hot_list.append(item.text)
        if num >= 7:
            break
        num += 1
    print(hot_list)
    driver.close()
    # ===========================================================================


    shadow_input = None
    while shadow_input is None:

        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        user_data_dir = r"C:\Users\MSI\AppData\Local\Google\Chrome\User Data\Profile 3"
        remote_debugging_port = 9222

        subprocess.Popen([
            chrome_path,
            f"--remote-debugging-port={remote_debugging_port}",
            f"--user-data-dir={user_data_dir}"
        ])
        print('aaa')
        # 等待Chrome浏览器启动
        time.sleep(5)
        print('bbb')
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        print('ccc')
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.86 Safari/537.36"
        chrome_options.add_argument(f"user-agent={user_agent}")
        print('ddd')
        driver = webdriver.Chrome(options=chrome_options)
        print('執行drive')
        driver.get('https://copilot.microsoft.com/chats/Un5iiWkyD3ZEYVYw9xW81')
        print('執行網頁')
        driver.implicitly_wait(20)
        time.sleep(random.uniform(3, 5))
        shadow_input = driver.execute_script('''
            const firstShadowRoot = document.evaluate(
                `//*[@id="userInput"]`,
                document,
                null,
                XPathResult.FIRST_ORDERED_NODE_TYPE,
                null
            ).singleNodeValue; // 確保使用 singleNodeValue 獲取節點

            return firstShadowRoot ;
        ''')
        print(f"Script result: {shadow_input}")
        # if shadow_input is None:
        #     driver.close()
        time.sleep(1)
    shadow_num = 4
    hot_list_idx = 0
    for hot in hot_list:
        time.sleep(random.uniform(1, 3))
        # if hot_list_idx == 1:
        #     countinue_button = driver.execute_script(f'''
        #         const ZeroShadowRoot = document.querySelector("#b_sydConvCont > cib-serp").shadowRoot;
        #         const firstShadowRoot = ZeroShadowRoot.querySelector("#cib-conversation-main").shadowRoot;
        #         const secondElement = firstShadowRoot.querySelector("#cib-chat-main > cib-chat-turn").shadowRoot;
        #         const thirdElement = secondElement.querySelector("cib-message-group.response-message-group").shadowRoot;
        #         const fourElement = thirdElement.querySelector("cib-message:nth-child(4)").shadowRoot;
        #         const fiveElement = fourElement.querySelector("cib-shared > div > cib-muid-consent");
        #         return fiveElement ? fiveElement.shadowRoot : null;
        #     ''').find_element(By.CSS_SELECTOR, "div.get-started-btn-wrapper.inline-explicit > button")
        #     driver.execute_script("arguments[0].scrollIntoView(true);", countinue_button)
        #     countinue_button.click()

        shadow_input.send_keys(
            f"現在你是一名 短影音創作者 我會給你一個今天內中國社群媒體\"微博\"的時事話題 你必須先上網搜尋時事話題+\"微博热搜 24小时内\"的相關資料後 依照事件概要 事件結果 網路評價這三個文案大綱 依據這些大綱寫200字左右的文案 內容以中文輸出 只輸出文字 不要輸出多餘文字 首先第{hot_list_idx + 1}個話題:{hot}\n")

        time.sleep(30)
        retime = 0
        while (retime < 5):
            try:
                shadow_output = driver.find_element(By.CSS_SELECTOR,r'#app > main > div.h-dvh > div > div > div.min-h-\[calc\(100dvh-60px-var\(--composer-container-height\)\)\].sm\:min-h-\[calc\(100dvh-120px-var\(--composer-container-height\)\)\] > div.pb-6.inline-block.w-full.space-y-8 > div:nth-child(5)')
                print('shadow成功:',shadow_output)
                break
            except:
                retime += 1
                time.sleep(10)
                print(f"shadow重試第{retime}次")

        if retime == 5:
            return
        shadow_num += 1
        hot_list_idx += 1
        out_put_element_list=[]
        shadow_output_find_elements=shadow_output.find_elements(By.TAG_NAME,'p')
        for out_put_element in shadow_output_find_elements:
            if(len(shadow_output_find_elements)==1):
                break
            out_put_element_text=''.join(char for char in out_put_element.text if char <= '\u9fff')
            print('out_put_element_text:',out_put_element_text)
            out_put_element_list.append(out_put_element_text)

        if  out_put_element_list:
            text = ' '.join(out_put_element_list)
            text_list.append(text)
            print(text)
    print("hot end==========================")
    print(text_list)
    driver.close()
    time.sleep(3)
    invideo(text_list)
    # lumen5(hot_list, text_list)


def invideo(text_list):
    def click_if_can(css_value,driver):
        wait_time=0
        while wait_time<100:
            try:
                print("嘗試點擊")
                button = driver.find_element(By.CSS_SELECTOR, css_value)
                button.click()
                break
            except NoSuchElementException:
                print("按鈕尚未出現，繼續等待")
                time.sleep(1)  # 等待一秒後再嘗試
                wait_time+=1
                continue
            except ElementClickInterceptedException:
                print("另一個元素阻擋了按鈕，跳過該元素")
                break # 被阻擋時退出循環或根據需要繼續循環
            except Exception as e:
                print(f"發生未知錯誤: {e}")
                break
        if wait_time >= 100:
            raise TimeoutError('等待時間過長')

    # 启动Chrome浏览器
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    user_data_dir = r"C:\Users\MSI\AppData\Local\Google\Chrome\User Data\Profile 3"
    remote_debugging_port = 9222

    subprocess.Popen([
        chrome_path,
        f"--remote-debugging-port={remote_debugging_port}",
        f"--user-data-dir={user_data_dir}"
    ])

    # 等待Chrome浏览器启动
    time.sleep(5)

    # 使用Selenium连接到已启动的Chrome浏览器
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.86 Safari/537.36"
    chrome_options.add_argument(f"user-agent={user_agent}")
    # 增加 urllib3 的超时时间（默认为 120 秒）
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(360)  # 設置頁面加載超時時間（秒）
    driver.set_script_timeout(360)  # 設置腳本執行超時時間（秒）
    driver.implicitly_wait(10)
    try:
        driver.get("https://ai.invideo.io/workspace/c7839877-e5a2-47c3-9f70-c65727b50e97/v30-copilot")
        login_bottom=driver.find_element(By.CSS_SELECTOR,'#root > div > div.c-PJLV.c-cMmPCB > div.c-PJLV.c-gclpGc > div.c-PJLV.c-jbeQFI > div:nth-child(1) > button')
        print(login_bottom)
        login_bottom.click()
    except:
        pass
    driver.implicitly_wait(180)
    time.sleep(3)
    print('test1')
    for text_idx in range(len(text_list)):
        print('test2')
        driver.get("https://ai.invideo.io/workspace/c7839877-e5a2-47c3-9f70-c65727b50e97/v30-copilot")
        #driver.fullscreen_window()
        text_list[text_idx] = ''.join(c for c in text_list[text_idx] if ord(c) <= 0xFFFF)
        driver.find_element(By.CSS_SELECTOR,
                            '#root > div > div.c-PJLV.c-eLhtYl > div.c-PJLV.c-bOvwuE > div > div.c-PJLV.c-kqIzZB.c-kqIzZB-jloiqH-withContextBar-true > div > div:nth-child(1) > div > form > div.c-PJLV.c-kmjZLs > textarea').send_keys(
            text_list[text_idx])
        print('test3')
        driver.find_element(By.CSS_SELECTOR,
                            '#root > div > div.c-PJLV.c-eLhtYl > div.c-PJLV.c-bOvwuE > div > div.c-PJLV.c-kqIzZB.c-kqIzZB-jloiqH-withContextBar-true > div > div:nth-child(1) > div > form > div.c-PJLV.c-kSKXMG > button').click()
        driver.implicitly_wait(5)
        wait_time=0
        wait = WebDriverWait(driver, 1800)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                               '#root > div > div.c-PJLV.c-eLhtYl > div.c-PJLV.c-bOvwuE > div > div.c-PJLV.c-kqIzZB.c-kqIzZB-jloiqH-withContextBar-true > div > div > div.c-PJLV.c-ftcyyQ > div.c-PJLV.c-PJLV-ibXgGYd-css > div > div.c-PJLV.c-PJLV-igctWHd-css > button.c-fxmfvX.c-fxmfvX-jsiURM-variant-default.c-fxmfvX-iFmopW-size-default.c-WOVAc')))
        try :
            button = driver.find_element(By.CSS_SELECTOR, "button[value='1.0 minutes']")
            time.sleep(0.1)
        except:
            pass
        try:
            button = driver.find_element(By.CSS_SELECTOR, "button[value='youtube shorts']")
            time.sleep(0.1)
        except:
            pass
        driver.implicitly_wait(60)
        print('test4')
        driver.find_element(By.CSS_SELECTOR,
                            '#root > div > div.c-PJLV.c-eLhtYl > div.c-PJLV.c-bOvwuE > div > div.c-PJLV.c-kqIzZB.c-kqIzZB-jloiqH-withContextBar-true > div > div > div.c-PJLV.c-ftcyyQ > div.c-PJLV.c-PJLV-ibXgGYd-css > div > div.c-PJLV.c-PJLV-igctWHd-css > button.c-fxmfvX.c-fxmfvX-jsiURM-variant-default.c-fxmfvX-iFmopW-size-default.c-WOVAc').click()
        print('test5')
        try:
            driver.find_element(By.XPATH, "//button[div[text()='Continue']]").click()
        except:
            print('no such botton')
        try_time=0

        print('test5.1')
        while try_time < 10:
            try:
                print('test5.2')
                time.sleep(0.1)
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#root > div > div.c-PJLV.c-eLhtYl > div.c-PJLV.c-bOvwuE > div > div.c-PJLV.c-kqIzZB.c-kqIzZB-jloiqH-withContextBar-true > div > div > div > div.c-PJLV.c-imFJmV > div > div.c-PJLV.c-ZssbZ.c-PJLV-dhzjXW-layout-flex.c-PJLV-fGHEql-sizing-fullWidth.c-PJLV-knmidH-justify-between > div.c-PJLV.c-iFqkfs.c-PJLV-dhzjXW-layout-flex.c-PJLV-jroWjL-align-center > button.c-boeZgo.c-eZwudA.c-boeZgo-iRrDzT-size-s.c-boeZgo-ezrBnP-emphasis-low.c-boeZgo-ihXlSwn-css"))).click()
                print('test5.21')
                driver.find_element(By.CSS_SELECTOR,
                                    "#root > div > div.c-PJLV.c-eLhtYl > div.c-PJLV.c-bOvwuE > div > div.c-PJLV.c-kqIzZB.c-kqIzZB-jloiqH-withContextBar-true > div > div > div > div.c-PJLV.c-imFJmV > div > div.c-PJLV.c-ZssbZ.c-PJLV-dhzjXW-layout-flex.c-PJLV-fGHEql-sizing-fullWidth.c-PJLV-knmidH-justify-between > div.c-PJLV.c-iFqkfs.c-PJLV-dhzjXW-layout-flex.c-PJLV-jroWjL-align-center > button.c-boeZgo.c-eZwudA.c-boeZgo-iRrDzT-size-s.c-boeZgo-ezrBnP-emphasis-low.c-boeZgo-ihXlSwn-css").click()

                #driver.implicitly_wait(5)
                # try:
                #     print('test5.3')
                #     driver.find_element(By.XPATH, '//input[@placeholder="Give me a command to edit the video"]').send_keys("Don't add subtitles")
                # except:
                #     print('test5.4')
                #     driver.find_element(By.XPATH, '//magicbox-input[@placeholder="Give me a command to edit the video"]').send_keys("Don't add subtitles")
                #
                break
            except Exception as e:
                try_time += 1
                print(f'1報錯{e}: 重試第{try_time}次')
                try:
                    driver.find_element(By.CSS_SELECTOR,
                                        "button[value='stock_watermarks']").click()
                    break
                except Exception as e:
                    print(f'2報錯{e}: 重試第{try_time}次')

        print('test6')
        time.sleep(0.5)
        try:
            driver.find_element(By.CSS_SELECTOR,"button[value='normal']").click()
        except Exception as e:
            print(e)
        try:
            driver.find_element(By.CSS_SELECTOR,"button[value='720']").click()
        except Exception as e:
            print(e)
        print('test8')

        time.sleep(1)
        driver.find_element(By.XPATH, "//button[div[text()='Continue']]").click()
        print('test9')

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                               "#root > div > div.c-PJLV.c-eLhtYl.c-eLhtYl-btVtgV-autoGrow-true > div.c-PJLV.c-bOvwuE > div > div > div.c-PJLV.c-bPBhmT > div.c-PJLV.c-PJLV-iiPAZzK-css > div.c-PJLV.c-PJLV-irHuI-css > div.c-PJLV.c-PJLV-ifUnRPx-css > button.c-jaPdok.c-iPCGWA.c-jaPdok-icwXqlr-css")))
        time.sleep(10)
        print("成功下載影片")
    driver.close()


def lumen5(hot_list, text_list):
    idx = 0
    # 启动Chrome浏览器
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    user_data_dir = r"C:\Users\MSI\AppData\Local\Google\Chrome\User Data\Profile14_copy"
    remote_debugging_port = 9222

    subprocess.Popen([
        chrome_path,
        f"--remote-debugging-port={remote_debugging_port}",
        f"--user-data-dir={user_data_dir}"
    ])

    # 等待Chrome浏览器启动
    time.sleep(5)

    # 使用Selenium连接到已启动的Chrome浏览器
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://lumen5.com/app/?id=10875596#creator")
    # driver.fullscreen_window()
    driver.implicitly_wait(10)

    text_list[idx] = ''.join(c for c in text_list[idx] if ord(c) <= 0xFFFF)
    try:
        driver.find_element(By.CSS_SELECTOR,
                            'body > div.fade.full-screen-overlay.ai-script-modal.notranslate.modal-dialog-wrapper-fs.modal.show > div > div > div.p-l5-0.modal-body > div.d-flex.flex-row.justify-content-center > div > div.d-flex.options-container.mx-l5-auto.flex-column.mt-l5-16.mt-l5-lg-24 > div.d-flex.flew-row.flex-wrap > div.col.mb-l5-24.ai-voiceover-option > div').click()
    except:
        pass
    driver.implicitly_wait(300)
    print("test1")
    driver.find_element(By.CSS_SELECTOR,
                        'body > div.fade.full-screen-overlay.ai-script-modal.notranslate.modal-dialog-wrapper-fs.modal.show > div > div > div.p-l5-0.modal-body > div.d-flex.flex-row.overflow-hidden.justify-content-center.flex-grow-1.pt-l5-32.overflow-y-auto > div > div > div.top > div > div > div > button:nth-child(1)').click()
    driver.find_element(By.CSS_SELECTOR,
                        'body > div.fade.full-screen-overlay.ai-script-modal.notranslate.modal-dialog-wrapper-fs.modal.show > div > div > div.p-l5-0.modal-body > div.d-flex.flex-row.overflow-hidden.justify-content-center.flex-grow-1.pt-l5-32.overflow-y-auto > div > div > div.idea-form.overflow-y-auto.overflow-x-hidden > form > div:nth-child(2) > div.input-container > input').send_keys(
        hot_list[idx])
    # 事件概要 事件結果 網路評價
    driver.find_element(By.CSS_SELECTOR,
                        'body > div.fade.full-screen-overlay.ai-script-modal.notranslate.modal-dialog-wrapper-fs.modal.show > div > div > div.p-l5-0.modal-body > div.d-flex.flex-row.overflow-hidden.justify-content-center.flex-grow-1.pt-l5-32.overflow-y-auto > div > div > div.idea-form.overflow-y-auto.overflow-x-hidden > form > div:nth-child(3) > div:nth-child(2) > input').send_keys(
        "事件概要")
    driver.find_element(By.CSS_SELECTOR,
                        'body > div.fade.full-screen-overlay.ai-script-modal.notranslate.modal-dialog-wrapper-fs.modal.show > div > div > div.p-l5-0.modal-body > div.d-flex.flex-row.overflow-hidden.justify-content-center.flex-grow-1.pt-l5-32.overflow-y-auto > div > div > div.idea-form.overflow-y-auto.overflow-x-hidden > form > div:nth-child(3) > div:nth-child(3) > input').send_keys(
        "事件結果")
    driver.find_element(By.CSS_SELECTOR,
                        'body > div.fade.full-screen-overlay.ai-script-modal.notranslate.modal-dialog-wrapper-fs.modal.show > div > div > div.p-l5-0.modal-body > div.d-flex.flex-row.overflow-hidden.justify-content-center.flex-grow-1.pt-l5-32.overflow-y-auto > div > div > div.idea-form.overflow-y-auto.overflow-x-hidden > form > div:nth-child(3) > div:nth-child(4) > input').send_keys(
        "網路評價")
    print("test2")
    driver.find_element(By.CSS_SELECTOR,
                        'body > div.fade.full-screen-overlay.ai-script-modal.notranslate.modal-dialog-wrapper-fs.modal.show > div > div > div.p-l5-0.modal-body > div.d-flex.flex-row.overflow-hidden.justify-content-center.flex-grow-1.pt-l5-32.overflow-y-auto > div > div > div.top > div > div > div > button:nth-child(2)').click()
    driver.find_element(By.CSS_SELECTOR,
                        'body > div.fade.full-screen-overlay.ai-script-modal.notranslate.modal-dialog-wrapper-fs.modal.show > div > div > div.p-l5-0.modal-body > div.d-flex.flex-row.overflow-hidden.justify-content-center.flex-grow-1.pt-l5-32.overflow-y-auto > div > div > div.border.p-l5-24.pt-l5-12.mb-l5-32.d-flex.flex-column.flex-grow-1.overflow-y-auto.overflow-x-hidden.content-container > div.h-100.editor-container.mt-l5-8 > div.editor-input').send_keys(
        text_list[idx])

    driver.find_element(By.CSS_SELECTOR,
                        'body > div.fade.full-screen-overlay.ai-script-modal.notranslate.modal-dialog-wrapper-fs.modal.show > div > div > div.p-l5-0.modal-body > div.modal-footer.px-l5-40 > div > button').click()
    # driver.find_element(By.CSS_SELECTOR,'<button type="button" class="lumen5-button btn btn-rounded btn-primary btn-md"><i class="material-symbols-outlined me-l5-4">auto_awesome</i><span>Continue</span></button>').click()
    wait = WebDriverWait(driver, 1200)
    driver.find_element(By.CSS_SELECTOR,
                        'body > div.fade.full-screen-overlay.ai-script-modal.notranslate.modal-dialog-wrapper-fs.modal.show > div > div > div.p-l5-0.modal-body > div.modal-footer.px-l5-40 > div > div:nth-child(2) > button').click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#publish-button')))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                           '#react-root > div.dashboard-trim > div.page-container > div > div > div > div > div > div > div.card > div:nth-child(4) > div:nth-child(2) > div > a:nth-child(2)')))


text_list = [
    '中央氣象署今天表示，明天（2日）白天晴朗回溫，高溫約攝氏24至29度，是未來一周陽光最多的一天，要留意早晚溫差；周二（3日）開始水氣增加，北部及東半部出現局部短暫雨，周五（6日）東北風再帶一波水氣，降雨顯著；下一波冷空氣預計在8日至10日增強影響，北台灣再探15度。',
    'b', 'c', 'd']

hot_list = ["a", "b", "c"]
start_copilot()
#invideo(text_list)
# lumen5(hot_list, text_list)
