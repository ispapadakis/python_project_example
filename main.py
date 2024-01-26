from scraper import scrape_info_table
from fix_data import fix_format, plot_employees

def main():
    # Scrape Company Data from finance.google.com
    ticker_list = ["TSLA","AAPL","MSFT","AMZN"]
    df = scrape_info_table(ticker_list)
    df = fix_format(df)
    print(df)
    plot_employees(df)

    

if __name__ == "__main__":
    main()