from analysis.time_algorithm import random_int_list, random_float_list, \
    string_list, increasing_list, decreasing_list


class TestLists:
    size = 100
    random_lists = [random_int_list, random_float_list, string_list]
    fixed_lists = [increasing_list, decreasing_list]

    def test_random_lists(self):
        for rand in self.random_lists:
            alpha = 0.95
            diff_counter = 0
            rounds = 30
            for _ in range(rounds):
                list_1 = rand(self.size)
                list_2 = rand(self.size)
                if list_1 != list_2:
                    diff_counter += 1

            assert (diff_counter/rounds) > alpha

    def test_fixed_lists(self):
        for fixed in self.fixed_lists:
            alpha = 0.99
            same_counter = 0
            rounds = 30
            for _ in range(rounds):
                list_1 = fixed(self.size)
                list_2 = fixed(self.size)
                if list_1 == list_2:
                    same_counter += 1

            assert (same_counter / rounds) > alpha
