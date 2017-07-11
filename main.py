import youtube_grabber as youtube
import facebook_grabber as facebook

def printYouTubeData():
	YOUTUBE_RAW_DATA = youtube.request_stats()
	print("Youtube View = " + youtube.get_statistics(YOUTUBE_RAW_DATA,'viewCount'))
	print("Video amount = "  + youtube.get_statistics(YOUTUBE_RAW_DATA,'videoCount'))
	print("Subscriber amount = " + youtube.get_statistics(YOUTUBE_RAW_DATA,'subscriberCount'))

def printFacebookData():
	facebook.printLikes()
	
printYouTubeData()
printFacebookData()