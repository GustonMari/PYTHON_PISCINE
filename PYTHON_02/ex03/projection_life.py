from load_csv import load
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

if __name__ == "__main__":
    data_life = load("life_expectancy_years.csv")
    data_growth = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    data_life = data_life["1900"]
    data_growth = data_growth["1900"]
    print(data_life)
    # print(data_growth)
    plt.scatter(data_growth, data_life, label='1900')

    # Set the axis labels and title
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.title('1900')

    # Add legend
    plt.legend()

    # Display the plot
    plt.show()