from pydantic import BaseModel

class Banner(BaseModel):
    location: str
    owner: str
    price: str
    html_code: str
    type : str
    size : str
    status : str
    exp_date: str