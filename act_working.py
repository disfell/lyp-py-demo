import requests
import configparser
import logging

config = configparser.ConfigParser()
config.read('config.ini')

def heartbeat():
  try:
    _post()
  except Exception as e:
    logging.exception(e)

def _post():
  server = config.get('lyp-ink', 'server')
  url = f'{server}/api/working'
  response = requests.post(url, data={ 'heartbeat': True})
  # 检查请求是否成功
  if response.status_code >= 200 or response.status_code <= 299:
    logging.info(f'{url} 响应：{response.text}')  # 打印返回的文本
  else:
    logging.error(f'Failed to post data: {response.status_code} | {response.text}')  