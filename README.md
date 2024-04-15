# Algo-Bot

``python3 app.py --debug``

``flask --app app.py --debug run -p 5001``
<!-- --host=0.0.0.0 run  -->

``gunicorn --worker-tmp-dir /dev/shm``

You can generate a secret key with the following command in the terminal:
``python3 -c 'import secrets; print(secrets.token_urlsafe(16))``

## UI
`` python3 -m http.server 9000 ``

## APIs

``http://127.0.0.1:5001/historic_values_today/USD/XAU/``

https://search.r-project.org/CRAN/refmans/okxAPI/html/get_history_candles.html
https://www.okx.com/help/how-can-i-do-spot-trading-with-the-jupyter-notebook
https://www.okx.com/help/how-can-i-do-derivatives-trading-with-the-jupyter-notebook
https://www.okx.com/docs-v5/en/#overview-demo-trading-services
https://www.okx.com/docs-v5/en/#overview-market-maker-program
https://www.okx.com/docs-v5/en/#overview-broker-program
https://www.okx.com/docs-v5/en/#spread-trading
https://www.okx.com/docs-v5/en/#order-book-trading

https://www.goldapi.io/dashboard

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

# AlgoUi

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 17.0.8.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via a platform of your choice. To use this command, you need to first add a package that implements end-to-end testing capabilities.

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI Overview and Command Reference](https://angular.io/cli) page.
