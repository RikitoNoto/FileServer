b'# webdriver \xe3\x81\xae\xe6\x83\x85\xe5\xa0\xb1\r\nfrom datetime import time\r\n\r\nfrom selenium import webdriver\r\n# html \xe3\x81\xae \xe3\x82\xbf\xe3\x83\x96\xe3\x81\xae\xe6\x83\x85\xe5\xa0\xb1\xe3\x82\x92\xe5\x8f\x96\xe5\xbe\x97\r\nfrom selenium.webdriver.common.by import By\r\n# \xe3\x82\xad\xe3\x83\xbc\xe3\x83\x9c\xe3\x83\xbc\xe3\x83\x89\xe3\x82\x92\xe5\x8f\xa9\xe3\x81\x84\xe3\x81\x9f\xe6\x99\x82\xe3\x81\xab web \xe3\x83\x96\xe3\x83\xa9\xe3\x82\xa6\xe3\x82\xb6\xe3\x81\xab\xe6\x83\x85\xe5\xa0\xb1\xe3\x82\x92\xe9\x80\x81\xe4\xbf\xa1\xe3\x81\x99\xe3\x82\x8b\r\nfrom selenium.webdriver.common.keys import Keys\r\n# \xe6\xac\xa1\xe3\x81\xab\xe3\x82\xaf\xe3\x83\xaa\xe3\x83\x83\xe3\x82\xaf\xe3\x81\x97\xe3\x81\x9f\xe3\x83\x9a\xe3\x83\xbc\xe3\x82\xb8\xe3\x81\x8c\xe3\x81\xa9\xe3\x82\x93\xe3\x81\xaa\xe7\x8a\xb6\xe6\x85\x8b\xe3\x81\xab\xe3\x81\xaa\xe3\x81\xa3\xe3\x81\xa6\xe3\x81\x84\xe3\x82\x8b\xe3\x81\x8b\xe3\x83\x81\xe3\x82\xa7\xe3\x83\x83\xe3\x82\xaf\xe3\x81\x99\xe3\x82\x8b\r\nfrom selenium.webdriver.support import expected_conditions as EC\r\n# \xe5\xbe\x85\xe6\xa9\x9f\xe6\x99\x82\xe9\x96\x93\xe3\x82\x92\xe8\xa8\xad\xe5\xae\x9a\r\nfrom selenium.webdriver.support.ui import WebDriverWait\r\n# \xe7\xa2\xba\xe8\xaa\x8d\xe3\x83\x80\xe3\x82\xa4\xe3\x82\xa2\xe3\x83\xad\xe3\x82\xb0\xe5\x88\xb6\xe5\xbe\xa1\r\nfrom selenium.webdriver.common.alert import Alert\r\nimport os\r\n\r\ndriver = webdriver.Ie(os.path.join("D://EXE", "IEDriverServer_Win32_3.150.1", "IEDriverServer.exe"))\r\nbasic_id = "admin"\r\nbasic_pass = "0425"\r\n\r\n\r\n\r\ndriver.get("https://keisan.casio.jp/exec/user/1325256498")\r\n# driver.get(\'http://{}:{}@18.177.227.239/\'.format(basic_id, basic_pass))\r\n\r\n# print(driver.page_source)\r\ndriver.find_element_by_name("var_y").clear()\r\ndriver.find_element_by_name("var_y").send_keys("555")\r\n\r\ndriver.find_element_by_id("executebtn").click()\r\n\r\nprint(driver.current_url)\r\n# driver.close()'