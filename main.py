from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from naver_search import search_naver
from airtable_logger import send_log  # ✅ 이 줄 추가

app = FastAPI()

class CheckRequest(BaseModel):
    uuid: str
    keywords: List[str]
    mall: str

@app.post("/check")
async def check(data: CheckRequest):
    results = search_naver(data.keywords, data.mall)
    send_log(data.uuid, data.keywords, results)  # ✅ Airtable 기록
    return {"results": results}
