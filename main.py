from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from naver_search import search_naver

app = FastAPI()

class CheckRequest(BaseModel):
    uuid: str
    keywords: List[str]
    mall: str

@app.post("/check")
async def check(data: CheckRequest):
    results = search_naver(data.keywords, data.mall)
    return {"results": results}