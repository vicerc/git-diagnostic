import pandas as pd

def most_retweeted(df):
	df_rt = df.sort_values(by="retweetCount", ascending=False)
	return df_rt.head(10)