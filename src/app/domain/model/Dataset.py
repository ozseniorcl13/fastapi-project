from pydantic import BaseModel
from app.domain.enums.DatasetName import DatasetName

class Dataset(BaseModel):
    name: DatasetName
    path: str
    volume: str
    target: str