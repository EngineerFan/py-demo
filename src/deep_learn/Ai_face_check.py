import base64
from algorithm.utils import ApiUtil
import requests

host = 'https://aip.baidubce.com/oauth/2.0/token'

result = ApiUtil.get(host, grant_type='client_credentials',
                     client_id='Ibc3OpICapNnT4IXDSoHHEUG',
                     client_secret='YSdKNmiSetcYNm1BWA8wiwEHPLVMwz1Z')
print(result)
access_token = result['access_token']
# 从本地读取图片
with open('/Users/fxl/Pictures/images.jpeg', 'rb') as f:
    base64_data = base64.b64encode(f.read())

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/object_detect"
params = {'image': base64_data, 'with_face': 1}
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
result = ApiUtil.post(request_url, params, headers)
print(result)
