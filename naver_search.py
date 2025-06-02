import os
import urllib.request
import urllib.parse
import json
import re
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("NAVER_CLIENT_ID")
client_secret = os.getenv("NAVER_CLIENT_SECRET")

def search_naver(keywords, mall_name):
    all_results = {}
    for keyword in keywords:
        encText = urllib.parse.quote(keyword)
        seen_titles = set()
        best_product = None
        for start in range(1, 1001, 100):
            url = f"https://openapi.naver.com/v1/search/shop.json?query={encText}&display=100&start={start}"
            req = urllib.request.Request(url)
            req.add_header("X-Naver-Client-Id", client_id)
            req.add_header("X-Naver-Client-Secret", client_secret)
            res = urllib.request.urlopen(req)
            result = json.loads(res.read())
            for idx, item in enumerate(result.get("items", []), start=1):
                if mall_name in item.get("mallName", ""):
                    title_clean = re.sub(r"<.*?>", "", item["title"])
                    if title_clean in seen_titles:
                        continue
                    seen_titles.add(title_clean)
                    rank = start + idx - 1
                    best_product = {
                        "rank": rank,
                        "title": title_clean,
                        "price": item["lprice"],
                        "link": item["link"],
                        "mallName": item["mallName"]
                    }
                    break
            if best_product:
                break
        all_results[keyword] = best_product or "검색 결과 없음"
    return all_results
