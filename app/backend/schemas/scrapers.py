from pydantic import BaseModel, validator
from typing import List


class ScraperModel(BaseModel):
    websites: List
    query: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "query": "polisiye",
                    "websites": [
                        "kitapyurdu",
                        "kitapsepeti"
                    ]
                }
            ]
        }
    }

    @validator("websites")
    def website_validator(cls, v):
        available_websites = ["kitapyurdu", "kitapsepeti"]

        for website in v:
            if website not in available_websites:
                raise ValueError("Can only contain kitapyurdu or kitapsepeti")
        return v

    @validator("query")
    def query_validator(cls, v):
        return v.strip()


class GetData(BaseModel):
    title: str
    publisher: str
    writers: List
    price: float
    url: str
    query: str

class GetDataList(BaseModel):
    data: List[GetData]
