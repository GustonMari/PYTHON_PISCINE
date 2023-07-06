from load_csv import load
import matplotlib.pyplot as plt
import numpy as np

def define_max(max1, max2) -> float:
    """Define the max value of the data"""
    max_val: float = 0
    if max1 > max2:
        max_val = max1
    else:
        max_val = max2
    return max_val

def define_min(min1, min2) -> float:
    """Define the min value of the data"""
    min_val: float = 0
    if min1 < min2:
        min_val = min1
    else:
        min_val = min2
    return min_val

def aff_pop():
    """Compare two different country with a plot"""
    path: str = "population_total.csv"
    data = load(path)
    #TODO: attention il faut que les annees soient jusqu'a 2050
    data_fr = data[data['country'] == 'France']
    data_be = data[data['country'] == 'Belgium']
    x = data.columns[1:data.columns.get_loc("2050")+1]
    y1 = data_fr.iloc[0, 1:data.columns.get_loc("2050")+1].str.replace('M', '').astype(float) * 1e6
    y2 = data_be.iloc[0, 1:data.columns.get_loc("2050")+1].str.replace('M', '').astype(float) * 1e6

    # Plot the data
    plt.plot(x, y1, label='France')
    plt.plot(x, y2, label='Belgium')
    plt.xticks(range(0, 2050 - 1800, 40))
    plt.yticks(np.arange(0, max(y1), 20e6), [f"{int(val/1e6)}M" for val in np.arange(0, max(y1), 20e6)])
    # plt.yticks(np.arange(0, max(y1), 20e6), [f"{int(val/1e6)}M" for val in np.arange(0, max(y1), 20e6)])
    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('Population Projections')
    plt.show()

if __name__ == "__main__":
    aff_pop()