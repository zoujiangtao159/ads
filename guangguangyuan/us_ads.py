import json

with open("geo_ad_list.json",'r') as loadaff_f:
    load_dict_aff = json.load(loadaff_f)
us_ads =[]
ad_trackurls=[]
for us_ad in load_dict_aff:
    for i in us_ad.keys():
        if i == 'US':
            ad_trackurls.append(us_ad[i]['tracking_link'].replace('pub_gaid=&pub_idfa=&pub_aid=','pub_gaid=785fa536-39ba-4426-83bc-c9cec0d5ebbf&pub_idfa=&pub_aid=04a45210b59814a3'))
            us_ads.append(us_ad[i])

with open("us_ads.json", "w") as f:
    json.dump(us_ads, f)
    print("加载入文件完成...")
print(ad_trackurls)
ad_all ={}

apps =[]
for ad_trackurl in ad_trackurls:
    data = {
        "title": "",
        "description": "",
        "banner_link": "",
        "preview_link": "",
        "packageName": "",
        "creative_type": 0,
        "company": "",
        "app_link": "http://r1.snnd.co/v1/wad/r?_po=nO9adO08YZ1Ctt5uJamr_NBOR_gkJSxZSiQ06R6AzjfGPKD07jCCbpIs_JeoqkMcR3Osujiw_HtFVTgUXlt0YN4wNq9am8s-au5g1Oj5naz6_NE0uBWnNnm_lGa6-A7keULjblPHDeGpzHmBuElbi2fTfKj4i4lwS-_L5jlKS_jpmf_rlLrYMWWeTsoVxoi8ZXV6bJNGfoCjCP8gCssup5ML_mPB4NN6FAwOI__8IUMqfBSHV4RftnNbSWiKcGnwOZ96253AngYDr0ZdM6x0x4plCaCKS-W0Q2Cwff-DXwThFmyNhBjtVZby4ZbsmWizMEqs7Rgxc-0ogJGECv4RV7KslrJLSNduGGVZojQf62NtpIXMCvXuorMm0AScl6TxctwBcFTK6QGSIGnVOGi9UCmt1OHkOZwzvln8KuGYPZrApCmFi3bp_b8MGk0bd4ch6oFAQtCbzaiSGPM4EWRmeaCcwErRlWu8SFvsAJIWogIuZ6hnvNqNt1wbWEsnrcz14lsWJYQNT0X64JfulBBckG3O4zLH3q92pDuie9H7ky7ItFhWYEOcNEBa4Cu8JQaTx9Tf7KqT8ecnIy_ZNIDOebnu7j7iigT8",
        "impression_track_url": "",
        "click_record_url": "",
        "conversion_track_url": "",
        "icon_link": "",
        "ratings": 0,
        "f": 1,
        "g": "5",
        "category": "",
        "in_order": 0,
        "platform": "Android",
        "h": True
    }
    data['app_link'] = ad_trackurl
    apps.append(data)
    #print(apps)
ad_all['apps'] = apps
#print(apps)
ad_all['sdk_config'] ={
		"request_delaytime" : "20000",
		"timeout" : "10000",
		"request_period" : "50000",
		"pl" : True,
		"pld" : False,
		"iu_conf" : 7
	}
ad_L = json.dumps(ad_all)

