from newsapi import NewsApiClient
import os

BUSINESS_NEWS_API_KEY = os.getenv("BUSINESS_NEWS_API_KEY")
ENTERTAINMENT_NEWS_API_KEY = os.getenv("ENTERTAINMENT_NEWS_API_KEY")
TECHNOLOGY_NEWS_API_KEY = os.getenv("TECHNOLOGY_NEWS_API_KEY")


class ApiProvider:

    @staticmethod
    def get_newsapi_for_business():
        return NewsApiClient(api_key=BUSINESS_NEWS_API_KEY)

    @staticmethod
    def get_newsapi_for_entertainment():
        return NewsApiClient(api_key=ENTERTAINMENT_NEWS_API_KEY)

    @staticmethod
    def get_newsapi_for_technology():
        return NewsApiClient(api_key=TECHNOLOGY_NEWS_API_KEY)
