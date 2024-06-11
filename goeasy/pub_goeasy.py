import json
import requests
from requests.structures import CaseInsensitiveDict
import logging

# 开发文档：https://docs.goeasy.io/2.x/
def post(channel = 'lyp-ink', msg = 'hello'):
  # 新加坡rest-host：rest-singapore.goeasy.io
  url = "https://rest-hz.goeasy.io/v2/pubsub/publish"
  headers = CaseInsensitiveDict()
  headers["Accept"] = "application/json"
  headers["Content-Type"] = "application/json"
  data = json.dumps({
    "appkey": "PR-61796e986b26406d966e4978ba6140a8",
    "channel": channel,
    "content": msg
  })
  resp = requests.post(url, headers=headers, data=data)
  logging.info(f'pub goeasy: {data} => {resp.status_code}')