#Importing necessary libraries and modules
import nltk
# nltk.download('all')
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoConfig
import torch
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
import re  # For regular expressions
import emoji  # For handling emojis
from nltk.corpus import stopwords  # For retrieving stopwords
from nltk.stem import WordNetLemmatizer  # For lemmatization
import math

#Defining a function to clean the text, i.e, the Review column values
def clean_text(text):

  #Lowercasing the text
  text = text.lower()

  #Removing any alpha-numerics or digits in the text
  text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
  text = re.sub(r'\d+', '', text)

  #Converting the emojis (if present) into text format
  text = emoji.demojize(text)

  #Setting and removing the stop words (from English)
  stop_words = set(stopwords.words("english"))

  #Splitting the text by whitespace
  text = text.split() #text is now a list

  #Removing the stop words from the text
  text = (word for word in text if word not in stop_words)

  #Lemmatizing the text
  lemmatizer = WordNetLemmatizer()

  #Storing the lemmatized version of words from the text
  lemmatized_words = (lemmatizer.lemmatize(word) for word in text)

  #Joining again to form the clean text
  clean_text = ' '.join(lemmatized_words)

  #Returning the cleaned text
  return clean_text

#Function to convert the sentiment score to sentiment label 
def score_to_sent(sentiment_score):

  if sentiment_score==1:
    return 'negative'

  if sentiment_score==2:
    return 'neutral'

  else:
    return 'positive'

#Function to apply the RoBERTa Model and derive the sentiment label
def get_sentiment_roberta(text, MODEL, max_length=512, stride=256, device='cuda' if torch.cuda.is_available() else 'cpu'):
    
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