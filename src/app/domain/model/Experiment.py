import datetime
from pydantic import BaseModel, Field
from app.domain.enums.ExperimentsType import ExperimentsType
from app.domain.model.Dataset import Dataset
from app.domain.model.User import User

class Experiment(BaseModel):
    id: str = Field(const=datetime.datetime.now().strftime("%Y%m%d%H%M%S"), default=datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    name: str
    type: ExperimentsType
    namespace: str
    dataset: Dataset
    user: User