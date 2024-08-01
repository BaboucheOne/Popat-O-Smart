from uuid import UUID


class ReportsNotFoundException(RuntimeError):

    MESSAGE: str = "There is no documents for report id %s."

    def __init__(self, plant_id: UUID):
        super().__init__(self.MESSAGE % plant_id)
