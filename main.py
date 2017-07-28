import youtube_grabber as youtube
import facebook_grabber as facebook
import gsheethelper as gsheet
import jira
import time
import googleAnalytics as ga

def printYouTubeData():
	YOUTUBE_RAW_DATA = youtube.request_stats()

def printFacebookData():
	facebook.printLikes()



def main():
    YOUTUBE_RAW_DATA = youtube.request_stats()
    jira_data = jira.get_jira_data()
    data_input = []
    data_input.append(time.strftime("%x"))
    data_input.append(youtube.get_statistics(YOUTUBE_RAW_DATA,'subscriberCount'))
    data_input.append(youtube.get_statistics(YOUTUBE_RAW_DATA,'viewCount'))
    data_input.append(youtube.get_statistics(YOUTUBE_RAW_DATA,'videoCount'))
    data_input.append(str(facebook.getLikes()))
    for entry in jira_data:
        data_input.append(str(jira_data[entry]))
    data_input.append(ga.get_session('career-map'))
    data_input.append(ga.get_user('career-map'))
    data_input.append(ga.get_session('pi-stacja'))
    data_input.append(ga.get_user('pi-stacja'))
    data_input.append(ga.get_session('katalyst-education'))
    data_input.append(ga.get_user('katalyst-education'))
    gsheet.add_new_row(data_input,'pistacja','A1:E1').execute()


'''print("Youtube View = " + youtube.get_statistics(YOUTUBE_RAW_DATA,'viewCount'))
	print("Video amount = "  + youtube.get_statistics(YOUTUBE_RAW_DATA,'videoCount'))
	print("Subscriber amount = " + youtube.get_statistics(YOUTUBE_RAW_DATA,'subscriberCount'))
'''
if __name__ == "__main__":
    main()