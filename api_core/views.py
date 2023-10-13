from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import response
from bs4 import BeautifulSoup
import requests
# Create your views here.

class WebNews(APIView):
  def get(self, request):
    news_url = "https://punchng.com/"
    response = requests.get(news_url)

    if response.status_code != 200:
      return Respnse({"error": "Failed to load webpage"})

    soup = BeautifulSoup(respose.text, 'html.parser')

    news_articles = []
    return Response(news_articles)