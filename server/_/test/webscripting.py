# webdriver の情報
from datetime import time

from selenium import webdriver
# html の タブの情報を取得
from selenium.webdriver.common.by import By
# キーボードを叩いた時に web ブラウザに情報を送信する
from selenium.webdriver.common.keys import Keys
# 次にクリックしたページがどんな状態になっているかチェックする
from selenium.webdriver.support import expected_conditions as EC
# 待機時間を設定
from selenium.webdriver.support.ui import WebDriverWait
# 確認ダイアログ制御
from selenium.webdriver.common.alert import Alert
import os

driver = webdriver.Ie(os.path.join("D://EXE", "IEDriverServer_Win32_3.150.1", "IEDriverServer.exe"))
basic_id = "admin"
basic_pass = "0425"



driver.get("https://keisan.casio.jp/exec/user/1325256498")
# driver.get('http://{}:{}@18.177.227.239/'.format(basic_id, basic_pass))

# print(driver.page_source)
driver.find_element_by_name("var_y").clear()
driver.find_element_by_name("var_y").send_keys("555")

driver.find_element_by_id("executebtn").click()

print(driver.current_url)
# driver.close()