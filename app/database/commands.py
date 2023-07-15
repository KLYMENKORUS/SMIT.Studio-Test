import json
import aiofiles
from app.database import Insurance


class InitialInsurance:

    def __init__(self, file) -> None:
        self.file = file

    async def initialize(self):
        """This command initialize insurances from init json file"""

        try:
            if await Insurance.all().count():
                return
        except TypeError:
            ...

        async with aiofiles.open(self.file, 'r') as file:
            initial_json = json.loads(await file.read())

        for date in initial_json:
            for insurance in initial_json[date]:
                await Insurance.create(**insurance, date=date)
