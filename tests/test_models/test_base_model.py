"""
Base Model Tests
"""
from datetime import datetime
import unittest

#import pycodestyle

from models.base_model import BaseModel


class test_base_model(unittest.TestCase):
    """Tests"""

    # def test_pep8_base_model(self):
    #     """
    #     Test that checks PEP8 base_model.py
    #     """
    #     syntax = pycodestyle.StyleGuide(quit=True)
    #     check = syntax.check_files(['models/base_model.py'])
    #     self.assertEqual(
    #         check.total_errors, 0,
    #         "Pycodestyle errors found in base_model.py"
    #     )

    # def test_pep8_base_self(self):
    #     """
    #     Test that checks PEP8 test_base_model.py
    #     """
    #     syntax = pycodestyle.StyleGuide(quit=True)
    #     check = syntax.check_files(['tests/test_models/test_base_model.py'])
    #     self.assertEqual(
    #         check.total_errors, 0,
    #         "Pycodestyle errors found in test_base.py"
    #     )

    def test_docum(self):
        """test for documentation"""
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def setUp(self):
        # self.BaseModel._BaseModel__nb_objects = 0
        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def test_id(self):
        """check id"""
        b1 = BaseModel()
        self.assertEqual(type(b1.id), str)

    def test_id_uniq(self):
        """check uniq id"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertTrue(b1.id != b2.id)

    def test_name(self):
        """check name"""
        b1 = BaseModel()
        b1.name = "name test"
        self.assertEqual(b1.name, "name test")

    def test_my_number(self):
        """check my_number"""
        b1 = BaseModel()
        b1.my_number = 89
        self.assertEqual(b1.my_number, 89)

    def test_created_at_type(self):
        """check datetime type"""
        b1 = BaseModel()
        self.assertEqual(type(b1.created_at), datetime)

    def test_update_at_type(self):
        """check datetime type"""
        b1 = BaseModel()
        self.assertEqual(type(b1.updated_at), datetime)

    def test_str(self):
        """check __str__"""
        b1 = BaseModel()
        self.assertTrue(b1.__str__)

    # def test_save(self):
    #     """check json"""
    #     self.assertTrue()


if __name__ == '__main__':
    unittest.main()
