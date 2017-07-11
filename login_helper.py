import json

def getCredentials(platform,key):
	auth_data = open('auth-info.json')
	auth_json = json.load(auth_data)
	return auth_json[platform][key] 

	

