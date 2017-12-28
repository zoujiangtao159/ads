import json

with open("record.json",'r') as load_f:
    load_dict = json.load(load_f)
    #print(load_dict)
iosads =[]
androidads = []
for ad in load_dict['campaigns']:
    if ad['platform'] == 'Android':
        androidads.append(ad)
    else:
        iosads.append(ad)


with open("iosads.json","w") as f:
     json.dump(iosads,f)
     print("加载入文件完成...")


with open("androidads.json","w") as f:
     json.dump(androidads,f)
     print("加载入文件完成...")



