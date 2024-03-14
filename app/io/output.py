import pandas as pd


def to_console(data):
    """
    Prints the given data to the console.

    Args:
        data: Data to be printed.
    """
    print(data)


def write_to_file(data, file_path):
    """
    Writes data to a file.

    Args:
        data: Data to be written.
        file_path (str): Path to the file where the data will be written.
    """
    with open(file_path, 'w') as file:
        file.write(data)


def pandas_to_file(data, file_path):
    """
    Writes a pandas DataFrame to a CSV file.

    Args:
        data(DataFrame): DataFrame to be written.
        file_path (str): Path to the CSV file where the DataFrame will be written.
    """
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
