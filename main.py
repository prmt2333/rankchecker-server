from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List
from naver_search import search_naver
from airtable_logger import send_log

app = FastAPI()

class CheckRequest(BaseModel):
    uuid: str
    keywords: List[str]
    mall: str

def get_client_ip(request: Request) -> str:
    return request.client.host

@app.post("/check")
async def check(data: CheckRequest, request: Request):
    results = search_naver(data.keywords, data.mall)
    ip = get_client_ip(request)
    send_log(data.uuid, data.keywords, results, data.mall, ip)
    return {"results": results}
