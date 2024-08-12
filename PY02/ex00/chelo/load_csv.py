import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Takes a path as argument, writes the dimensions of the data set
    and returns it.

    Parameters:
        path (str): The file path of the CSV file to load.

    Returns:
        pd.DataFrame: The DataFrame containing the data from the CSV file.

    Raises:
        FileNotFoundError: If the specified file is not found.
        pd.errors.ParserError: If there is an error parsing the CSV file.
        pd.errors.EmptyDataError: If no data is found in the CSV file.
        AssertionError: If the file is not a CSV file.
    """
    try:
        data = None
        assert path.endswith('.csv'), "File is not a CSV file."
        data = pd.read_csv(path)
        # print(data.info())
        # shape: Returns a tuple representing the dimensionality
        # of the dataset
        print(f'Loading dataset of dimesions: {data.shape}')
    except FileNotFoundError:
        print("File not found.")
    except pd.errors.ParserError:
        print("Unable to parse CSV file.")
    except pd.errors.EmptyDataError:
        print("No data found")
    except AssertionError as e:
        print("Error:", e)
    return data
