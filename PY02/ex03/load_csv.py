import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    DESCRIPTION :
    function that takes a path as argument,
    writes the dimensions of the data set and returns it.
    ABOUT PANDAS LIBRARY :
    A pandas DataFrame is a two-dimensional data structure
    similar to a table in a relational database or a spreadsheet.
    It consists of rows and columns.
    Each column can have a different data type (e.g., integer, float, string).
    However, all columns must have the same length.
    """
    dataset = None
    try:
        if not path.lower().endswith('.csv'):
            raise AssertionError("The file is not a CSV format.")
        # Use the .read_csv method to convert the data set into a DataFrame
        dataset = pd.read_csv(path)
        print(f"LOADING DATASET OF DIMENSIONS {dataset.shape}")
    except FileNotFoundError:
        print("FILE NOT FOUND")
    except pd.errors.EmptyDataError:
        print("No data")
    except pd.errors.ParserError:
        print("Parser error")
    except AssertionError as e:
        print(e)
    return dataset
