from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class PlantReportRequest(BaseModel):
    plant_id: UUID = Field(default_factory=uuid4)
    timestamp: int
    humidity: float
