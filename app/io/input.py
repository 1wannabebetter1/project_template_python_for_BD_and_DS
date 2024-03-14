import pandas as pd


def read_from_console():
    """
    Reads data input from the console.

    Return:
        (str). Data entered by the user.
    """
    data = input("Insert your data")
    return data


def read_from_file(file_path):
    """
    Reads data from a file.

    Args:
        file_path (str): Path to the file to be read.

    Return:
        (str). Content of the file.
    """
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return "File not found"


def read_pandas(file_path):
    """
    Reads data from a CSV file into a pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file.

    Return:
        pandas.DataFrame: pandas.DataFrame or None: DataFrame containing the CSV data, or None if the file is not found.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File not found")
        return None
