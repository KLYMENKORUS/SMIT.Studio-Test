from enum import Enum

from tortoise.models import Model
from tortoise import fields


class CargoTypes(str, Enum):
    glass = 'Glass'
    other = 'Other'


class Insurance(Model):
    id = fields.IntField(pk=True)
    cargo_type = fields.CharEnumField(CargoTypes, max_length=100)
    rate = fields.DecimalField(18, 5)
    date = fields.DateField()

    def __str__(self):
        return self.cargo_type

    class Meta:
        unique_together = (('cargo_type', 'date'),)