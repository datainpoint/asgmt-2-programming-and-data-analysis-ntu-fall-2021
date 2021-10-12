import unittest
import ipynb.fs.full.exercises as ex

class TestAssignmentTwo(unittest.TestCase):
    def test_01_find_bmi_category(self):
        self.assertEqual(ex.find_bmi_category(32.90), "Class I Obese")
        self.assertEqual(ex.find_bmi_category(26.63), "Pre-obese")
        self.assertEqual(ex.find_bmi_category(24.83), "Normal range")
        self.assertEqual(ex.find_bmi_category(17.58), "Mild thinness")
    def test_02_convert_kilometer_to_mile(self):
        self.assertTrue(ex.convert_temperature_degrees_to_different_scales(0, "Celsius", "Fahrenheit") >= 32)
        self.assertTrue(ex.convert_temperature_degrees_to_different_scales(100, "Celsius", "Fahrenheit") >= 212)
        self.assertTrue(ex.convert_temperature_degrees_to_different_scales(32, "Fahrenheit", "Celsius") >= 0)
        self.assertTrue(ex.convert_temperature_degrees_to_different_scales(212, "Fahrenheit", "Celsius") >= 100)
        self.assertTrue(ex.convert_temperature_degrees_to_different_scales(0, "Celsius", "Kelvin") >= 273)
        self.assertTrue(ex.convert_temperature_degrees_to_different_scales(100, "Celsius", "Kelvin") >= 373)
        self.assertTrue(ex.convert_temperature_degrees_to_different_scales(32, "Fahrenheit", "Kelvin") >= 273)
        self.assertTrue(ex.convert_temperature_degrees_to_different_scales(212, "Fahrenheit", "Kelvin") >= 373)
    def test_03_check_types(self):
        self.assertEqual(ex.check_types(1), 'int')
        self.assertEqual(ex.check_types(1.0), 'float')
        self.assertEqual(ex.check_types(False), 'bool')
        self.assertEqual(ex.check_types(True), 'bool')
        self.assertEqual(ex.check_types("5566"), 'str')
        self.assertEqual(ex.check_types(None), 'NoneType')
    def test_04_fizz_buzz(self):
        self.assertEqual(ex.fizz_buzz(0), 'Fizz Buzz')
        self.assertEqual(ex.fizz_buzz(3), 'Fizz')
        self.assertEqual(ex.fizz_buzz(5), 'Buzz')
        self.assertEqual(ex.fizz_buzz(15), 'Fizz Buzz')
        self.assertEqual(ex.fizz_buzz(16), 16)
    def test_05_first_n_fizz_buzz(self):
        self.assertEqual(ex.first_n_fizz_buzz(1), ['Fizz Buzz'])
        self.assertEqual(ex.first_n_fizz_buzz(2), ['Fizz Buzz', 1])
        self.assertEqual(ex.first_n_fizz_buzz(4), ['Fizz Buzz', 1, 2, 'Fizz'])
        self.assertEqual(ex.first_n_fizz_buzz(6), ['Fizz Buzz', 1, 2, 'Fizz', 4, 'Buzz'])
        self.assertEqual(ex.first_n_fizz_buzz(16), ['Fizz Buzz', 1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz Buzz'])
    def test_06_retrieve_the_middle_elements(self):
        self.assertEqual(ex.retrieve_the_middle_elements([2, 3, 5]), 3)
        self.assertEqual(ex.retrieve_the_middle_elements([2, 3, 5, 7]), (3, 5))
        self.assertEqual(ex.retrieve_the_middle_elements([2, 3, 5, 7, 11]), 5)
        self.assertEqual(ex.retrieve_the_middle_elements([2, 3, 5, 7, 11, 13]), (5, 7))
    def test_07_median(self):
        self.assertEqual(ex.median([2, 3, 5, 7, 11]), 5)
        self.assertEqual(ex.median([2, 3, 5, 7, 11, 13]), 6.0)
        self.assertEqual(ex.median([11, 13, 17, 2, 3, 5, 7]), 7)
        self.assertEqual(ex.median([7, 11, 13, 17, 19, 2, 3, 5]), 9.0)
    def test_08_collect_divisors(self):
        self.assertEqual(ex.collect_divisors(1), [1])
        self.assertEqual(ex.collect_divisors(2), [1, 2])
        self.assertEqual(ex.collect_divisors(3), [1, 3])
        self.assertEqual(ex.collect_divisors(4), [1, 2, 4])
        self.assertEqual(ex.collect_divisors(5), [1, 5])
        self.assertEqual(ex.collect_divisors(6), [1, 2, 3, 6])
        self.assertEqual(ex.collect_divisors(7), [1, 7])
    def test_09_is_prime(self):
        self.assertFalse(ex.is_prime(1))
        self.assertTrue(ex.is_prime(2))
        self.assertTrue(ex.is_prime(3))
        self.assertFalse(ex.is_prime(4))
        self.assertTrue(ex.is_prime(5))
        self.assertFalse(ex.is_prime(6))
        self.assertTrue(ex.is_prime(7))
    def test_10_reverse_vowels(self):
        self.assertEqual(ex.reverse_vowels('Luke Skywalker'), 'LUkE SkywAlkEr')
        self.assertEqual(ex.reverse_vowels('Darth Vadar'), 'DArth VAdAr')
        self.assertEqual(ex.reverse_vowels('The Avengers'), 'ThE avEngErs')
        self.assertEqual(ex.reverse_vowels('Python'), 'PythOn')
        self.assertEqual(ex.reverse_vowels('Anaconda'), 'anAcOndA')

suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentTwo)
runner = unittest.TextTestRunner(verbosity=2)
if __name__ == '__main__':
    test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print("You've got {} successes among {} questions.".format(number_of_successes, number_of_test_runs))