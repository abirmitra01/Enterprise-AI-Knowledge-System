from pydantic import BaseModel
from pydantic import EmailStr

class UserRegister(BaseModel):

    username:str

    email:EmailStr

    password:str

    full_name:str


class UserLogin(BaseModel):

    username:str

    password:str


class Token(BaseModel):

    access_token:str

    token_type:str