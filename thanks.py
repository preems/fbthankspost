import requests
import json,random
import datetime
print("Enter your Auth token")
token = str(raw_input("> "))
print ("Enter your birth month (1-12)")
month = int(raw_input("> "))
print ("Enter your birth day (1-31)")
date = int(raw_input("> "))
bday = datetime.date(datetime.datetime.now().year,month,date)
base_url='https://graph.facebook.com/v2.1/'
url='https://graph.facebook.com/v2.1/me/feed?fields=id,from&limit=100'
feed = json.loads(requests.get(url+'&access_token='+token).text)
messages = ['Thanks ','Thank u ','thanks a lot ','thanks ','Thanks a lot ','thank u ']
suffix = [' :)',' ',' !!']
#print feed
for status in feed['data']:
	print datetime.datetime.strptime(status['created_time'][0:10],"%Y-%m-%d").date(),bday
	if datetime.datetime.strptime(status['created_time'][0:10],"%Y-%m-%d").date() != bday:
		continue
	print status['from']['name']
	print status['id']
	dict = {}
	dict['message']=messages[random.randint(0,5)]+status['from']['name'].split(' ')[0]+suffix[random.randint(0,2)]
	print dict['message']
	r=requests.post(base_url+status['id']+'/comments?method=POST&access_token='+token,params=dict)
	print r.text
	r = requests.post(base_url+status['id']+'/likes?method=POST&access_token='+token)
	print r.text

