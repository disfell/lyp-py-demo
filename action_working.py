import requests

def heartbeat():
  try:
    _post()
  except Exception as e:
    print(f"Error: {e}")

def _post():
  response = requests.post('http://localhost:3000/api/working', data={ 'heartbeat': True})
  # 检查请求是否成功
  if response.status_code == 200:
    print(response.text)  # 打印返回的文本
  else:
    print('Failed to post data:', response.status_code)  