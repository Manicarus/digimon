import requests
import re
import time

save_address = 'save_pic/'
url = 'http://digidb.io/digimon-list/'
response = requests.get(url)
match_str = '<tr><td width=.*?><b>&nbsp;.*?</b></td><td width=.*?>&nbsp;<img style="vertical-align:middle;" src=".*?" /> <a style="font-weight: bold;" href=.*?>(.*?)</a></td><td width=.*?><center>(.*?)</center></td><td width=.*?><center>(.*?)</center></td><td width=.*?><center>(.*?)</center></td><td width=.*?><center>(.*?)</center></td><td width=.*?><center>(.*?)</center></td><td><center>(.*?)</center></td><td><center>(.*?)</center></td><td><center>(.*?)</center></td><td><center>(.*?)</center></td><td><center>(.*?)</center></td><td><center>(.*?)</center></td></tr>'
urls = re.findall(match_str, response.text)
result = requests.get(url)
file_name = 'digimon_list.txt'
with open(save_address + file_name, 'w') as f:
    for url_one in urls:
        string_url = str(url_one) + '\n'
        f.write(string_url)

