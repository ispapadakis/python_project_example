import pandas as pd
import matplotlib.pyplot as plt

def fix_format(df):
    """
    Transform Pandas Data Frame

    After scraping all results are in str form
    Change Employees to int
    Change Founded to date
    Remove 'United States' from the Headquarters string

    Args:
        df (pandas.DataFrame): Raw Results

    Returns:
        df (pandas.DataFrame): Processed Results
    """
    df['Headquarters'] = df['Headquarters'].apply(lambda x: "Unknown" if type(x) is float else x.replace("United States",""))
    df["Employees"] = df["Employees"].apply(lambda x: int(x.replace(",","")))
    df["Founded"] = pd.to_datetime(df["Founded"], format="%b %d, %Y").dt.date
    return df

def plot_employees(df):
    """
    Bar Plot of Employees by Company

    Args:
        df (pandas.DataFrame): Processed Results - Does not work on Raw Results
    """
    ax = df["Employees"].plot.bar(rot='90')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.bar_label(ax.containers[0], labels=df["Founded"].apply(lambda x: x.strftime("Founded\n%Y")), c="grey")
    plt.show()   

def main():
    """
    Get Results from .csv file and show functionality
    """
    df = pd.read_csv("Data/ticker_info.csv", index_col="Ticker")
    df = fix_format(df)
    plot_employees(df)

if __name__ == "__main__":
    main()