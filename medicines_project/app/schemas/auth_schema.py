from pydantic import BaseModel, EmailStr, Field

class TokenProviderData(BaseModel):
    uid: str = Field(alias="sub")
    email: EmailStr
    role: str = Field(default="")
