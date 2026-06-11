from pydantic import BaseModel


class Metrics(BaseModel):
    cpu: float
    memory: float
    rps: int
    latency: float