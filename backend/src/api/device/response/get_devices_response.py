from dataclasses import dataclass
from typing import List

from dataclasses_jsonschema import JsonSchemaMixin
from fastapi.responses import Response
from starlette import status

from src.domain.device.device import Device


@dataclass
class GetDevicesResponse(JsonSchemaMixin):
    devices: List[Device]

    def response(self) -> Response:
        return Response(
            content=self.to_dict(),
            media_type="application/json",
            status_code=status.HTTP_200_OK,
        )
