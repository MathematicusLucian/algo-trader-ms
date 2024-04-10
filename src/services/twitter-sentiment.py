import os
import csv
import urllib.request
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TFAutoModelForSequenceClassification, BertTokenizer, BertForSequenceClassification, pipeline
import numpy as np
from scipy.special import softmax

def extract_words_from_tweet(tweet_content):
    tweet_words = []
    for t in tweet_content.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        tweet_words.append(t)
    return " ".join(tweet_words)

def get_tokenizer_path(model, is_local, task):
    if is_local:
        ROOT_DIR = os.path.abspath(os.curdir)
        llm_model = os.path.join(ROOT_DIR, f"cardiffnlp/twitter-roberta-base-{task}")
    else:
        llm_model = 'yiyanghkust/finbert-tone' if model=="finbert-tone" else f"cardiffnlp/twitter-roberta-base-{task}"
    return llm_model

def get_tokenizer(model, task, is_local=False):
    model_path = get_tokenizer_path(model, is_local, task)
    if(model=="roberta-base"):
        return AutoTokenizer.from_pretrained(model_path)
        # FinBERT model fine-tuned on 10,000 manually annotated (positive, negative, neutral) sentences from analyst reports.
        # https://huggingface.co/yiyanghkust/finbert-tone 
    elif(model=="finbert-tone"):
        # Roberta setup
        # https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment
        return BertTokenizer.from_pretrained(model_path)
    
def get_model_for_classification(llm_model):
    if(llm_model=="roberta-base"):
        return AutoModelForSequenceClassification.from_pretrained(llm_model)
    elif(llm_model=="finbert-tone"):
        return BertForSequenceClassification.from_pretrained('yiyanghkust/finbert-tone',num_labels=3)

def determine_model(is_financial):
    return "finbert-tone" if is_financial else "roberta-base"

def save_model(model_for_classification, llm_model):
    model_for_classification.save_pretrained(llm_model)

def generate_labels(task):
    mapping_link = f"https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/{task}/mapping.txt"
    with urllib.request.urlopen(mapping_link) as f:
        html = f.read().decode('utf-8').split("\n")
        csvreader = csv.reader(html, delimiter='\t')
    return [row[1] for row in csvreader if len(row) > 1]

def get_tweets(is_financial: bool):
    return ["there is a shortage of capital, and we need extra financing",  
        "growth is strong and we have plenty of liquidity", 
        "there are doubts about our finances", 
        "profits are flat"] if is_financial else """
        Marsian spacecraft land in New York, and advance towards the White House. 
        Lockdown. Shops closed. Estimated 2 million human fatalities.
        President of the USA may be dead."""

def prepare_output__numpy(output, labels):
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    ranking = np.argsort(scores)
    ranking = ranking[::-1]
    for i in range(scores.shape[0]):
        l = labels[ranking[i]]
        s = scores[ranking[i]]
        print(f"{i+1}) {l} {np.round(float(s), 4)}")

def prepare_output__sentiment(output):
    print(output) 

def determine_sentiment(tweet_content, is_financial: bool):
    task="sentiment"
    llm_model = determine_model(is_financial)
    model_for_classification = get_model_for_classification(llm_model)
    tokenizer = get_tokenizer(llm_model, task, False)
    labels = generate_labels(task)
    if is_financial:
        nlp = pipeline("sentiment-analysis", model=model_for_classification, tokenizer=tokenizer)
        output = nlp(tweet_content)
        prepare_output__sentiment(output)
    else:
        tweet_words = extract_words_from_tweet(tweet_content)
        encoded_tweet = tokenizer(tweet_words, return_tensors='pt')
        output = model_for_classification(**encoded_tweet)
        prepare_output__numpy(output, labels)

if __name__ == "__main__":
    is_financial = True
    tweet_content = get_tweets(is_financial)
    determine_sentiment(tweet_content, is_financial)