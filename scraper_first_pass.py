from urllib.request import urlopen
from bs4 import BeautifulSoup
#import re

# FOLLOW LINK https://www.google.com/finance/quote/AAPL:NASDAQ for INFO

def get_raw_text(ticker):
    """ Get Ticker Data from finance.google.com (Without HTML PARSER)"""
    url = f"https://www.google.com/finance/quote/{ticker}:NASDAQ"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html

def get_parsed_text(ticker):
    """ Get Ticker Data from finance.google.com (Use HTML PARSER)"""
    url = f"https://www.google.com/finance/quote/{ticker}:NASDAQ"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    return soup

html = get_raw_text("AAPL")
about_loc = html.find(">About<")
print("WHAT I GOT USING RAW TEXT")
print(html[(about_loc-1000):about_loc+4000])
print("\n"*2)

    
#fragment = re.search(r"(>About<).*?(<div class=.*</div>)(.*)( <a target.*?Wikipedia)", html, re.DOTALL)
#if fragment is not None:
#    print(fragment.groups())
#else:
#    print("regex not found")

print("WHAT I GET USING HTML PARSER AND EXTRA WORK")
soup = get_parsed_text("TSLA")

txt = soup.get_text()
about_loc = txt.find("About\ue316\ue313")
wikipedia_loc = txt[about_loc:].find(" Wikipedia") + about_loc
ceo_loc = txt[about_loc:].find("CEO") + about_loc
founded_loc = txt[ceo_loc:].find("Founded") + ceo_loc
website_loc = txt[founded_loc:].find("Website") + founded_loc
employees_loc = txt[website_loc:].find("Employees") + website_loc
dicover_loc = txt[employees_loc:].find("Discover more") + employees_loc
print(txt[about_loc:wikipedia_loc])
print(txt[ceo_loc:founded_loc])
print(txt[founded_loc:website_loc])
print(txt[website_loc:employees_loc])
print(txt[employees_loc:dicover_loc])

print("\nTHE UNREADABLE STUFF IS YOUR FRIEND")
for x in txt[about_loc:about_loc + 7]:
    print(x, "ASCII CODE:", ascii(x))
