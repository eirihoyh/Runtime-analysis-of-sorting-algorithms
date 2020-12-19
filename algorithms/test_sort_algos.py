from code.insertion_sort import insertion_sort
from code.bubble_sort import bubble_sort
from code.merge_sort import merge_sort
from code.quick_sort import quick_sort
from code.combo_merge_insert import tim_sort

from analysis.time_algorithm import random_int_list, random_float_list, \
    string_list, increasing_list, decreasing_list


class TestAllAlgorithms:

    size = 100
    diff_lists = [random_int_list, random_float_list, random_float_list, string_list,
                  increasing_list, decreasing_list]

    def test_insertion_sort(self):
        for new_list in self.diff_lists:
            random_list = new_list(self.size)

            # copy the random list and check if random_list get effected
            sorted_list = random_list.copy()
            insertion_sort(sorted_list)
            if new_list != increasing_list:
                assert sorted_list != random_list

            # checks if insertion sort actually works by using python.sort()
            random_list.sort()
            assert sorted_list == random_list

    def test_bubble_sort(self):
        for new_list in self.diff_lists:
            random_list = new_list(self.size)

            sorted_list = random_list.copy()
            bubble_sort(sorted_list)
            if new_list != increasing_list:
                assert random_list != sorted_list

            random_list.sort()
            assert sorted_list == random_list

    def test_merge_sort(self):
        for new_list in self.diff_lists:
            random_list = new_list(self.size)

            sorted_list = random_list.copy()
            merge_sort(sorted_list)
            if new_list != increasing_list:
                assert random_list != sorted_list

            random_list.sort()
            assert sorted_list == random_list

    def test_quick_sort(self):
        for new_list in self.diff_lists:
            random_list = new_list(self.size)

            sorted_list = random_list.copy()
            quick_sort(sorted_list)
            if new_list != increasing_list:
                assert random_list != sorted_list

            random_list.sort()
            assert sorted_list == random_list

    def test_tim_sort(self):
        for new_list in self.diff_lists:
            random_list = new_list(self.size)

            sorted_list = random_list.copy()
            tim_sort(sorted_list)
            if new_list != increasing_list:
                assert random_list != sorted_list

            random_list.sort()
            assert sorted_list == random_list
