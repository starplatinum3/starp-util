

# https://uland.taobao.com/sem/tbsearch?refpid=mm_26632258_3504122_32538762&keyword=java&clk1=f0c0948220ecee34d8e48fcb4b69b80b&upsId=f0c0948220ecee34d8e48fcb4b69b80b&spm=a2e0b.20350158.search.1&pid=mm_26632258_3504122_32538762&union_lens=recoveryid%3A201_33.42.156.233_16319860_1667716432848%3Bprepvid%3A201_33.8.41.104_12221870_1667717148444
import requests
url="""
https://uland.taobao.com/sem/tbsearch?refpid=mm_26632258_3504122_32538762&keyword=java&clk1=f0c0948220ecee34d8e48fcb4b69b80b&upsId=f0c0948220ecee34d8e48fcb4b69b80b&spm=a2e0b.20350158.search.1&pid=mm_26632258_3504122_32538762&union_lens=recoveryid%3A201_33.42.156.233_16319860_1667716432848%3Bprepvid%3A201_33.8.41.104_12221870_1667717148444
"""
# cookies={
                        #  'cookie': '你的cookie'}
r = requests.get(url, timeout=30, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}, )
# r.raise_for_status()
# r.encoding = r.apparent_encoding

# UnicodeEncodeError: 'latin-1' codec can't encode characters in position 7-8: ordinal not in range(256)
print(r.text)

with open("taobaoHtml.html","w",encoding="utf-8") as f:
    f.write(r.text)