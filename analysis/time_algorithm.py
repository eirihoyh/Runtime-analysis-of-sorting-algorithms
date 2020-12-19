import numpy as np
import timeit
import copy
import pandas as pd
import string


def time_algorithm(algorithm, repeat=5, seed=12345):
    runtime = {'size': [], 'list_type': [], 'time': []}
    np.random.seed(seed)
    lists = [string_list, decreasing_list, random_float_list, increasing_list, random_int_list]
    for new_list in lists:
        t_ar = 0
        size = 10
        print('start')
        while t_ar < 5:
            try:
                data = new_list(size)
                clock = timeit.Timer(stmt='algo(copy(data))',
                                     globals={'algo': algorithm,
                                              'data': data,
                                              'copy': copy.copy})

                n_ar, t_ar = clock.autorange()

                if t_ar < 1:
                    n_ar = int(n_ar * (1 / t_ar))

                time = np.array(clock.repeat(repeat, number=n_ar)) / n_ar

                runtime['size'].append(size)
                runtime['list_type'].append(new_list.__name__)
                runtime['time'].append(min(time))

                size = 2*size
            except RuntimeError:
                t_ar = 10

    runtime = pd.DataFrame(runtime)
    runtime.to_pickle(path=f'../data/benchmark_{algorithm.__name__}')


def random_float_list(size):
    return list(np.random.uniform(size, size=size))


def random_int_list(size):
    return list(np.random.randint(size, size=size))


def increasing_list(size):
    return list(range(size))


def decreasing_list(size):
    return list(reversed(range(size)))


def string_list(size):
    alphabet = np.array(list(string.ascii_lowercase + ' '))
    return list(np.random.choice(alphabet, size=size))
