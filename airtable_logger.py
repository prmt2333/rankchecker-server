from pyairtable import Table
from datetime import datetime
import os

AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
BASE_ID = os.getenv("BASE_ID")
TABLE_NAME = "SearchLogs"

def send_log(uuid, keywords, results):
    table = Table(AIRTABLE_API_KEY, BASE_ID, TABLE_NAME)
    flat_results = "\n".join([
        f"{kw} → {val['rank']}위, {val['title'][:20]}..." if isinstance(val, dict) else f"{kw} → 없음"
        for kw, val in results.items()
    ])
    table.create({
        "uuid": uuid,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "keywords": ", ".join(keywords),
        "results_json": flat_results
    })
