from scraper import scrape_info_table
from fix_data import fix_format, plot_employees

def main():
    """
    Bring Everything Together

    - Create a list of Company Ticker Symbol (Search the internet for Nasdaq Ticker Symbols)
    - Collect Results in a Pandas Data Frame using <scrape_info_table>
    - Change format of Founded from str to date and of Employees from str to int using fix_format
    - Print the result
    - Show a graph of the results using <plot_employees>
    """
    ticker_list = ["TSLA","AAPL","MSFT","AMZN"]
    df = scrape_info_table(ticker_list)
    df = fix_format(df)
    print(df)
    plot_employees(df)

if __name__ == "__main__":
    main()