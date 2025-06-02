from fastapi import FastAPI, Request
from naver_search import search_naver

app = FastAPI()

@app.post("/check")
async def check(request: Request):
    data = await request.json()
    keywords = data.get("keywords", [])
    mall = data.get("mall", "")
    uuid = data.get("uuid", "")
    results = search_naver(keywords, mall)
    return {"results": results}
