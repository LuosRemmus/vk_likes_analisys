from matplotlib import pyplot as plt
from datetime import datetime


def create_plot(title: str, values: list[int], labels: list[str | int | float], filepath: str, font_size: int = 36,
                font_weight: int = 8):
    font_dict = {
        'fontsize': font_size,
        'fontweight': font_weight
    }
    plt.title(title, y=1.5, fontdict=font_dict)
    plt.axis('equal')
    plt.pie(values, labels=labels, radius=2, autopct='%0.1f%%')
    plt.savefig(filepath, bbox_inches='tight', pad_inches=1)
    print(f'{datetime.utcnow()} [INFO] Plot successfully saved!')
    plt.clf()
