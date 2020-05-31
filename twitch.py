# import subprocess
# subprocess.call('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
# import os
# os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe').open("https://www.twitch.tv/")
import webbrowser
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' 
url = "https://www.twitch.tv/"
webbrowser.get(chrome_path).open(url)


