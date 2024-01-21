import pint
from django.core.exceptions import ValidationError
from pint.errors import UndefinedUnitError

def validate_unit_measure(value):
    ureg = pint.UnitRegistry()
    try:
        single_unit = ureg[value]
    except UndefinedUnitError as e:
        raise ValidationError(e)
