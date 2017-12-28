import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

mobile_emulation = {"deviceName": "Nexus 5"}
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
#chrome_options.add_argument('--proxy-server=http://70.169.70.83:80')#IP=,sg,Singapore,,
chrome_options.add_argument('--proxy-server=http://70.169.70.83:80')#IP=,sg,Singapore,,
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='chromedriver.exe')
driver.get("http://c.snnd.co/api/v4/click?campaign_id=9625727&publisher_id=1139&rt=171222020355&_po=3b547673d06d9668ef43b703c745e3d5&_mw=p&_c=50&_cw=p&_ad=1540&publisher_slot=&sub_1=&pub_gaid=302f2641-2c2e-41bc-867f-e1b14556d844&pub_idfa=&pub_aid=72db996fd65bbe82")
print(driver.page_source)
print(driver.current_url)
time.sleep(5)
#driver.close()