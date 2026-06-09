from pydantic import BaseModel

class ComplaintRequest(BaseModel):

    text: str

    department: str

    group: str

    software: str

    hw_flag: int