import json
import lxml
import requests
from bs4 import BeautifulSoup

url = 'http://pspm.pingstart.com/api/campaigns?token=d777c5d1-ee12-43cf-9661-e357428854c3&publisher_id=1139'
s = requests.session()
req = s.get(url)
req_result = req.content.decode(encoding='utf-8')
json_res = json.loads(req_result)
with open("record.json","w") as f:
     json.dump(json_res,f)
     print("加载入文件完成...")