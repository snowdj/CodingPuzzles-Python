import unittest
import time

from CodingPuzzles.sort.src import insert_sort
from CodingPuzzles.sort.src import merge_sort
from CodingPuzzles.sort.src import bubble_sort
from CodingPuzzles.sort.src import quick_sort

class SortTestCase(unittest.TestCase):
    def setUp(self):
        print("Setup SortTestCase")

    def test_insert_sort_t0(self):
        print("TestCase: test_insert_sort_t0")

        input_list = []
        print("Input: ", input_list)
        res = insert_sort.InsertionSort(input_list)
        print("Result: ", res)
        self.assertEqual(res, sorted(input_list))

    def test_insert_sort_t1(self):
        print("TestCase: test_insert_sort_t1")
        start_time = time.clock()

        #input = raw_input('Please input numbers to be sorted, separate by space:')
        #for item in input.split(' '):
        #    input_list.append(int(item))

        input_list = [3, 8, 29, 52, 12, 38, 42, 11]
        print("Input: ", input_list)
        res = insert_sort.InsertionSort(input_list)
        print("Result: ", res)
        self.assertEqual(res, sorted(input_list))

        print("--- %s seconds ---" % (time.clock() - start_time))

    def test_merge_sort_t0(self):
        print("TestCase: test_merge_sort_t0")

        input_list = []
        print("Input: ", input_list)
        res = merge_sort.MergeSort(input_list)
        print("Result: ", res)
        self.assertEqual(res, sorted(input_list))

    def test_merge_sort_t1(self):
        print("TestCase: test_merge_sort_t1")
        start_time = time.clock()

        input_list = [3, 8, 29, 52, 12, 38, 42, 11]
        print("Input: ", input_list)
        res = merge_sort.MergeSort(input_list)
        print("Result: ", res)
        self.assertEqual(res, sorted(input_list))

        print("--- %s seconds ---" % (time.clock() - start_time))

    def test_bubble_sort_t0(self):
        print("TestCase: test_bubble_sort_t0")

        input_list = []
        print("Input: ", input_list)
        res = bubble_sort.BubbleSort(input_list)
        print("Result: ", res)
        self.assertEqual(res, sorted(input_list))

    def test_bubble_sort_t1(self):
        print("TestCase: test_bubble_sort_t1")
        start_time = time.clock()

        input_list = [3, 8, 29, 52, 12, 38, 42, 11]
        print("Input: ", input_list)
        res = bubble_sort.BubbleSort(input_list)
        print("Result: ", res)
        self.assertEqual(res, sorted(input_list))

        print("--- %s seconds ---" % (time.clock() - start_time))

    def test_quick_sort_t0(self):
        print("TestCase: test_quick_sort_t0")

        input_list = []
        print("Input: ", input_list)
        res = quick_sort.QuickSort(input_list)
        print("Result: ", res)
        self.assertEqual(res, sorted(input_list))

    def test_quick_sort_t1(self):
        print("TestCase: test_quick_sort_t1")
        start_time = time.clock()

        input_list = [3, 8, 29, 52, 12, 38, 42, 11]
        print("Input: ", input_list)
        res = quick_sort.QuickSort(input_list)
        print("Result: ", res)
        self.assertEqual(res, sorted(input_list))

        print("--- %s seconds ---" % (time.clock() - start_time))
        
    def tearDown(self):
        print("Bye Test")

if __name__ == '__main__':
    unittest.main()
