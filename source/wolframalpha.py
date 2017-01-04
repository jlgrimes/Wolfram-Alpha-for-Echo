from urllib.request import urlopen
from xml.dom import minidom

query = "integrate arctan(x)"

query = query.replace(" ", "%20")

api_root = "http://api.wolframalpha.com/v2/query?"
appid = "TEL9QP-HYK7YETLXE"

url = api_root + "input=" + query + "&appid=" + appid

print(url)

resp = urlopen(url)
doc = minidom.parse(resp)

pods = doc.getElementsByTagName("pod")

if "derivative " or " derivative" in query:
    subpods = pods[0].getElementsByTagName("subpod")
elif "antiderivative" or "integral" or "integrate" in query:
    subpods = pods[0].getElementsByTagName("subpod")
else:
    subpods = pods[1].getElementsByTagName("subpod")

answer = subpods[0].getElementsByTagName("plaintext")[0]

print(answer.firstChild.data)
