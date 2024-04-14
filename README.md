# Algo-Bot

``python3 app.py --debug``

``flask --app app.py --debug run -p 5001``
<!-- --host=0.0.0.0 run  -->

``gunicorn --worker-tmp-dir /dev/shm``

You can generate a secret key with the following command in the terminal:
``python3 -c 'import secrets; print(secrets.token_urlsafe(16))``

## Backtseting Data

***DOGE:** [Kaggle](https://www.kaggle.com/datasets/svaningelgem/crypto-currencies-daily-prices?select=DOGE.csv)

## Twitter Sentiment Analysis

CLI: `main.py`
- `--f`: Set to True if wish to use FinBERT model rather than Roberta.

Sample output:

    `[{'label': 'Negative', 'score': 0.9966174960136414}, {'label': 'Positive', 'score': 1.0}, {'label': 'Negative', 'score': 0.9999710321426392}, {'label': 'Neutral', 'score': 0.9889441728591919}]`

## Models

### Roberta
[https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment)

### FinBERT (Financial Roberta)
***Finbert Tone:*** Fine-tuned on 10,000 manually annotated (positive, negative, neutral) sentences from analyst reports. [https://huggingface.co/yiyanghkust/finbert-tone](https://huggingface.co/yiyanghkust/finbert-tone)