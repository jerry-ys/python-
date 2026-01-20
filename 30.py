import urllib.request
import urllib.parse

url = "https://dict.youdao.com/webtranslate"
data = {}
data['i'] = 'i love fishc.com'
data['from'] = 'en'
data['to'] = 'zh-CHS'
data['useTerm'] = 'false'
data['domain'] = '0'
data['dictResult'] = 'true'
data['keyid'] = 'webfanyi'
data['sign'] = '4b4727d24b8bb59fe9af3eae54457fee'
data['client'] = 'fanyideskweb'
data['product'] = 'webfanyi'
data['appVersion'] = '1.0.0'
data['vendor'] = 'web'
data['pointParam'] = 'client,mysticTime,product'
data['mysticTime'] = '1754723102027'
data['keyfrom'] = 'fanyi.web'
data['mid'] = '1'
data['screen'] = '1'
data['model'] = '1'
data['network'] = 'wifi'
data['abtest'] = '0'
data['yduuid'] = 'abcdefg'

data = urllib.parse.urlencode(data).encode('utf-8')
reponse = urllib.request.urlopen(url,data)
html = reponse.read().decode('utf-8')

print(html)
import json
json.loads(html)