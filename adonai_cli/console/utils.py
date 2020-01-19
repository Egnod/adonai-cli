import termtables
from typing import List, Dict, Union
from enum import Enum

class Defaults(Enum):
    NO_INPUT = "no_input"

def get_table(dict_list: Union[List[Dict], Dict], header: List[str]):
    rows = []

    if isinstance(dict_list, dict):
        dict_list = [dict_list]

    for obj in dict_list:
        rows.append(list(obj.values()))
    
    return termtables.to_string(
        rows,
        header=header
    )


def get_fields_dict(fields: List[str]):
    return {field: True for field in fields}


def get_arguments(**fields: Dict):
    clear_fields = fields.copy()

    for field_name in fields:
        if fields[field_name] == Defaults.NO_INPUT:
            clear_fields.pop(field_name)

    return clear_fields
