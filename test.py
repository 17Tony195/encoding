import requests

text = 'Hello'  # 'Hello\n world'  'Hello, apple!\n New line \t tab char'
r = requests.get('http://127.0.0.1:8000/encode/'+text).json()
encoded = r['encoded']
key = r['key']
print('encoded text: ' + encoded)
print('key: ' + key)

r = requests.get('http://127.0.0.1:8000/decode/'+encoded+'/'+key).json()
decoded = r['decoded']
print()
print('decoded text:')
print(decoded)
