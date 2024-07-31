from pydantic import BaseModel


class PlantReportRequest(BaseModel):
    plant_id: str
    timestamp: int
    humidity: float
