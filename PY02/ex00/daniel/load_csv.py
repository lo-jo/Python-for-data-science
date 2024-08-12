import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Loads a dataset from a CSV file and returns it as a pandas DataFrame.

    Parameters:
    -----------
    path : str
        The file path to the CSV file to be loaded.

    Returns:
    --------
    pd.DataFrame
        A pandas DataFrame containing the data from the CSV file.
        If the file cannot be loaded, returns None.

    Exceptions:
    -----------
    FileNotFoundError:
        Raised when the file at the specified path does not exist.

    pd.errors.ParserError:
        Raised when the file cannot be parsed as a CSV.

    pd.errors.EmptyDataError:
        Raised when the file is empty or contains no data.

    AssertionError:
        Raised for any other assertion errors encountered during loading.

    Notes:
    ------
    The function prints a message indicating the dimensions of the loaded
    dataset if loading is successful. If an error occurs, an appropriate
    error message is printed.
    """

    table = None
    try:
        assert path.endswith('.csv'), "load function only supports csv files."
        table = pd.read_csv(path)
        dimensions = table.shape
        print(f"Loading dataset of dimensions {dimensions}")
    except FileNotFoundError:
        print("File not found.")
    except pd.errors.ParserError:
        print("Unable to parse CSV file.")
    except pd.errors.EmptyDataError:
        print("No data found")
    except AssertionError as e:
        print("Error:", e)
    return (table)
