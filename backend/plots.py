from matplotlib import pyplot as plt
from backend.config import MEDIA_FILEPATH


def create_plot(
        title: str, 
        values: dict.values, 
        labels: dict.keys, 
        filepath: str = MEDIA_FILEPATH):

    font_dict_lables = {
        'family': 'sans-serif',
        'color': 'blue',
        'weight': 'bold',
        'size': 24,
    }

    fig, ax = plt.subplots(figsize=(10, 15))
    ax.bar(labels, values)
    plt.xticks(rotation='vertical')
    ax.set_xlabel(title, fontdict=font_dict_lables)
    ax.set_ylabel("values", fontdict=font_dict_lables)
    ax.set_title(title)
    plt.savefig(f"{filepath}/{title}.png")
    plt.close()
