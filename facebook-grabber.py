import requests
import json
import facebook
import loginHelper as login
AUTH_TOKEN = login.getCredentials('facebook','auth-token')
PAGE_ID = login.getCredentials('facebook','page-id')
graph = facebook.GraphAPI(access_token = AUTH_TOKEN)
page = graph.get_object(id=PAGE_ID,fields='fan_count')
print "Facebook Likes = " + str(page.get('fan_count')) + "Likes "