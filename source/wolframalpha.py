from urllib.request import urlopen
from xml.dom import minidom

query = "what is the antiderivative of x squared"

query = query.replace(" ", "%20")

api_root = "http://api.wolframalpha.com/v2/query?"
appid = "TEL9QP-HYK7YETLXE"

url = api_root + "input=" + query + "&appid=" + appid

resp = urlopen(url)
doc = minidom.parse(resp)

pods = doc.getElementsByTagName("pod")

if "derivative" in query:
    subpods = pods[0].getElementsByTagName("subpod")
else:
    subpods = pods[1].getElementsByTagName("subpod")

answer = subpods[0].getElementsByTagName("plaintext")[0]

print(answer.firstChild.data)
