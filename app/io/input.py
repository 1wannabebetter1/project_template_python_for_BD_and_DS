import pandas as pd


def read_from_console():
    data = input("Insert your data")
    return data


def read_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return "File not found"


def read_pandas(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        return "File not found"
