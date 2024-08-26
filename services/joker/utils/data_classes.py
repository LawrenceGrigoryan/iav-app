from pydantic import BaseModel


class JokerRequest(BaseModel):
    prompt: str