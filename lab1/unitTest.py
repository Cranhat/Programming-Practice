import unittest
import re

def Add(input):
    numbers = re.split(r"[,\n]", input)
    sum = 0
    size = len(numbers)
    for number in numbers:
        if(number == "" and size > 1):
            raise(ValueError)
        elif(number != ""):
            sum += int(number)
    return sum

class TestMyMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Add("1,1"), 2)
        self.assertEqual(Add("1,9"), 10)
        self.assertEqual(Add("1"), 1)
        self.assertEqual(Add(""), 0)
        self.assertEqual(Add("1,1,1"), 3)
        self.assertEqual(Add("1,2,3,4,5,6,7,8,9"), 45)

    def test_wrong_input(self):
        with self.assertRaises(ValueError):
            Add("2,,4")
        with self.assertRaises(ValueError):
            Add(",1")
        with self.assertRaises(ValueError):
            Add("1,")
        with self.assertRaises(ValueError):
            Add(",")
        with self.assertRaises(ValueError):
            Add("1,3,,7")

    def test_n_comma(self):
        self.assertEqual(Add("1\n1"), 2)
        self.assertEqual(Add("1\n9"), 10)
        self.assertEqual(Add("1"), 1)
        self.assertEqual(Add(""), 0)
        self.assertEqual(Add("1\n1\n1"), 3)
        self.assertEqual(Add("1,2\n3,4,5\n6,7,8\n9"), 45)

    def test_wrong_input_n_comma(self):
        with self.assertRaises(ValueError):
            Add("2\n,4")
        with self.assertRaises(ValueError):
            Add("\n1")
        with self.assertRaises(ValueError):
            Add("1\n")
        with self.assertRaises(ValueError):
            Add("\n")
        with self.assertRaises(ValueError):
            Add("1\n3\n\n7")