import pandas as pd


def to_console(data):
    print(data)


def write_to_file(data, file_path):
    with open(file_path, 'w') as file:
        file.write(data)


def pandas_to_file(data, file_path):
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
