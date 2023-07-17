import json
import aiofiles
from app.database import Insurance
from app.internal.insurance.utils import InsuranceExists


class InitialInsurance:

    def __init__(self, file) -> None:
        self.file = file

    @InsuranceExists('The data already exists in the database')
    async def initialize(self):
        """This command initialize insurances from init json file"""

        async with aiofiles.open(self.file, 'r') as file:
            initial_json = json.loads(await file.read())

        for date in initial_json:
            for insurance in initial_json[date]:
                await Insurance.create(**insurance, date=date)
