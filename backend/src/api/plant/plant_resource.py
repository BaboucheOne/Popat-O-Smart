import uuid

from fastapi import APIRouter
from fastapi.responses import Response
from starlette import status

from src.api.plant.request.plant_report_request import PlantReportRequest
from src.domain.plant.plant_report import PlantReport

router = APIRouter()


@router.post("/plant/report")
async def add_report(plant_report_request: PlantReportRequest):
    plant_report = PlantReport(
        uuid.UUID(plant_report_request.plant_id),
        uuid.uuid4(),
        plant_report_request.timestamp,
        plant_report_request.humidity,
    )

    print(plant_report)

    return Response(status_code=status.HTTP_200_OK)
