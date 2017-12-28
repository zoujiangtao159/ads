import time

from date.redis_sql_link import Redis111,Redis2,Redis3,Redis4,Redis5,Redis8
def track_logs(data):
	# data = {"jsonurl_len":"7","origin_len":"9","urls":[{"error":"","duration":"312","url":"http://c.snnd.co/api/v4/click?campaign_id=9727989&publisher_id=1139&rt=171225092644&_po=d56ff9486a99c332ae356461e5c4394c&_mw=p&_c=50&_cw=c&_ad=1368&publisher_slot=&sub_1=&pub_gaid=302f2641-2c2e-41bc-867f-e1b14556d844&pub_idfa=&pub_aid=72db996fd65bbe82"},{"error":"","duration":"725","url":"http://track.yinuoapp.com/click?campid=20414260850232-9754&aff_sub=2c02812b-fe2d-4caf-bcbb-09a460f3b211__pspm&sub_channel=143347_1139_0&gaid=302f2641-2c2e-41bc-867f-e1b14556d844&idfa="},{"error":"","duration":"306","url":"http://track.yinuoapp.com/redirect?_time=1514194787&_sign=985e5b9a3c14d96770503139c4de10cf&campid=20414260850232-9754&aff_sub=2c02812b-fe2d-4caf-bcbb-09a460f3b211__pspm&sub_channel=143347_1139_0&gaid=302f2641-2c2e-41bc-867f-e1b14556d844&idfa=&ref="},{"error":"","duration":"763","url":"http://tracking.sumatoad.com/aff_c?offer_id=151732&aff_id=6655&aff_sub=20414260850232-5a40c76418bea91db073c206&aff_sub2=9754_143347_1139_0&google_aid=302f2641-2c2e-41bc-867f-e1b14556d844&ios_idfa=&aff_sub4=videoshow"},{"error":"","duration":"266","url":"http://tracking.sumatoad.com/aff_r?offer_id=151732&aff_id=6655&url=http%3A%2F%2Fclinkadtracking.com%2Ftracking%3Fcamp%3D38108433%26pubid%3D1853%26sid%3Dwadogo_WAdvZoomyAPI_127745_10298d7c34ec3f3501c5eab021cec4%26subpubid%3D6655_9754_143347_1139_0%26sid2%3D9754_143347_1139_0%26gaid%3D302f2641-2c2e-41bc-867f-e1b14556d844&urlauth=816620697111116404969980652682"},{"error":"","duration":"1881","url":"http://clinkadtracking.com/tracking?camp=38108433&pubid=1853&sid=wadogo_WAdvZoomyAPI_127745_10298d7c34ec3f3501c5eab021cec4&subpubid=6655_9754_143347_1139_0&sid2=9754_143347_1139_0&gaid=302f2641-2c2e-41bc-867f-e1b14556d844"},{"error":"","duration":"0","url":"market://details?id=com.xpro.camera.lite&referrer=utm_source%3DZoomy%26utm_campaign%3Dgroup4%26utm_content%3D4IMNjWABAAA9BwAACQAAAFPHCQAAAAAAEX1FApqZGT8AAAAAATVweQA*%26af_siteid%3D1853_6655_9754_143347_1139_0%26google_aid%3D302f2641-2c2e-41bc-867f-e1b14556d844"}],"timeout":"false","campaign_id":""}
	# print(data['timeout'])
	if data['timeout'] != 'true':
		af_url = data['urls'][-2]['url']
		# print(af_url.split('/'))
		if af_url.split('/')[2] == 'app.appsflyer.com':
			google_url = data['urls'][-1]['url']
			store_qu_baoming = google_url.split('?')
			for package_name in store_qu_baoming:
				try:
					id = package_name.split('=')
					for name in id:
						if name =='id':
							refer_package_name =id[id.index(name)+1]
							refer_package_name_0 =refer_package_name.split('&')[0]
							conn_redis_8 = Redis8()
							conn_redis_8.set(str(refer_package_name_0), refer_package_name_0)
							print(refer_package_name_0)
				except:
					pass



