from dataclasses import dataclass
from typing import List

from dataclasses_jsonschema import JsonSchemaMixin
from fastapi.responses import Response
from starlette import status

from src.domain.report.report import Report


@dataclass
class GetReportsResponse(JsonSchemaMixin):
    devices: List[Report]

    def response(self) -> Response:
        return Response(
            content=self.to_dict(),
            media_type="application/json",
            status_code=status.HTTP_200_OK,
        )
