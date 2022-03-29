import pandas as pd

def top_days(df):
    df["day"] = df.apply(lambda row: row["date"].date(), axis=1)

    df_grouped = df.groupby(by="day")

    return df_grouped.size().sort_values(ascending=False).head(10)