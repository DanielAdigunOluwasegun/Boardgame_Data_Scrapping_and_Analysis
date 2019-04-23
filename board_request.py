import urllib.request
import os 
import time
import datetime
import requests
if not os.path.exists("html_files"):
	os.mkdir("html_files")

pages = [ 'page/1', 'page/2', 'page/3', 'page/4', 'page/5', 'page/6', 'page/7', 'page/8', 'page/9', 'page/10', 'page/11', 'page/12', 'page/13', 'page/14', 'page/15', 'page/16', 'page/17', 'page/18', 'page/19', 'page/20', 'page/21', 'page/22', 'page/23', 'page/24', 'page/25','page/26', 'page/27', 'page/28', 'page/29', 'page/30', 'page/31', 'page/32', 'page/33', 'page/34', 'page/35', 'page/36', 'page/37', 'page/38', 'page/39', 'page/40', 'page/41', 'page/42', 'page/43', 'page/44', 'page/45', 'page/46', 'page/47', 'page/48', 'page/49', 'page/50']

for page in pages: 
	for i in range(1): 
		current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
		print(str(i) + ":" + current_time_stamp)
		f = open("html_files/boardgames" + current_time_stamp + ".html","wb")
		page_link = 'https://boardgamegeek.com/browse/boardgame/' + page
		response = urllib.request.urlopen(page_link)
		html = response.read()
		f.write(html)
		f.close()
		print("requesting boardgames")
		time.sleep(3)




