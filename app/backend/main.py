from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
from routes import scraper


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/html", StaticFiles(directory="html"), name="html")
templates = Jinja2Templates(directory="./html")
app.include_router(scraper.router)


@app.get("/")
def main(request: Request):
    return templates.TemplateResponse("get_data.html", context={"request": request, "data": {}})

@app.get("/scrape")
def scrape(request: Request):
    return templates.TemplateResponse("scrape_data.html", context={"request": request, "data": {}})
