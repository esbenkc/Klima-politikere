import pandas as pd
import sentida

s = sentida.Sentida()

df = pd.read_csv("E:/Downloads/many_tweets/mf_all_tweets_20200402.csv")
df["sentiment"] = [s.sentida(i, speed = "normal", output = "mean") for i in df["text"]]

df[["sentiment", "tweet_id"]].to_csv("E:/Downloads/many_tweets/mf_all_tweets_20200402_sentiment.csv")