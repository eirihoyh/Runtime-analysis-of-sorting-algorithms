import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def new_figure(height=55):
    "Return figure with width 84mm and given height in mm."

    return plt.figure(figsize=(84/25.4, height/25.4))


def save_figures(data):
    fig = new_figure()
    ax = fig.add_subplot(1, 1, 1)
    name = data['list_type'][0]
    grid = sns.scatterplot(data=data, x="size", y="time", hue="algorithm", style="algorithm",
                           edgecolor="none", s=20, palette=['purple', 'green', 'navy', 'orange',
                                                            'lightpink', 'black', 'gray'])
    grid.set(xscale="log", yscale="log", xlabel="List size", ylabel="Time (s)", title=f'{name}')
    legend = ax.legend(prop={'size': 5}, title='Algorithms')
    plt.setp(legend.get_title(), fontsize='xx-small')
    fig.savefig(f'../figures/{name}.pdf', bbox_inches='tight')


if __name__ == '__main__':
    ins_sort = pd.read_pickle("../data/benchmark_insertion_sort")
    ins_sort.name = 'Insertion sort'
    bub_sort = pd.read_pickle("../data/benchmark_bubble_sort")
    bub_sort.name = 'Bubble sort'
    tim_sort = pd.read_pickle("../data/benchmark_tim_sort")
    tim_sort.name = 'Timsort'
    quick_sort = pd.read_pickle("../data/benchmark_quick_sort")
    quick_sort.name = 'Quicksort'
    python_sort = pd.read_pickle("../data/benchmark_python_sort")
    python_sort.name = 'Python sort'
    numpy_sort = pd.read_pickle("../data/benchmark_numpy_sort")
    numpy_sort.name = 'Numpy sort'
    merge_sort = pd.read_pickle("../data/benchmark_merge_sort")
    merge_sort.name = 'Mergesort'
    dataframe = [ins_sort, bub_sort, tim_sort, merge_sort, quick_sort, python_sort, numpy_sort]

    random_int_df = {'size': [], 'algorithm': [], 'list_type': [], 'time': []}
    random_float_df = {'size': [], 'algorithm': [], 'list_type': [], 'time': []}
    string_list_df = {'size': [], 'algorithm': [], 'list_type': [], 'time': []}
    increasing_list_df = {'size': [], 'algorithm': [], 'list_type': [], 'time': []}
    decreasing_list_df = {'size': [], 'algorithm': [], 'list_type': [], 'time': []}

    for df in dataframe:
        random_int_list = df.query("list_type == 'random_int_list'")

        for val in random_int_list.index:
            line = random_int_list.query(f"index == {val}")
            random_int_df['time'].append(line['time'].values[0])
            random_int_df['size'].append(line['size'].values[0])
            random_int_df['list_type'].append(line['list_type'].values[0])
            random_int_df['algorithm'].append(df.name)

        random_float_list = df.query("list_type == 'random_float_list'")

        for val in random_float_list.index:
            line = random_float_list.query(f"index == {val}")
            random_float_df['time'].append(line['time'].values[0])
            random_float_df['size'].append(line['size'].values[0])
            random_float_df['list_type'].append(line['list_type'].values[0])
            random_float_df['algorithm'].append(df.name)

        increasing_list = df.query("list_type == 'increasing_list'")

        for val in increasing_list.index:
            line = increasing_list.query(f"index == {val}")
            increasing_list_df['time'].append(line['time'].values[0])
            increasing_list_df['size'].append(line['size'].values[0])
            increasing_list_df['list_type'].append(line['list_type'].values[0])
            increasing_list_df['algorithm'].append(df.name)

        decreasing_list = df.query("list_type == 'decreasing_list'")

        for val in decreasing_list.index:
            line = decreasing_list.query(f"index == {val}")
            decreasing_list_df['time'].append(line['time'].values[0])
            decreasing_list_df['size'].append(line['size'].values[0])
            decreasing_list_df['list_type'].append(line['list_type'].values[0])
            decreasing_list_df['algorithm'].append(df.name)

        string_list = df.query("list_type == 'string_list'")

        for val in string_list.index:
            line = string_list.query(f"index == {val}")
            string_list_df['time'].append(line['time'].values[0])
            string_list_df['size'].append(line['size'].values[0])
            string_list_df['list_type'].append(line['list_type'].values[0])
            string_list_df['algorithm'].append(df.name)

    plots = [random_int_df, increasing_list_df, random_float_df, decreasing_list_df, string_list_df]
    for plot in plots:
        save_figures(plot)
