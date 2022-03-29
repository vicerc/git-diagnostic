import pandas as pd

def top_users(df):
    df["username"] = df.apply(lambda row: row["user"]["username"], axis=1)

    df_grouped = df.groupby(by="username")

    return df_grouped.size().sort_values(ascending=False).head(10)