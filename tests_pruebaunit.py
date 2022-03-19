import unittest
from io import StringIO
from unittest.mock import patch

#def add5(v):
#    myval = v + 5
#    return myval

#class tests_add5(unittest.TestCase):
#    def tests_add5(self):
#        self.assertEqual(add5(1),6)
#        self.assertEqual(add5(5),10)

def circumference(radius):
    pi = 3.14
    circunferenceValue = pi * radius *2
    return circunferenceValue


def printCircumference2(radius):
    myCircumference = circumference(radius) #Variable invoca o hace uso de funcion circumference y alberga su resultado.
    circleValue = "{:.2f}".format(myCircumference)
    print ("Circumference of a circle with a radius of " + str(radius) + " is " + str(circleValue))        
#-------------------------------

class test_circum(unittest.TestCase):
    def test_circumference(self):
        self.assertAlmostEqual(circumference(5),31.40)


class tests_PC(unittest.TestCase):
    def test_funcion(self):
        test = 5
        expect_value = "Circumference of a circle with a radius of 5 is 31.40\n"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            printCircumference2(test)
            self.assertEqual(fake_out.getvalue(),expect_value)
            



if __name__ == '__main__':
    unittest.main()

