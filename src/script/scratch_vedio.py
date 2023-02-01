import urllib
from bs4 import BeautifulSoup
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
browser = webdriver.Chrome(r"chromedriver.exe", options=option)

# browser.get('https://www.itlaoqi.com/')
# cookie = {'name': 'Cookie',
#           'value': 'stk=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI2MjI2In0.TFbILMGWiIQP-4kG_M5FO-YL_l89_KBxrSQY-GZAEuk;playerSpeed=1.0;selectedStreamLevel=OD;p_h5_u=14650C05-D507-4763-B058-648C1E21F1D9'}
# browser.add_cookie(cookie_dict=cookie)
browser.get(
    'https://vod.cn-shanghai.aliyuncs.com/?AccessKeyId=STS.NTWrK5RHJq8Rhe7F5Ao8t2iPj&Action=GetPlayInfo&AuthInfo=%7B%22CI%22%3A%22Yc9i6u%2FggcRqMoDZ6FnckKMRj8A42rayUz3wg1vHLLMqVc1yEnMt9q6yE9ibxb%2Fz%22%2C%22Caller%22%3A%22bF3xpbMyHBeAR41CM6SenXRYIno0rlP8QabuOuidKb4%3D%22%2C%22ExpireTime%22%3A%222022-12-14T08%3A26%3A47Z%22%2C%22MediaId%22%3A%22c2393008ffc742b2b06e92de36cca38a%22%2C%22PlayDomain%22%3A%22video.itlaoqi.com%22%2C%22Signature%22%3A%22ZWM6qstPrOmb7d7OE%2FHBIQqA8Kw%3D%22%7D&AuthTimeout=7200&Channel=HTML5&Definition=&Format=JSON&Formats=&PlayConfig=%7B%7D&PlayerVersion=2.8.2&Rand=12a35c91-0a6b-43f0-8ff2-988c8300e01d&ReAuthInfo=%7B%7D&SecurityToken=CAIShwN1q6Ft5B2yfSjIr5fiOfGBv5drxvq5akOGojUUY7dY3az7iDz2IHpNe3hqB%2B0fsPkwlGlU6fgclrMqG8EeGBKUMZsstMwOr1n8JpLFst2J6r8JjsUau7sEs0apsvXJasDVEfl2E5XEMiIR%2F00e6L%2F%2BcirYpTXHVbSClZ9gaPkOQwC8dkAoLdxKJwxk2t14UmXWOaSCPwLShmPBLUxmvWgGl2Rzu4uy3vOd5hfZp1r8xO4axeL0PoP2V81lLZplesqp3I4Sc7baghZU4glr8qlx7spB5SyVktyWGUhJ%2FzaLIoit7NpjfiB0eoQAPopFp%2FX6jvAawPLUm9bYxgphB8R%2BXj7DZYaux7GzeoWTO80%2BaKzwNlnUz9mLLeOViQ4%2FZm8BPw44ELhIaF0IUE1xFmuCd%2FX4oAyaO1v6GpLoiv9mjcBHqHzz5sePKlS1RLGU7D0VIJdUbTlzbUdJjDa%2FL%2FZYLlMcKg84WeiPMax3bQFDr53vsTbbXzZb0mptuPnzdxAKDj%2Baq1GUGoABk8hlZ%2B5G%2FE6vrbNONy5qHjir3uuBeHIxD%2F%2BJ9SSlizOu81%2BiOfE0wQkzrZy15HytOXuoKxx%2BHjXBSLu2i6WPZwI8jBlQdTNN%2BTrtTlza5Sb873uAi69x44dMGneR7iPPH6qg75mh%2Bhy5IoEe%2F8JydhSLeh6Edp%2FTRc0bmjbXV0Y%3D&SignatureMethod=HMAC-SHA1&SignatureNonce=3ad1b5df-c446-46c2-8c9e-76c9926bcbfb&SignatureVersion=1.0&StreamType=video&Version=2017-03-21&VideoId=c2393008ffc742b2b06e92de36cca38a&Signature=9PFd60WFnaxJ92hogbeRO8MaqZ4%3D')



