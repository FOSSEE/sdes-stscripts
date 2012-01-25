import fibonacci
import unittest

class TestFibonacciFunction(unittest.TestCase):

    def setUp(self):
        self.test_file = open('fibonacci_testcases.dat')
        self.test_cases = []
        for line in self.test_file:
            values = line.split(', ')
            n = int(values[0])
            a = int(values[1])
            
            self.test_cases.append([n, a])

    def test_fibonacci(self):
        for case in self.test_cases:
            n = case[0]
            a = case[1]
            self.assertEqual(fibonacci.fibonacci(n),a)

    def tearDown(self):
        self.test_file.close()
        del self.test_cases

if __name__ == '__main__':
    unittest.main()
