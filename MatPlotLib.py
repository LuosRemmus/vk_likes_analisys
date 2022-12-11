from matplotlib import pyplot as plt


def create_plot(title: str, values: list[int], labels: list[any], filepath: str):
    plt.title(title, y=2)
    plt.axis('equal')
    plt.pie(values, labels=labels, radius=3, autopct='%0.1f%%')
    plt.savefig(filepath, bbox_inches='tight', pad_inches=2)
    print('[INFO] Plot successfully saved!')
    plt.clf()
