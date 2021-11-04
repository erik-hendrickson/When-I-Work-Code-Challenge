import string
import pandas as pd
import sys
import requests

def main():

    print(get_raw_data.__doc__)
    print(pivot_raw_data.__doc__)

    filenames = list(string.ascii_lowercase)

    extension = '.csv'

    base_url = 'https://public.wiwdata.com/engineering-challenge/data/'

    save_raw_files = 0

    df = get_raw_data(base_url, filenames, extension, save_raw_files)

    df_pivoted = pivot_raw_data(df)

    print("Saving pivoted data to file 'web_traffic_pivoted.csv' ")
    df_pivoted.to_csv('web_traffic_pivoted.csv')


def pivot_raw_data(df):
    """
    ---
    Function:
    pivot_raw_data(df)

    Summary:
    Pivots the dataframe "df" using user_id as the index,
    path as the columns, and length as the values

    Parameters:
    df (dataframe): Datafrome of raw data from the get_raw_data

    Returns:
    df_pivoted: Dataframe of pivoted values
    """
    print("Pivoting dataframe...")
    try:
        df_pivoted = df.pivot(index='user_id', columns='path', values='length')

    except:
        print('Error when pivoting')
        sys.exit(1)

    return df_pivoted


def get_raw_data(base_url, filenames, extension, save_raw_files):

    """
    ---
    Function:
    get_raw_data(base_url, filenames, extension, save_raw_files)

    Summary:
    Attempts to download files in "filesnames" with extensions
    from "extension" from "base_url"

    Parameters:
    base_url (string): The base url to pull all files from
    filenames (list): The list of files names (without extensions) to attempt to download from the base_url
    extension (string): The extension to be added to all filenames when attempting to download from base_url
    save_raw_files (int): A flag to indicate of the raw data from the files downloaded should be saved. 1 = True

    Returns:
    df_all_data: Dataframe of values from all files downloaded
    """

    df_all_data = pd.DataFrame()

    for file in filenames:
        full_filename = file + extension
        full_url = base_url + full_filename

        # Get each file by name from the URL. Exit on failure
        try:
            print("Attempting to get data from file: " + full_url)
            df = pd.read_csv(full_url)

        except:
            print('Error with ' + full_url)
            sys.exit(1)

        if save_raw_files == 1:
            print("Saving data to file: " + full_filename)
            df.to_csv(full_filename)

        # Add current file data to main dataframe
        print("Appending data from " + full_filename + " to staging dataframe")
        df_all_data = df_all_data.append(df, ignore_index=True)

    return df_all_data


if __name__ == "__main__":
    main()
