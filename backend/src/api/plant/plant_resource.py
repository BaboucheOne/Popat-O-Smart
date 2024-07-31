from fastapi import APIRouter, Depends
from fastapi.responses import Response
from starlette import status

from src.api.plant.request.plant_report_request import PlantReportRequest
from src.application.plant.plant_service import PlantService
from src.config.service_locator import ServiceLocator

router = APIRouter()


@router.post("/plant/report")
async def add_report(
    plant_report_request: PlantReportRequest,
    plant_service: PlantService = Depends(
        lambda: ServiceLocator.get_dependency(PlantService)
    ),
):

    plant_service.add_report(
        plant_report_request.plant_id,
        plant_report_request.timestamp,
        plant_report_request.humidity,
    )

    return Response(status_code=status.HTTP_200_OK)
