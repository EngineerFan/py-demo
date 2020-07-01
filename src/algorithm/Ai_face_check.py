import requests
import base64

host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=&client_secret=3DEjNPihAT3SSG3w26stZuGGYvIa9xyc'
response = requests.get(host)
access_token = ''
if response:
    access_token = response.json()['access_token']

# 从本地读取图片
with open('C:\\Users\\admin\\Pictures\\pic\\微信图片_20200701165211.png', 'rb') as f:
    base64_data = base64.b64encode(f.read())

request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"

params = "{\"image\":\"" + str(base64_data,
                               'utf-8') + "\",\"image_type\":\"BASE64\",\"face_field\":\"faceshape,facetype\"}"

request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/json'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print(response.json())
