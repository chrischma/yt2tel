import telegram_send
import subprocess
import os 

# My standard-shortcut for sending messages with "telegram_send":

def tsend(text, file=""):
	telegram_send.send(messages=[text])

	if file != "":
		with open(file, "rb") as f:			
			telegram_send.send(files=[f])
	return

def get_url_from_user():
	url = input("URL: ")

	while (url[:16] != "https://www.yout") and (url[:16] != "https://youtu.be"):

		print("Please enter a valid URL. Examples: \n https://www.youtube.com/watch?v=xu92YRDNqWQ or \n https://youtu.be/xu92YRDNqWQ")
		url = input("URL: ")
	
	else:

		return url

print("Hi! Please enter an URL.")
url = get_url_from_user()

print(f'Video URL: {url}')
print("Working now...")

# Extracting Video Title with YouTube-dl:
title = str(subprocess.check_output('youtube-dl -e --get-filename '+url, shell=True, universal_newlines=None))
title = title[:25][2:]

print(f'Video Title: {title}...')

# Downloading and converting the video to mp3:
os.system('youtube-dl '+url+"  -o '"+title+".%(ext)s' -x --audio-format mp3")

# Sending the file to Telegram:
tsend("Alright, here's your latest file!:",f'{title}.mp3')

print("Sucess! Your file was sent to telegram!")
