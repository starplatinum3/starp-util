import urllib.parse
import base64

def v(t):
    t = urllib.parse.quote(t).replace('%', '\\x')
    return base64.b64encode(t.encode()).decode()

res=v("13131")

print(res)
# MTMxMzE=