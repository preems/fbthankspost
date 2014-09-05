import requests
import facebook,json,random
import datetime
#token = '&access_token=CAACEdEose0cBAITBWAZBY2tv8eA91ngKT3Bs44erpaKohAx1iBUcCd4HYEEHKaPbUJYoMf4FBIZAMEZBDoo9xjUSmX8FbsFezuHic4SGcJEGTKbV8BXZB8DzzXdv7JQ0OTI7bVFEfOEPy7Ixk33c8Fwm6Ds3GEWUsoghiOfaS10M3KnkzsQvKr281AInjU4PO6fJS8cyswZDZD'
print("Enter your Auth token")
token = str(raw_input("> "))
print ("Enter your birth month (1-12")
month = int(raw_input("> "))
print ("Enter your birth day (1-31")
date = int(raw_input("> "))
bday = datetime.date(datetime.now().year,month,date)
url='https://graph.facebook.com/v2.1/me/feed?fields=id,from&limit=1000'
feed = json.loads(requests.get(url+'me/feed?until=yesterday'+token).text)
messages = ['Thanks ','Thank u ','thanks a lot ','thanks ','Thanks a lot ','thank u ']
suffix = [' :)',' ',' !!']
for status in feed['data']:
	if datetime.strprime(status['created_time'][0:9],"%Y-%m-%d") is not bday:
		continue
	print status['from']['name']
	print status['id']
	dict = {}
	dict['message']=messages[random.randint(0,5)]+status['from']['name'].split(' ')[0]+suffix[random.randint(0,2)]
	print dict['message']
	r=requests.post(url+status['id']+'/comments?method=POST'+token,params=dict)
	r = requests.post(url+status['id']+'/likes?method=POST'+token)
	print r.text
