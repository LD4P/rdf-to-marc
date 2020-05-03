__author__ = "Jeremy Nelson"
__license__ = "Apache 2"

import js2py  # type: ignore
import pandas as pd  # type: ignore
import pymarc  # type: ignore
import rdflib  # type: ignore
from typing import Any, List, Optional


def conversion(js_template, value: Optional[str] = None) -> Any:
    js_str = js_template.replace("value", f"\"{value}\"")
    return js2py.eval_js(js_str)

def data_field(graph: rdflib.Graph, map_csv: str) -> List[pymarc.Field]:
    fields_df = pd.read_csv(map_csv)
    return [] 

def generate_fields(graph: rdflib.Graph, maps: List, func: Function) -> List[pymarc.Field]:
    fields = []
    for map_csv in maps:
        fields.extend(func(graph, map_csv))
    return fields


def leader(graph: rdflib.Graph, map_csv: str) -> str:
    leader_str = str()
    leader_df = pd.read_csv(map_csv)
    return leader_str

def main(graph: rdflib.Graph) -> pymarc.Record:
    leader_str = leader(graph, 'bf2marcSpec-LDR-001-005-v1.0.csv')
    record = pymarc.Record(leader=leader_str, file_encoding='utf-8')
    record.add_fields(generate_fields(graph, [], control_field))
    record.add_fields(generate_fields(graph, [], data_field))
    return record
