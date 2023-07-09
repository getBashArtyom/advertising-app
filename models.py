from pydantic import BaseModel

class Banner(BaseModel):
    location: str
    owner: str
    price: float
    html_code: str