from app.io.input import *
from app.io.output import *

TEST_FOLDER = "test_folder/"


def main():
    test_for_console = read_from_console()
    to_console(test_for_console)

    input_file = TEST_FOLDER + "sample.txt"
    text_from_file = read_from_file(input_file)
    output_file = TEST_FOLDER+"output.txt"
    write_to_file(text_from_file, output_file)
    to_console(text_from_file)

    input_csv = TEST_FOLDER + "sample.csv"
    df_from_file = read_pandas(input_csv)
    output_csv = TEST_FOLDER+"output.csv"
    pandas_to_file(df_from_file, output_csv)
    to_console(df_from_file)
    pass


if __name__ == "__main__":
    main()
