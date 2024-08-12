from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def display_campus_info(filename, country):
    try:
        data = load(filename)
        assert isinstance(data, pd.DataFrame), ""
        # Filter rows by country
        campus_data = data[data['country'] == country]
        assert not campus_data.empty, f"Data for {country} not found."
        # Extracting years from column names
        years = data.columns[1:]
        # Extracting life expectancy values for the specified country
        life_expectancy = campus_data.iloc[:, 1:].values.flatten()
        plt.plot(years, life_expectancy, linestyle='-')
        plt.title(f"{country} Life Expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        # Set x-axis ticks every 40 years
        plt.xticks(years[::40])
        plt.show()
    except AssertionError as e:
        print(e)


def main():
    try:
        display_campus_info("life_expectancy_years.csv", "France")
    except AssertionError as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()
