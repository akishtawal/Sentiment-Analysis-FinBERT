import pandas as pd
# import nltk
# nltk.download('all')
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoConfig, pipeline
import torch
# import seaborn as sns
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics import accuracy_score, precision_recall_fscore_support
# import re  # For regular expressions
# import emoji  # For handling emojis
# from nltk.corpus import stopwords  # For retrieving stopwords
# from nltk.stem import WordNetLemmatizer  # For lemmatization
import math

def score_to_sent(sentiment_score):

  if sentiment_score==1:
    return 'positive'

  if sentiment_score==2:
    return 'negative'

  else:
    return 'neutral'

def get_sentiment_finbert(text, MODEL, max_length=512, stride=256, device='cuda' if torch.cuda.is_available() else 'cpu'):
    
    # Load the pre-trained tokenizers, configuration, and model from the reference MODEL
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    config = AutoConfig.from_pretrained(MODEL)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)

    model.to(device)  # Move the model to the device

    tokens = tokenizer.encode(text, max_length=max_length, truncation=True, return_tensors='pt').to(device)  # Move the tokens to the device
    num_segments = max(1, math.ceil(len(tokens[0]) / stride))
    sentiment_logits = []

    with torch.no_grad():  # Disable gradient computation for inference
        for i in range(num_segments):
            start = i * stride
            end = min((i + 1) * stride, len(tokens[0]))
            segment_tokens = tokens[:, start:end]
            result = model(segment_tokens)
            sentiment_logits.append(result.logits)

    # Compute the average logits across segments
    avg_logits = torch.mean(torch.cat(sentiment_logits, dim=0), dim=0)

    # Compute the overall sentiment score by taking the argmax
    overall_sentiment_score = torch.argmax(avg_logits).item() + 1

    # Converting the sentiment score to a sentiment label
    overall_sentiment = score_to_sent(overall_sentiment_score)

    return overall_sentiment
