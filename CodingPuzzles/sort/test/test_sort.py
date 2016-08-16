import unittest

from CodingPuzzles.sort.lib import insert_sort

class SortTestCase(unittest.TestCase):
    def setUp(self):
        print("Setup SortTestCase")

    def test_insert_sort_t0(self):
        print("TestCase: test_insert_sort_t0")

        #input = raw_input('Please input numbers to be sorted, separate by space:')
        #for item in input.split(' '):
        #    input_list.append(int(item))

        input_list = [3, 8, 29, 52, 12, 38, 42, 11]
        print("Input: ", input_list)
        res = insert_sort.InsertionSort(input_list)
        print("Result: ", res)
        self.assertEqual(res, sorted(input_list))


    def test_insert_sort_t1(self):
        print("TestCase: test_insert_sort_t1")

        input_list = []
        print("Input: ", input_list)
        res = insert_sort.InsertionSort(input_list)
        print("Result: ", res)
        self.assertEqual(res, sorted(input_list))

    def tearDown(self):
        print("Bye Test")

if __name__ == '__main__':
    unittest.main()
