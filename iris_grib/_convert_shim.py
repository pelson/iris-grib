from . import GribWrapper
from .load_rules import convert as grib1_convert
from ._load_convert import convert as grib2_convert


def convert(field):
    editionNumber = field.sections[0]['editionNumber']
    print('HUZZAH!')
    if editionNumber == 1:
        msg_id = field._raw_message._message_id
        conversion_md = grib1_convert(GribWrapper(msg_id))
    elif editionNumber == 2:
        conversion_md = grib2_convert(field)
    else:
        raise ValueError()

    return conversion_md

