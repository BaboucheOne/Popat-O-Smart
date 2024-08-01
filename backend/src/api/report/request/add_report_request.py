from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class AddReportRequest(BaseModel):
    plant_id: UUID = Field(default_factory=uuid4)
    timestamp: int
    humidity: float
