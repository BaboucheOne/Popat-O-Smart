from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import Response
from starlette import status

from src.api.report.request.add_report_request import AddReportRequest
from src.api.report.response.get_reports_response import GetReportsResponse
from src.application.plant.plant_service import ReportService
from src.config.service_locator import ServiceLocator

router = APIRouter()


@router.post("/report")
async def add_report(
    add_report_request: AddReportRequest,
    report_service: ReportService = Depends(
        lambda: ServiceLocator.get_dependency(ReportService)
    ),
):

    report_service.add_report(
        add_report_request.plant_id,
        add_report_request.timestamp,
        add_report_request.humidity,
    )

    return Response(status_code=status.HTTP_201_CREATED)


@router.get("/{plant_id}/reports")
async def get_reports(
    plant_id: str,
    report_service: ReportService = Depends(
        lambda: ServiceLocator.get_dependency(ReportService)
    ),
):

    try:
        reports = report_service.get_reports(UUID(plant_id))
        return GetReportsResponse(reports)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")
