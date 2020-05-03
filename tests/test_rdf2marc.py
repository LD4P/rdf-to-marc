__author__ = "Jeremy Nelson"

import sys
sys.path.append("src")
import rdf2marc  # type: ignore
import rdflib  # type: ignore
import unittest

class TestRDF2MARCConversion(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_spaces(self) -> None:
        self.assertEqual(rdf2marc.conversion('"   "'), '   ')

    def test_simple_conditional(self) -> None:
        self.assertEqual(rdf2marc.conversion('(value == "") ? "n" : value', ''),
                         "n")
        self.assertEqual(rdf2marc.conversion('(value == "") ? "n" : value', 'a'),
                         "a")

class TestRDF2MARCDataField(unittest.TestCase):

    def setUp(self) -> None:
        self.graph = rdflib.Graph()
        self.field1XX_csv = "bf2marcSpec-1XX-6XX-7XX-8XX-v1.0.csv"

    def test_no_fields(self) -> None:
        no_fields = rdf2marc.data_field(self.graph, self.field1XX_csv)
        self.assertEqual(no_fields, [])


class TestRDF2MARCLeader(unittest.TestCase):

    def setUp(self) -> None:
        self.graph = rdflib.Graph()
        self.leader_csv_path = "bbf2marcSpec-LDR-001-005-v1.0.csv"

    def test_default_leader(self):
        leader = rdf2marc.leader(self.graph, self.leader_csv_path)
        self.assertEqual(leader, '')


class TestRDF2MARC(unittest.TestCase):

    def setUp(self) -> None:
        self.graph = rdflib.Graph()

    def test_main(self):
        record = rdf2marc.main(self.graph)
        self.assertEqual(record, pymarc.Record())
        
