from pydantic import BaseModel, Field, EmailStr, ConfigDict
from app.utils.pyobjectid import PyObjectId
from bson.objectid import ObjectId


class UserIn(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: PyObjectId = Field(alias="_id")
    username: str
    email: EmailStr

    # v2 →  model_config
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
    )
