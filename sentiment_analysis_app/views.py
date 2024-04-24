from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache
from .get_sentiment import clean_text, get_sentiment_roberta
from .get_sentiment_fin import get_sentiment_finbert
import logging
logger = logging.getLogger(__name__)

def sentiment_analysis_view(request):
    
    if request.method == 'POST':
        
        input_text = request.POST.get('input_text', '')

        cleaned_text = clean_text(input_text)
        logger.info(f'Processing input text: {cleaned_text}')

        MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"

        sentiment = get_sentiment_roberta(cleaned_text, MODEL)
        logger.info(f'Sentiment: {sentiment}')

        return JsonResponse({'sentiment': sentiment})
    
    else:
        return render(request, 'sentiment_analysis_temp.html')

def sentiment_analysis_fin_view(request):
    
    if request.method == 'POST':
        
        input_text = request.POST.get('input_text', '')

        finbert_model = "ProsusAI/finbert"

        sentiment = get_sentiment_finbert(input_text, finbert_model)
        
        cache.clear()
        return JsonResponse({'sentiment': sentiment})
    
    else:
        return render(request, 'sentiment_analysis_fin_temp.html')