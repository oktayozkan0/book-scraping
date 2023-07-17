from fastapi import APIRouter, Depends
from schemas.scrapers import ScraperModel, GetDataList
import requests
from database import mydb
from bson.json_util import loads


router = APIRouter()

@router.post("/startScraping")
def start_scraping(body: ScraperModel):
    for site in body.websites:
        d = requests.post(f"http://scraper:6800/schedule.json?project=scraper&spider={site}&query={body.query}")
    return d.json()

def get_records(collection, query):
    col = mydb[collection]
    data = col.find({"query": query}, {'_id':0})
    data = list(data)
    print(data)
    return data

@router.get("/getData")
def get_data(query: str, collection: str):
    data = get_records(collection=collection, query=query)
    return data
