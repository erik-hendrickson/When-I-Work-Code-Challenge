import string
import pandas as pd
import sys


def main():

    # Variables #

    # filenames is a list of strings indicating the names of the required files (without file extensions)
    # It is currently defined using the letters 'a' through 'z', but can also be manually defined using this format:
    # filenames = ['a','b']

    filenames = list(string.ascii_lowercase)

    # extension is the default file extension for the filenames above. In this case, '.csv'

    extension = '.csv'

    # base_url is the default URL utilized to pull the files by name and extension (defined above).
    # This can be modified if the URL were to change

    base_url = 'https://public.wiwdata.com/engineering-challenge/data/'

    # save_raw_files is a flag used to indicate the desire to save the raw data files after download
    # Set to 1 to save the files

    save_raw_files = 0

    # End Variables #

    # Get all files using above variables, store data in dataframe df
    df = get_raw_data(base_url, filenames, extension, save_raw_files)

    # Pivot the raw data
    # Index on user_id, use path values as columns, length as values
    df_pivoted = pivot_raw_data(df)

    # Save pivoted data to a csv
    df_pivoted.to_csv('web_traffic_pivoted.csv')


def pivot_raw_data(df):
    df_pivoted = df.pivot(index='user_id', columns='path', values='length')

    return df_pivoted


def get_raw_data(base_url, filenames, extension, save_raw_files):

    df_all_data = pd.DataFrame()

    for file in filenames:
        full_filename = file + extension
        full_url = base_url + full_filename

        # Get each file by name from the URL. Exit on failure
        try:
            df = pd.read_csv(full_url)
        except:
            print('Error with ' + full_url)
            sys.exit(1)

        if save_raw_files == 1:
            df.to_csv(full_filename)

        # Add current file data to main dataframe
        df_all_data = df_all_data.append(df, ignore_index=True)

    return df_all_data


if __name__ == "__main__":
    main()
