##########
 ## python 3.0+
 ## ZGraphToTG v1.0 
 ## Luchnikov Vladimir 
 ## Compatibility with Zabbix 2.0=< 

import datetime
import requests


#Configuration
username = 'username'
password = 'password'
width = '800'
graphid = '1798'
#To get historical data add to end of "graph_url" this [ '&stime=' + stime + '&isNow=0' ]
#stime = "19700101010100" #stime format is YYYYmmDDhhMMss
period = 86400 #period in seconds
url = "http://localhost/zabbix"
bot_token = '123456789:AAAAAAAAAAAAAAAAAAAAAAAAAAAA1111111'
bot_chatID = '-1234567'
#####
 # to get chat id:
 # 1.add bot to chat
 # 2.send post request curl -X POST https://api.telegram.org/bot<bot_token>/getUpdates 


def telegram_bot_sendphoto(bot_image, bot_message):
    
    bot_url = 'https://api.telegram.org/bot' + bot_token + '/sendPhoto'
    #photo = {'photo': (bot_image, open(bot_image, 'rb'), 'image/png')}
    photo = {'photo': bot_image }
    data = {"parse_mode": "Markdown", "chat_id": bot_chatID, "caption": bot_message}
    response_tb = requests.post(bot_url, data = data, files = photo)
    
    return response_tb.json()

#Non configurable
cookie_request_Data = {"name": username ,"password": password,"autologin": "1","enter": "Sign in"}
graph_url = url + '/chart2.php?graphid=' + graphid + '&width=' + width + '&period=' + str(period)
h_period = str(int(period / 3600))
url_z = url + "/index.php?login=1"
#file = 'graph_result.png'

#Get zbx_sessionid
response = requests.post(url_z, data=cookie_request_Data)
auth_cookies = {"zbx_sessionid": response.cookies['zbx_sessionid'] }

#Get image
graph = requests.post(graph_url, cookies=auth_cookies)
#open(file,'wb').write(graph.content)
file = graph.content

#Send image
message = 'Graph stats in last' + h_period + ' h.'
telegram_bot_sendphoto( file, message )