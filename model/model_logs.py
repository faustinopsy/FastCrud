from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class Logs(BaseModel):
    id: Optional[UUID] = None 
    path: str
    method: str
    client_ip: str
    data_ini: str
    data_fim: str
    process_time: str
