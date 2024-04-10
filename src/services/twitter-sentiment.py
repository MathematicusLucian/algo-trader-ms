from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

def extract_words_from_tweet(tweet_content):
    tweet_words = []
    for word in tweet_content.split(' '):
        if word.startswith('@') and len(word) > 1:
            word = '@user'
        elif word.startswith('http'):
            word = "http"
        tweet_words.append(word)
    return tweet_words

# Roberta setup
llm = "cardiffnlp/twitter-roberta-base-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(llm)
tokenizer = AutoTokenizer.from_pretrained(llm)
labels = ['Negative', 'Neutral', 'Positive']

tweet_content = "Marsian spacecraft land in New York, and advance towards the White House."

tweet_words = extract_words_from_tweet(tweet_content)
tweet_proc = " ".join(tweet_words)
encoded_tweet = tokenizer(tweet_proc, return_tensors='pt')
# output = model(encoded_tweet['input_ids'], encoded_tweet['attention_mask'])
output = model(**encoded_tweet)

scores = output[0][0].detach().numpy()
scores = softmax(scores)

for i in range(len(scores)):
    l = labels[i]
    s = scores[i]
    print(l,s)