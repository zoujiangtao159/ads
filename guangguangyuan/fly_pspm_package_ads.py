import json

with open("packagename_csv.json",'r') as loadaff_f:
    load_dict_aff = json.load(loadaff_f)
    #print(load_dict)

with open("androidads.json",'r') as loadads_f:
    load_dict_ads = json.load(loadads_f)
adlist = []
geo_list=[]
geo_ad_list =[]
ad_trackurls = []
for ad in load_dict_ads:
    ad_trackurls.append(ad['tracking_link'].replace('pub_gaid=&pub_idfa=&pub_aid=','pub_gaid=302f2641-2c2e-41bc-867f-e1b14556d844&pub_idfa=&pub_aid=72db996fd65bbe82'))
    if ad['package_id'] in load_dict_aff:
        print(ad['package_id'])
        adlist.append(ad)
        for country in ad['geo']:
            geo_ad_tu = {}
            geo_list.append(country)
            geo_ad_tu[country]=ad
        geo_ad_list.append(geo_ad_tu)
with open("af_pspm.json", "w") as f:
    json.dump(adlist, f)
    print("加载入文件完成...")

with open("geo.json", "w") as f:
    json.dump(geo_list, f)
    print("加载入文件完成...")
with open("geo_ad_list.json", "w") as f:
    json.dump(geo_ad_list, f)
    print("加载入文件完成...")
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
		"request_period" : "500000000",
		"pl" : True,
		"pld" : False,
		"iu_conf" : 7
	}
ad_L = json.dumps(ad_all)

with open("ad_all.json", "w") as f:
    json.dump(ad_all, f)
    print("加载入文件完成...ad_all")