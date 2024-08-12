from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def main():
    """
    DESCRIPTION
    A program that calls the load function and displays
    the projection of life expectancy in relation to the GDP
    of the year 1900 for each country.

    MATPLOT LIBRARY
    Library for creating static, animated, and interactive
    visualizations in Python.

    """
    life_expectancy = load("life_expectancy_years.csv")
    gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    # Extracting the year 1900 and converting it into nparray
    # Not mandatory but NumPy arrays are more efficient for
    # numerical operations
    y = np.array(life_expectancy['1900'])
    x = np.array(gdp['1900'])
    # Matplotlib will skip NaN values when plotting the data points.
    # No need to resize or parse the arrays
    plt.scatter(x, y, color='purple')
    # naming the x axis
    plt.xlabel('GDP')
    # naming the y axis
    plt.ylabel('Life expentancy')
    # giving a title to my graph
    plt.title('Life expectancy vs. GDP in 1900')
    # seting the scale of the x-axis to logarithmic.
    # values are spaced according to the logarithm of the actual value
    plt.xscale('log')
    # setting the current tick locations and labels of the x-axis.
    plt.xticks([300, 1000, 10000], ['300', '1K', '10K'])
    plt.show()


if __name__ == "__main__":
    main()
