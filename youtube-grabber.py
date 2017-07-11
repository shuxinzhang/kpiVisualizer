import requests
import json
import loginHelper as login

####run pip install requests before running this code!
auth_data = open('auth-info.json')
auth_json = json.load(auth_data)
CHANNEL_ID = login.getCredentials('youtube','channel-id') #hard-coded instance rn
AUTH_KEY = login.getCredentials('youtube','auth-key') #hard-coded instance

YOUTUBE_RAW_DATA = requests.get("https://www.googleapis.com/youtube/v3/channels?"+
	"part=statistics&id="+CHANNEL_ID+"&key="+AUTH_KEY)

def get_statistics(raw_data):
	if raw_data.status_code!=200:
		print 'Error getting data, check key or id!'
		return 
	else :
		statistics =  raw_data.json()['items'][0]['statistics']
		return statistics
#TO-DO: MIGRATE THOSE TO EXCEL
print("Youtube View = " + get_statistics(YOUTUBE_RAW_DATA)['viewCount']) 
print("Video amount = "  + get_statistics(YOUTUBE_RAW_DATA)['videoCount'])
print("Subscriber amount = " + get_statistics(YOUTUBE_RAW_DATA)['subscriberCount'])