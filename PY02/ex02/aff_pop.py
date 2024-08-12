import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from load_csv import load


def to_numeric(df):
    return df.apply(
        lambda col: col.map(lambda x: float(str(x).replace('M', ''))))


def get_data(df: pd.DataFrame, name: str, start: str, end: str) -> np.ndarray:
    try:
        campus_data = df[df.country == name]
        campus_data_in_range = to_numeric(campus_data.loc[:, (start):(end)])
        values_of_campus = campus_data_in_range.iloc[0].values
        return values_of_campus
    except IndexError as e:
        print(f'Error {e} | Maybe you choose a not valid country')
    return None


def aff_pop(path: str, campus_1: str, campus_2: str, start: str, end: str):
    try:
        assert path.endswith(".csv"), "Not a .csv file!"
        df = load(path)

        # Getting values from data
        campus_1_values = get_data(df, campus_1, start, end)
        campus_2_values = get_data(df, campus_2, start, end)

        if campus_1_values is not None and campus_2_values is not None:
            # Getting years
            year_col = df.columns[df.columns.to_series().between(start, end)]
            years = year_col.astype(int)

            # Plotting the data
            plt.figure(figsize=(12, 6))
            plt.plot(years, campus_1_values, label=f'{campus_1}')
            plt.plot(years, campus_2_values, label=f'{campus_2}')
            # Adding the legends
            plt.legend()
            # Set X-axis Y-axis major ticks and labels
            plt.yticks([20, 40, 60], ['20M', '40M', '60M'])
            plt.xticks(list(range(1800, 2041, 40)))

            # Set Y-axis limits to ensure there is space below 20
            plt.xlim(1780, 2060)
            plt.ylim(0, 70)

            # Labels and plot
            plt.xlabel('Year')
            plt.ylabel('Population')
            plt.title('Population Projection')

            # Display the plot
            plt.show()
    except AssertionError as e:
        print("Error: ", e)


def main():
    try:
        aff_pop("population_total.csv", "France", "Colombia", "1800", "2050")
    except AssertionError as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()
