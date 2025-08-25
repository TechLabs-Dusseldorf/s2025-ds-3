import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_lineplot(data, x_col, y_col, title, marker='o'):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x=x_col, y=y_col, marker=marker)
    plt.title(title, fontsize=14)
    plt.xlabel("Year")
    plt.ylabel("Microplastic Content (μg/kg)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


