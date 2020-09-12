import unittest
from A.front_end.student import *
from A.model.studentt import*
from A.back_end.connection import *

class test_student_app(unittest.TestCase):
    def test_get_name(self):
        e=studentt('1','2','3','male','3','4')
        self.assertTrue('1',e.get_Name())

    def test_get_rollno(self):
        e=studentt('john','2','john@gmail.com','male','090990099','1988')
        self.assertEqual('2',e.get_Roll_no())


    def test_get_email(self):
        e = studentt('hello', '1', '213123', 'male', '123', '213')
        self.assertEqual('213123', e.get_email())

    def test_get_gender(self):
        e = studentt('softwarica', '2', 'softwarica@python.com', 'others', '123456789', '2010')
        self.assertEqual('others', e.get_gender())


    def test_get_contact(self):
        e = studentt('samsung', '77', 'samsung@gmail.com', 'male', '77889900', '1995')
        self.assertEqual('77889900', e.get_contact())




