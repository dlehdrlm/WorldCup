import os
import requests
from wordcloud import WordCloud

FONT_URL = "https://github.com/googlefonts/noto-cjk/raw/main/Sans/OTF/Korean/NotoSansCJKkr-Regular.otf"
FONT_PATH = "NotoSansKR.otf"

if not os.path.exists(FONT_PATH):
    r = requests.get(FONT_URL)
    with open(FONT_PATH, "wb") as f:
        f.write(r.content)

wc = WordCloud(
    font_path=FONT_PATH,
    width=1000,
    height=500,
    background_color="white"
).generate(text)
