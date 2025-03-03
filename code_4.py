import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv('./big-mac-full-index.csv')


def get_big_mac_price_by_year(year,country_code):
    result = df[(df['date'].str.startswith(str(year))) & (df['iso_a3'] == country_code)]
    return result[['date', 'iso_a3', 'local_price']]


def get_big_mac_price_by_country(country_code):
    result = df[df['iso_a3'] == country_code]
    return result[['date', 'iso_a3', 'local_price']]

def get_the_cheapest_big_mac_price_by_year(year):
    result = df[df['date'].str.startswith(str(year))]
    return result[result['local_price'] == result['local_price'].min()][['date', 'iso_a3', 'local_price']]

def get_the_most_expensive_big_mac_price_by_year(year):
    result = df[df['date'].str.startswith(str(year))]
    return result[result['local_price'] == result['local_price'].max()][['date', 'iso_a3', 'local_price']]
if __name__ == "__main__":
    
    test_year = "2004"
    test_country = "USA"
    
    print("\nBig Mac Prices for Year and Country:")
    print(get_big_mac_price_by_year(test_year, test_country))

    print("\nBig Mac Price History for Country:")
    print(get_big_mac_price_by_country(test_country))

    print("\nCheapest Big Mac in Year:")
    print(get_the_cheapest_big_mac_price_by_year(test_year))

    print("\nMost Expensive Big Mac in Year:")
    print(get_the_most_expensive_big_mac_price_by_year(test_year))