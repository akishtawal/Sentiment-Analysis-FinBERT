# FinBERT Sentiment Analysis for Financial Text

This repository contains a project that utilizes HuggingFace's FinBERT model for sentiment analysis of financial text. FinBERT is a pre-trained NLP model specifically designed to analyze sentiment in the finance domain, making it an ideal choice for this task.

## Problem Statement

Financial areas like the stock market operate on tight schedules, and time is a crucial resource. Our objective is to summarize the overall sentiment of incoming financial text into three categories: Negative, Neutral, and Positive. This simplification allows for quick comprehension of large amounts of textual data, providing a valuable tool for decision-making processes in the financial sector.

## Data Exploration

The dataset used for this project was obtained from Kaggle and contained approximately 20,000 unique entries with two columns: the text (financial news headlines) and the sentiment score (-1, 0, 1 for negative, neutral, and positive sentiment, respectively). To avoid class imbalance and improve computational efficiency, a subset of 13,500 entries was randomly sampled, with 4,500 entries for each sentiment category.

## Approach

HuggingFace's transformers library in Python was used to leverage the FinBERT model, which is pre-trained on a large financial corpus and fine-tuned for financial sentiment classification tasks. FinBERT's training was based on the Financial PhraseBank by Malo et al. (2014), ensuring its suitability for analyzing financial text like the news headlines in our dataset.

## Results

Despite not fine-tuning the model on our specific dataset, the FinBERT model achieved impressive results, with an overall accuracy of 79% and F1-scores above 75% for each sentiment class (Positive: 79%, Neutral: 76%, Negative: 82%).

## Deployment

A basic web application was developed using Django, allowing users to input finance-related text and submit it for sentiment analysis. The application provides a convenient interface for quickly evaluating the overall sentiment of financial text, saving time and effort compared to reading the entire text.

## Future Scope

This project has several potential avenues for future development:

1. Integrating the current model with other pre-existing sentiment analysis models could enable sentiment analysis across a wider range of fields beyond finance.
2. News agencies and marketing channels could leverage this model to visually summarize the sentiment of news articles using colored dots (red, gray, or green) for a quick overview.
3. The model could be deployed in real-time financial news gadgets, assisting brokers in making informed buying or selling decisions based on the sentiment analysis.

## Usage

To run the web application locally, follow these steps:

1. On the terminal, run the following command:

```
python manage.py runserver 0.0.0.0:8000
```

This will enable the application to run on all IP addresses of your local system.

2. Once the app is loaded, open `0.0.0.0:8000/sentiment_fin/` in your web browser to access the web application.

3. In the text box, enter the financial text you want to analyze, and click the "Submit" button.

4. The sentiment associated with the input text will be displayed on the page.

Alternatively, you can explore deploying the application on a web server or cloud platform for wider accessibility.

Please refer to the project documentation for more detailed information and instructions.
