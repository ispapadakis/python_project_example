from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# ON MAC OS Terminal you may need to issue this command:
# open /Applications/Python\ 3.10/Install\ Certificates.com
# Assuming you are using version 3.10

def get_parsed_html(ticker):
    """ Get Ticker Data from finance.google.com (Use HTML PARSER)"""
    url = f"https://www.google.com/finance/quote/{ticker}:NASDAQ"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    return soup

def get_entry_attributes(focus, label_class, attr_class, about_class):
    """
    Have BeautifulSoup Analyze the Focus Section of the HTML and return a dictionary of attributes
    
    Args:
        focus (bs4.BeautifulSoup): focus section from parser html
        label_class (string): class code for the label
        attr_class  (string): class code for the attribute
        about_class (string): class code for the about section

    Returns:
        dict: dictionary of attributes
    """
    out = dict()
    lbls = focus.find_all("div", class_=label_class)
    attrs = focus.find_all("div",class_=attr_class)
    for lbl, a in zip(lbls,attrs):
        out[lbl.get_text()] = a.get_text()
    about_section = focus.find("div",class_=about_class)
    out["About"] = about_section.get_text().replace(" Wikipedia","")
    return out

def scrape_info(ticker):
    """
    After analyzing the class codes of the <div> tags we want, we can have BeautifulSoup do all the work.

    Args:
        ticker (string): Stock Market Ticker Symbol of NASDAQ Company
    """
    soup = get_parsed_html(ticker)
    
    # SECRET SAUCE
    # Go line-by-line in raw HTML code of finance.google.com 
    #   and find the class codes of the <div> tags we want
    # Run scraper_first_pass.py to see raw HTML code
    focus_section_div_class = "v5gaBd SgSxlb"
    label_class = "mfs7Fc"
    attribute_class = "P6K39c"
    about_section_class = "bLLb2d"
    
    focus = soup.find("div", class_=focus_section_div_class)
    entry_attrs = get_entry_attributes(focus,label_class,attribute_class,about_section_class)
    return entry_attrs
        
def scrape_info_table(ticker_list, text_limit=500):
    tbls = []
    keys = []
    for ticker in ticker_list:
        keys.append(ticker)
        d = {k:v[:text_limit] for k,v in scrape_info(ticker).items()}
        tbls.append(pd.Series(d))
    df = pd.concat(tbls, axis=1, keys=keys)
    return df


def main():
    ticker_list = ["TSLA","AAPL","MSFT","AMZN"]
    for tck in ticker_list:
        print("\n"*3)
        d = scrape_info(tck)
        for k, v in d.items():
            print(k,":",v)

    df = scrape_info_table(ticker_list)
    df.to_csv("Data/ticker_info.csv")

if __name__ == "__main__":
    main()