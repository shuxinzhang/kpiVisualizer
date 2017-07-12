import youtube_grabber as youtube
import facebook_grabber as facebook
import gsheethelper as gsheet
import time

def printYouTubeData():
	YOUTUBE_RAW_DATA = youtube.request_stats()
	print("Youtube View = " + youtube.get_statistics(YOUTUBE_RAW_DATA,'viewCount'))
	print("Video amount = "  + youtube.get_statistics(YOUTUBE_RAW_DATA,'videoCount'))
	print("Subscriber amount = " + youtube.get_statistics(YOUTUBE_RAW_DATA,'subscriberCount'))

def printFacebookData():
	facebook.printLikes()

def main():
    YOUTUBE_RAW_DATA = youtube.request_stats()
    data_input = []
    data_input.append(time.strftime("%x"))
    data_input.append(youtube.get_statistics(YOUTUBE_RAW_DATA,'subscriberCount'))
    data_input.append(youtube.get_statistics(YOUTUBE_RAW_DATA,'viewCount'))
    data_input.append(youtube.get_statistics(YOUTUBE_RAW_DATA,'videoCount'))
    data_input.append(str(facebook.getLikes()))
    print(data_input)
    gsheet.add_new_row(data_input,'pistacja','A1:E1').execute()


'''print("Youtube View = " + youtube.get_statistics(YOUTUBE_RAW_DATA,'viewCount'))
	print("Video amount = "  + youtube.get_statistics(YOUTUBE_RAW_DATA,'videoCount'))
	print("Subscriber amount = " + youtube.get_statistics(YOUTUBE_RAW_DATA,'subscriberCount'))
'''
if __name__ == "__main__":
    main()