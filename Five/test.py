import requests

ret = requests.get("http://jsnice.org/")
print(ret.text)