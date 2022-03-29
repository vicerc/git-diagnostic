import pandas as pd
import re
from collections import defaultdict

def top_hashtags(df):
    hashtags = defaultdict(int)

    for tweet in df["content"]:
        query = re.findall(r"#\w+", tweet)
        for hashtag in query:
            hashtags[hashtag] += 1
    
    return pd.DataFrame(hashtags.items(), columns=['hashtag', 'count']).sort_values(by='count', ascending=False).head(10)