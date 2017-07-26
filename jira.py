import urllib
import requests
import login_helper as login_helper
from collections import OrderedDict

def login():
	username = login_helper.getCredentials('jira','username')
	password = login_helper.getCredentials('jira','password')
	return (username,password)

def search(jql):
	base_url = "https://jira.katalysteducation.org/rest/api/2/search?jql="
	url = base_url+jql
	res = requests.get(url,auth=login())
	return res.json()

def jql(type_,status):
	query_details = 'type='+type_+'&status '+status
	return urllib.quote(query_details)

def total_published_video():
	return search(jql('Video','=DONE'))['total']

def total_published_playlist():
	return search(jql('Playlist','=DONE'))['total']

def total_pipeline_video():
	return search(jql('Video','!=DONE'))['total']

def total_preproduction_video():
	return search(jql('Video','=Pre-Production'))['total']

def total_production_video():
	return search(jql('Video','=Production'))['total']

def total_postproduction_video():
	return search(jql('Video','not in (Open,Pre-Production,Production,Publication,"Quality Control 2","Quality Control 1","Final Approval","Final Approval 2",Planning,"Teaser Approval",DONE)'))['total']

def cnx_graphics():
	return search(jql('"CNX Subtask"','not in (Open,"CNX Ingest","Quality Control 1",Editing)'))['total']

def cnx_modules():
	return search(jql('"CNX Section"','not in (Open,"Adaptation (Stage I)","Legitimization (Stage II)",Editing,"CNX Ingest")'))['total']

def get_jira_data():
	data = OrderedDict()
	data['published videos'] = total_published_video()
	data['published playlists'] = total_published_playlist()
	data['pipeline videos']= total_pipeline_video()
	data['postproduction videos']=total_postproduction_video()
	data['preproduction videos']=total_preproduction_video()
	data['production videos']=total_production_video()
	data['cnx graphics']=cnx_graphics()
	data['cnx modules']=cnx_modules()
	return data
	
print get_jira_data()
	



