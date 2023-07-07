from load_csv import load
import matplotlib.pyplot as plt


def printplot():
    """Prints a plot of the life expectancy in France"""
    path: str = "life_expectancy_years.csv"
    data = load(path)
    data = data[data["country"] == "France"]

    # ! extract the years by selecting all columns starting from the 2nd column
    years = data.columns[1:].astype(int)
    # ! extract the life expectancy by selecting all rows from the first column
    life_expectancy = data.iloc[0, 1:].values

    plt.plot(years, life_expectancy)
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.title('France Life expectancy Projections')
    plt.show()


if __name__ == "__main__":
    """main function"""
    printplot()
