from transformers import AutoTokenizer, AutoModelForSequenceClassification, TFAutoModelForSequenceClassification, BertTokenizer, BertForSequenceClassification, pipeline
import numpy as np
from scipy.special import softmax
import os
import csv
import urllib.request

def extract_words_from_tweet(tweet_content):
    tweet_words = []
    for t in tweet_content.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        tweet_words.append(t)
    return " ".join(tweet_words)

# Roberta setup
# https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment
task = "sentiment"
ROOT_DIR = os.path.abspath(os.curdir)
# llm_model = f"cardiffnlp/twitter-roberta-base-{task}"
# llm_model = os.path.join(ROOT_DIR, f"cardiffnlp/twitter-roberta-base-{task}")
# tokenizer = AutoTokenizer.from_pretrained(llm_model)
# FinBERT model fine-tuned on 10,000 manually annotated (positive, negative, neutral) sentences from analyst reports.
# https://huggingface.co/yiyanghkust/finbert-tone 
tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-tone')

labels=[]
mapping_link = f"https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/{task}/mapping.txt"

with urllib.request.urlopen(mapping_link) as f:
    html = f.read().decode('utf-8').split("\n")
    csvreader = csv.reader(html, delimiter='\t')
labels = [row[1] for row in csvreader if len(row) > 1]

# model = AutoModelForSequenceClassification.from_pretrained(llm_model)
finbert = BertForSequenceClassification.from_pretrained('yiyanghkust/finbert-tone',num_labels=3)
# model.save_pretrained(llm_model)

tweet_content = ["there is a shortage of capital, and we need extra financing",  
             "growth is strong and we have plenty of liquidity", 
             "there are doubts about our finances", 
             "profits are flat"]
# tweet_content = "Marsian spacecraft land in New York, and advance towards the White House. Lockdown. Shops closed. Estimated 2 million human fatalities. President of the USA may be dead."
# tweet_words = extract_words_from_tweet(tweet_content)
# encoded_tweet = tokenizer(tweet_words, return_tensors='pt')
# output = model(**encoded_tweet)
# scores = output[0][0].detach().numpy()
# scores = softmax(scores)

# ranking = np.argsort(scores)
# ranking = ranking[::-1]
# for i in range(scores.shape[0]):
#     l = labels[ranking[i]]
#     s = scores[ranking[i]]
#     print(f"{i+1}) {l} {np.round(float(s), 4)}")

nlp = pipeline("sentiment-analysis", model=finbert, tokenizer=tokenizer)
results = nlp(tweet_content)
print(results) 